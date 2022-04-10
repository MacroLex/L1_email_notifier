import feedparser, time, os.path, espeakng, sys, pygame

USERNAME = "test"   
PASSWORD = "test"

esng = espeakng.Speaker()
esng.voice = 'fr'
esng.wpm = 120

pygame.init()
res = pygame.display.list_modes()
width, heigth = res[0]
screen = pygame.display.set_mode([width, heigth])
pygame.display.toggle_fullscreen()
pygame.mouse.set_visible = False

def quit_app():
    pygame.quit()
    sys.exit(0)
    
def set_text(string, coordx, coordy, fontSize):

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
    
                
    cur_mails = int(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom")["feed"]["fullcount"])

    if os.path.isfile("emails.txt") == False: #create the file if it doesnt exist
        f = open('emails.txt', 'w')
        f.write('1'); #The interpreter doesn't like reading from an empty file
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
        objet = "Objet : " + str(feedparser.parse("https://" + USERNAME + ":" + PASSWORD +"@mail.google.com/gmail/feed/atom").entries[0].title)
            
        screen.fill((255, 255, 255))
        texte4 = set_text("Vous avez un nouveau message !", width//2, heigth//2, 60)
        screen.blit(texte4[0], texte4[1])
        pygame.display.update()
        esng.say("Vous avez un nouveau message !", sync = True, wait4prev = True)
        texte2 = set_text(author, width//2, heigth//3, 60)
        screen.blit(texte2[0], texte2[1])
        pygame.display.update()
        esng.say(author, sync = True, wait4prev = True)
        texte3 = set_text(objet, width//2, 2*(heigth//3), 60)
        screen.blit(texte3[0], texte3[1])
        pygame.display.update()
        esng.say(objet, sync = True, wait4prev = True)
        #afficher et faire lire "'expéditeur : ' author"
        #afficher et faire lire "'objet : ' objet"

    f.close()
    for i in range(6000):
        time.sleep(0.002)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_app()
