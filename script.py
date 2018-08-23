#IMPORTS:
import pygame, sys

file_player = "vaisseau.png"
file_alien = "alien.png"
file_arriere_plan = "arriere-plan.png"
file_menu = "menu.png"
file_missile = "missile.png"
file_font = "space_invaders.ttf"

class Player(pygame.sprite.Sprite):

    def __init__(self, image,coord, speed):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect().move(coord)

        self.screen = pygame.display.get_surface().get_rect()


        self.state = "stable"
        self.speed = speed
        self.movepos = [0,0]

    def update(self):
        newpos = self.rect.move(self.movepos)
        if self.screen.contains(newpos):
            self.coord=self.movepos
            self.rect = newpos
        pygame.event.pump()


    def moveleft(self):
        self.movepos[0]-=self.speed
        self.state = "moveleft"

    def moveright(self):
        self.movepos[0]+=self.speed
        self.state = "moveright"

    def tirer(self, image, speed):
        bullet = Bullet(image, (self.rect.x+int(self.rect.w/2)-3, self.rect.y+int(self.rect.h/2)), speed)
        return bullet




class Bullet(pygame.sprite.Sprite):
    def __init__(self, image, coord, speed):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect().move(coord)

        self.screen = pygame.display.get_surface().get_rect()


        self.speed = speed


    def update(self):
        movepos = [0,-self.speed]
        newpos = self.rect.move(movepos)
        if self.screen.contains(newpos):
            self.rect = newpos
        else:
            self.kill()
        pygame.event.pump()


#On creer la clase principale qui contient tous les éléments liées à l'affichage de la fenêtre et sa fermeture
def main():

    pygame.init() #On initialise pygame, on se prépart à l'utilisé

    #Taille de la fenetre qui s'adapte a l'ecran
    ratio=7/9
    info = pygame.display.Info()
    if info.current_w*ratio<=info.current_h:
        largeur=int(info.current_w)
        hauteur=int(info.current_w*ratio)
    else:
        largeur=int(info.current_h*(ratio))
        hauteur=int(info.current_h)

    print(largeur, hauteur)

    #VARIABLES
    speed_player = 10 #px/frame
    speed_bullet = 3
    player_x = (largeur / 2 - 70) #On s'en sert pour placer le joueur sur l'axe x
    player_y = (hauteur - 90 - 20) #On s'en sert pour placer le joueur sur l'axe y

    #AFFICHAGE:
    app = pygame.display.set_mode((largeur, hauteur), pygame.FULLSCREEN) #On affiche la fenetre avec comme parametre largeur et hauteur
    pygame.display.set_caption("Space Invaders") #On change le titre de la fenetre

    clock = pygame.time.Clock()

    background = pygame.image.load(file_arriere_plan).convert_alpha() #On définit l'arrière arriereplan
    menu = False
    app.blit(background, (0, 0)) #On affiche l'arrière plan
    #
    # #MENU:
    # largeur_menu = (largeur / 2) - 10 # => 340
    # hauteur_menu = 10
    # menu_ = pygame.image.load("menu.png").convert_alpha()
    # menu = False #pour savoir si l'on est au menu ou non
    # app.blit(menu_, (largeur_menu, hauteur_menu))

    # #MUSIQUE DE FOND:
    # pygame.mixer.music.load("audio.wav")
    # pygame.mixer.music.play()
    # volume = pygame.mixer.music.get_volume() #Retourne la valeur du volume, entre 0 et 1
    # pygame.mixer.music.set_volume(0.5) #Met le volume à 0.5 (moitié)

    player = Player(file_player, (player_x, player_y), speed_player)
    players = pygame.sprite.RenderPlain(player)

    bullets = pygame.sprite.RenderPlain()

    #EVENEMENTS:
    while True: #Tans que ouvert = True:
        clock.tick(120) #Limite a 120 fps
        for event in pygame.event.get(): #On recupère tous les évenements de pygame
            if event.type == pygame.QUIT: #Si l'evenement = quit,
                return
            if event.type == pygame.KEYDOWN: #On récupère l'evenement 'KEYDOWN' de pygame
                #POUR LES CHIFFRES AU DESSUS DE 'AZERTY':
                if menu:
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1: #Si la touche préssée est 1,
                        menu = False #On est plus dans le menu
                    elif event.key == pygame.K_2 or event.key == pygame.K_KP2: #Si la touche est 2,
                        return
                elif not menu:
                    if event.key == pygame.K_LEFT: #Si la flèche gauche est pressée,
                        player.moveleft()

                    elif event.key == pygame.K_RIGHT:#Si la flèche droite est pressée,
                        player.moveright()

                    elif event.key == pygame.K_SPACE: #Si la barre espace est préssée,
                         #On tire une bullet selon la position du joueur
                         bullets.add(player.tirer(file_missile, speed_bullet))
                    elif event.key == pygame.K_ESCAPE:
                        return
            elif event.type == pygame.KEYUP:
                if menu:
                    pass
                elif not menu:
                    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                        player.state="stable"
                        player.movepos = [0,0]


        for bullet in bullets.sprites():
            app.blit(background, bullet.rect, bullet.rect)
        bullets.update()
        bullets.draw(app)

        app.blit(background, player.rect, player.rect)
        players.update()
        players.draw(app)

        pygame.display.update() #On rafraichit la fenêtre a chaque execution de code

if __name__ == "__main__":
    main()
