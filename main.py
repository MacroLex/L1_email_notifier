import feedparser, time, os.path

USERNAME = "joachimveran06"   
PASSWORD = "StBarth2002"     

while True:

        cur_mails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])

        if os.path.isfile("emails.txt") == False: #create the file if it doesnt exist
                f = open('emails.txt', 'w')
                f.write('1'); #The interpreter doesn't like reading from an empty file
                f.close
        
        print(cur_mails)

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

            author = str(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom").entries[0].author)
            objet = str(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom").entries[0].title)
            
            print("expéditeur : ", author)
            print("objet : ", objet)
            #afficher et faire lire "'expéditeur : ' author"
            #afficher et faire lire "'objet : ' objet"

        f.close()
        time.sleep(60)