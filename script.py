#IMPORTS:
import pygame, sys

#On créer la clase principale qui contient tous les éléments liées à l'affichage de la fenêtre et sa fermeture
class Principale():

    pygame.init() #On initialise pygame, on se prépart à l'utilisé

    #VARIABLES:
    ouvert = True #On assignera false pour fermer la fenêtre via la boucle while
    largeur = 700 #On définit la largeur de la fenêtre principale
    hauteur = 900 #On définit la hauteur de la fenêtre principale

    #AFFICHAGE:
    app = pygame.display.set_mode((largeur, hauteur)) #On affiche la fenetre avec comme parametre largeur et hauteur
    arriereplan = pygame.image.load("arrière-plan.png").convert_alpha() #On définit l'arrière arriereplan
    app.blit(arriereplan, (0, 0)) #On affiche l'arrière plan
    pygame.display.set_caption("Space Invaders") #On change le titre de la fenetre

    #MENU:
    menu = pygame.image.load("menu.png").convert_alpha()
    app.blit(menu, (10, 10))

    #EVENEMENTS:
    while ouvert: #Tans que ouvert = True:

        for event in pygame.event.get(): #On recupère tous les evenement de pygame
            if event.type == pygame.QUIT: #Si l'evenement = quit,
                ouvert = False #On assigne 'ouvert' en tans que False et la boucle s'arrête
                sys.exit() #On quitte le programme

            if event.type == pygame.KEYDOWN: #On récupère l'evenement 'KEYDOWN' de pygame
                if event.key == pygame.K_1: #Si la touche préssée est 1,
                    app.blit(arriereplan, (0, 0)) #On enlève le menu et on va commencer a jouer
                elif event.key == pygame.K_2: #Si la touche est 2,
                    sys.exit() #On quitte le programme
        pygame.display.update() #On rafraichit la fenêtre a chaque execution de code
