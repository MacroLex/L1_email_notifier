import feedparser, time, os.path, espeakng, sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
blue_led = 11
white_led = 13
red_led = 15
GPIO.setup(blue_led, GPIO.OUT)
GPIO.setup(white_led, GPIO.OUT)
GPIO.setup(red_led, GPIO.OUT)

"""
On pose les identifiants de connexion ici, de sorte que le code soit utilisable par n'importe qui avec son propre compte,
Il faut tout de même paramétrer son compte google car cette application n'est pas très sécurisée, il faut autoriser les applications moins sécurisées.
"""

USERNAME = "TEST"   
PASSWORD = "TEST"

esng = espeakng.Speaker() #On initialise le synthétiseur de voix
esng.voice = 'fr' #On met la langue en français
esng.wpm = 120 #On définit le nombre de mots par minutes

def blink():
    i=0
    for i in range(7):
        GPIO.output(blue_led, GPIO.HIGH)
        GPIO.output(white_led, GPIO.HIGH)
        GPIO.output(red_led, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(blue_led, GPIO.LOW)
        GPIO.output(white_led, GPIO.LOW)
        GPIO.output(red_led, GPIO.LOW)
        time.sleep(0.5)

while True:           
    cur_mails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"]) #récupère le nombre actuel de mail

    if os.path.isfile("emails.txt") == False: #on crée le fichier qui stocke l'ancien nombre de mail si il n'existe pas
        f = open('emails.txt', 'w')
        f.write('1'); #L'interpréteur n'aime pas lire un fichier vide
        f.close

    f = open('emails.txt', 'r')
    last_mails = int(f.read())
    f.close()

    if  cur_mails < last_mails:
        last_mails = cur_mails
        f = open('emails.txt', 'w')
        f.write(str(last_mails))
        print("pas de nouveau message")

    if  cur_mails > last_mails:
        last_mails = cur_mails
        f = open('emails.txt', 'w')
        f.write(str(last_mails))

        author = "Expéditeur : " + str(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom").entries[0].author)
        #On récupère l'expéditeur du mail avec feedparser dans le feed atom de l'adresse mail
        objet = "Objet : " + str(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom").entries[0].title)
        #On récupère l'objet du mail avec feedparser dans le feed atom de l'adresse mail
        print(author, objet)    
        esng.say("Vous avez un nouveau message !", sync = True, wait4prev = True) #On affiche puis on annonce l'arrivée d'un nouveau message
        blink()
        esng.say(author, sync = True, wait4prev = True)
        esng.say(objet, sync = True, wait4prev = True) #On affiche et on annonce l'objet et l'expéditeur du message
        
        time.sleep(60)
