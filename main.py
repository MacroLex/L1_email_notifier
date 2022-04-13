import feedparser, time, os.path, espeakng, sys, pygame

"""
On pose les identifiants de connexion ici, de sorte que le code soit utilisable par n'importe qui avec son propre compte,
Il faut tout de même paramétrer son compte google car cette application n'est pas très sécurisée, il faut autoriser les applications moins sécurisées.
"""

USERNAME = "test"   
PASSWORD = "test"

esng = espeakng.Speaker() #On initialise le synthétiseur de voix
esng.voice = 'fr' #On met la langue en français
esng.wpm = 120 #On définit le nombre de mots par minutes

pygame.init() #On initialise pygame, puis on définit automatiquement la résolution de l'écran en fonction de l'écran qu'on souhaite utiliser.
res = pygame.display.list_modes()
width, heigth = res[0]
screen = pygame.display.set_mode([width, heigth])
pygame.display.toggle_fullscreen() #On met en plein écran
pygame.mouse.set_visible = False #On affiche pas la souris

def quit_app(): #Cette fonction sert à quitter l'interpréteur si il y a un problème
    pygame.quit()
    sys.exit(0)
    
def set_text(string, coordx, coordy, fontSize): #On crée la fonction qui permet d'afficher du texte sur pygame
    font = pygame.font.Font('freesansbold.ttf', fontSize)
    text = font.render(string, True, (0, 0, 0)) 
    textRect = text.get_rect()
    textRect.center = (coordx, coordy) 
    return (text, textRect)

while True:
    screen.fill((255, 255, 255))
    texte1 = set_text("Pas de nouveaux messages !", width//2, heigth//2, 60)
    screen.blit(texte1[0], texte1[1])
    pygame.display.update()
    
                
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

    if  cur_mails > last_mails:
        last_mails = cur_mails
        f = open('emails.txt', 'w')
        f.write(str(last_mails))

        author = "Expéditeur : " + str(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom").entries[0].author)
        #On récupère l'expéditeur du mail avec feedparser dans le feed atom de l'adresse mail
        objet = "Objet : " + str(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom").entries[0].title)
        #On récupère l'objet du mail avec feedparser dans le feed atom de l'adresse mail
            
        screen.fill((255, 255, 255)) #On remet un fond
        texte4 = set_text("Vous avez un nouveau message !", width//2, heigth//2, 60) 
        screen.blit(texte4[0], texte4[1])
        pygame.display.update()
        esng.say("Vous avez un nouveau message !", sync = True, wait4prev = True) #On affiche puis on annonce l'arrivée d'un nouveau message
        texte2 = set_text(author, width//2, heigth//3, 60)
        screen.blit(texte2[0], texte2[1])
        pygame.display.update()
        esng.say(author, sync = True, wait4prev = True)
        texte3 = set_text(objet, width//2, 2*(heigth//3), 60)
        screen.blit(texte3[0], texte3[1])
        pygame.display.update()
        esng.say(objet, sync = True, wait4prev = True) #On affiche et on annonce l'objet et l'expéditeur du message

    f.close()
    for i in range(6000): #On attend environ 1 minute avant de refaire le code d'avant, tout en permettant à l'utilisateur s'il le désire de quitter l'application
        time.sleep(0.002)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_app()
