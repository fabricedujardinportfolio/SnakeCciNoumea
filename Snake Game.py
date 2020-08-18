#Décommenté par brique pour voir ce que cela fait 

# Aide pour commencé 
# init() = Initialise tous les modules Pygame importés(retourne un tuple indiquant le succès
#          et l 'échec des initialisations)

# display.set_mode () = Prend un tuple ou une liste comme paramètre pour créer une surface (tuple préféré)

# update() = Met à jour l'écran

# quit() = Utilisé pour tout réinitialiser

# set_caption() = Définira le texte de la légende en haut de l'écran d'affichage

# event.get() = Renvoie la liste de tous les événements

# Surface.fill() = Remplira la surface d'une couleur unie

# time.Clock() = Aide à suivre le temps

# font.SysFont() = Créera une police Pygame à partir des ressources de polices système

#draw.rect () = aide à dessiner un rectangle avec la couleur et la taille désirées.

#//////////////////////////////////////////////////
#Création de l'écrant Brique 1 
#/////////////////////////////////////////////////

# import pygame
# pygame.init()
# dis=pygame.display.set_mode((400,300))
# pygame.display.update()
# pygame.quit()
# quit()


##Ici tout fonctione cependant l'ecrant ne reste pas réglons cela voulais vous ? ... respecter la case 

##//////////////////////////////////////////////////
##Utilison un boucle while Brique 2
##/////////////////////////////////////////////////

# import pygame
# pygame.init()   ##||||| utiliser les méthodes init ()  et quit ()  pour initialiser et désinitialiser tout au début et à la fin du code.
# dis=pygame.display.set_mode((400,300))  ##||||| Pour créer l'écran à l' aide Pygame, vous devrez utiliser la display.set_mode ()  fonction . 
# pygame.display.update()  ##||||| La méthode update ()  est utilisée pour mettre à jour toutes les modifications apportées à l'écran. La méthode flip () fonctionerais tout aussi bien.
# pygame.display.set_caption('Snake game by fabrice')  ##*||||| Explication plus bas
# game_over=False
# while not game_over:  ##||||| Boucle while
#     for event in pygame.event.get():  ##*||||| Explication plus bas
#         print(event)   ##||||| imprime toutes les actions qui se déroulent à l'écran
 
# pygame.quit()
# quit()  ## ||||| utiliser les méthodes init ()  et quit ()  pour initialiser et désinitialiser tout au début et à la fin du code.


# Lorsque vous exécutez ce code, vous verrez que l 'écran
#  que vous avez vu précédemment ne se ferme pas et qu 'il 
#  renvoie toutes les actions qui se déroulent dessus.
#  J 'ai fait cela en utilisant la fonction event.get () * .
#   De plus, j 'ai nommé l' écran «Snake Game by fabrice»
#   en utilisant la fonction display.set_caption ()  .

##//////////////////////////////////////////////////
##probléme de fermeture applications Brique 3
##/////////////////////////////////////////////////



##Spécifions la fermeture de l'ecrant avec événement appelé «QUIT»
# import pygame
# pygame.init()
# dis=pygame.display.set_mode((400,300))
# pygame.display.update()
# pygame.display.set_caption('Snake game by fabrice')
# game_over=False
# while not game_over:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:  ## ||||| il doit être utilisé comme suit.
#             game_over=True
 
# pygame.quit()
# quit()

# Alors maintenant, votre écran est prêt. 
# La partie suivante consiste à dessiner 
# notre serpent de iles de ouvéa sur l'écran qui 
# est couvert dans le sujet suivant.


##//////////////////////////////////////////////////
##Créez le serpent: Brique 4
##/////////////////////////////////////////////////

# import pygame
# pygame.init()
# dis=pygame.display.set_mode((400,300))
 
# pygame.display.set_caption('Snake game by fabrice')
 
# blue=(0,0,255)  ##|||||quelques variables de couleur
# red=(255,0,0)   ##|||||quelques variables de couleur
 
# game_over=False
# while not game_over:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             game_over=True
#     pygame.draw.rect(dis,blue,[200,150,10,10]) ##||||| draw.rect () nous aidera à dessiner le rectangle avec la couleur et la taille désirées.
#     pygame.display.update() ##||||| Le update à était placer selon le sens de la lecture  
# pygame.quit()
# quit()

## sa ces sur cet un serpent calédonien ! 

# ##*avait vous remarqué que nous avons déplacé le update 

##//////////////////////////////////////////////////
##Déplacer le serpent: Brique 5
##/////////////////////////////////////////////////

##Pour déplacer le serpent, Nous devons utiliser les événements clés présents dans la classe KEYDOWN de Pygame.
# Les événements qui sont utilisés ici sont, K_UP, K_DOWN, K_LEFT et K_RIGHT
#  pour faire bouger le serpent respectivement vers le haut, le bas, la gauche et la droite.
#  En outre, l'écran d'affichage passe du noir par défaut au blanc à l'aide de la méthode fill ()  .

##Créons de nouvelles variables x1_change et y1_change afin de stocker les valeurs de mise à jour des coordonnées x et y pour que notre serpent puisse pensé .

# import pygame
 
# pygame.init()
 
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)
 
# dis = pygame.display.set_mode((800, 600))
# pygame.display.set_caption('Snake Game by fabrice')
 
# game_over = False
 
# x1 = 300
# y1 = 300
 
# x1_change = 0       
# y1_change = 0
 
# clock = pygame.time.Clock()
 
# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 x1_change = -10
#                 y1_change = 0
#             elif event.key == pygame.K_RIGHT:
#                 x1_change = 10
#                 y1_change = 0
#             elif event.key == pygame.K_UP:
#                 y1_change = -10
#                 x1_change = 0
#             elif event.key == pygame.K_DOWN:
#                 y1_change = 10
#                 x1_change = 0
 
#     x1 += x1_change 
#     y1 += y1_change
#     dis.fill(white)
#     pygame.draw.rect(dis, black, [x1, y1, 10, 10])
 
#     pygame.display.update()
 
#     clock.tick(30)
 
# pygame.quit()
# quit()



## Oulala il me fait déja  peur se serpent ! 
##laissez-vous du temps à comprendre cette étape . 
#Plusieurs problèmes sont survenue . essayons de les régler quand pensé vous ?
#17/08/2020



##//////////////////////////////////////////////////
##PRODUCTION Game Over quand Snake atteint les limites: Brique 6
##/////////////////////////////////////////////////

# Ici, si le joueur atteint les limites de
# l 'écran, il perd. Pour préciser cela, Nous utiliserons  une
# instruction «if» qui définit les limites pour que les
# coordonnées x et y du serpent soient inférieures ou
# égales à celle de l 'écran. 
# supprimons les codes en dur et utilisons des variables
# à la place afin que cela devienne facile au cas où nous
# voudrions apporter des modifications au jeu plus tard.
# import pygame
# import time
# pygame.init()
 
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)
 
# dis_width = 800
# dis_height  = 600
# dis = pygame.display.set_mode((dis_width, dis_width))
# pygame.display.set_caption('Snake Game by fabrice')
 
# game_over = False
 
# x1 = dis_width/2
# y1 = dis_height/2
 
# snake_block=10
 
# x1_change = 0
# y1_change = 0
 
# clock = pygame.time.Clock()
# snake_speed=30
 
# font_style = pygame.font.SysFont(None, 50)
 
# def message(msg,color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width/2, dis_height/2])
 
# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 x1_change = -snake_block
#                 y1_change = 0
#             elif event.key == pygame.K_RIGHT:
#                 x1_change = snake_block
#                 y1_change = 0
#             elif event.key == pygame.K_UP:
#                 y1_change = -snake_block
#                 x1_change = 0
#             elif event.key == pygame.K_DOWN:
#                 y1_change = snake_block
#                 x1_change = 0
 
#     if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #||||| *
#         game_over = True
 
#     x1 += x1_change
#     y1 += y1_change
#     dis.fill(white)
#     pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
 
#     pygame.display.update()
 
#     clock.tick(snake_speed)
 
# message("Tu a perdue",red)
# pygame.display.update()
# time.sleep(2)
 
# pygame.quit()
# quit()

##//////////////////////////////////////////////////
##Ajoutons de la nourriture: Brique 7
##/////////////////////////////////////////////////


#Ici, nous ajouterons de la nourriture pour le serpent 
# et quand le serpent croise cette nourriture,
#  nous aurons un message disant «Miam !!». De plus,
#  nous ferons un petit changement dans lequel nous inclurerons  
# les options pour quitter le jeu ou pour jouer 
# à nouveau lorsque le joueur perd.

# import pygame
# import time
# import random
 
# pygame.init()
 
# white = (255, 255, 255)
# black = (0, 0, 0)
# red = (255, 0, 0)
# blue = (0, 0, 255)
 
# dis_width = 800
# dis_height = 600
 
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Snake Game by fabrice')
 
# clock = pygame.time.Clock()
 
# snake_block = 10
# snake_speed = 30
 
# font_style = pygame.font.SysFont(None, 30)
 
 
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width/3, dis_height/3])
 
 
# def gameLoop():  # créer une fonction
#     game_over = False
#     game_close = False
 
#     x1 = dis_width / 2
#     y1 = dis_height / 2
 
#     x1_change = 0
#     y1_change = 0
 
#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
 
#     while not game_over:
 
#         while game_close == True:
#             dis.fill(white)
#             message("Tu as perdu! Appuyez à nouveau sur Q-Quit ou C-Play", red)
#             pygame.display.update()
 
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()
 
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
 
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
 
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(white)
#         pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])
#         pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
#         pygame.display.update()
 
#         if x1 == foodx and y1 == foody:
#             print("Délicieux!!")
#         clock.tick(snake_speed)
 
#     pygame.quit()
#     quit()
 
 
# gameLoop()

##//////////////////////////////////////////////////
##PRODUCTION Augmentons la longueur du serpent: Brique 8
##/////////////////////////////////////////////////


#Le code suivant augmentera la taille de notre serpend de ouvéa lorsqu'il
#mange la nourriture. De plus, si le serpent entre en collision
#avec son propre corps, le jeu est terminé et vous verrai un
#message comme «Vous avez perdu ! Appuyez sur Q-Quit ou C-Play 
#encore “. La longueur du serpent est essentiellement contenue 
#dans une liste et la taille initiale spécifiée dans le code 
# suivant est d'un bloc.

# import pygame
# import time
# import random
 
# pygame.init()
 
# white = (255, 255, 255)
# yellow = (255, 255, 102)
# black = (0, 0, 0)
# red = (213, 50, 80)
# green = (0, 255, 0)
# blue = (50, 153, 213)
 
# dis_width = 600
# dis_height = 400
 
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Snake Game by fabrice')
 
# clock = pygame.time.Clock()
 
# snake_block = 10
# snake_speed = 15
 
# font_style = pygame.font.SysFont("bahnschrift", 25)
# score_font = pygame.font.SysFont("comicsansms", 35)
 
# def our_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
# def gameLoop():
#     game_over = False
#     game_close = False
 
#     x1 = dis_width / 2
#     y1 = dis_height / 2
 
#     x1_change = 0
#     y1_change = 0
 
#     snake_List = []
#     Length_of_snake = 1
 
#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
#     while not game_over:
 
#         while game_close == True:
#             dis.fill(blue)
#             message("Tu as perdu! Appuyez à nouveau sur C-Play ou sur Q-Quit", red)
 
#             pygame.display.update()
 
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()
 
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0
 
#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(blue)
#         pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
#         snake_Head = []
#         snake_Head.append(x1)
#         snake_Head.append(y1)
#         snake_List.append(snake_Head)
#         if len(snake_List) > Length_of_snake:
#             del snake_List[0]
 
#         for x in snake_List[:-1]:
#             if x == snake_Head:
#                 game_close = True
 
#         our_snake(snake_block, snake_List)
 
 
#         pygame.display.update()
 
#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#             Length_of_snake += 1
 
#         clock.tick(snake_speed)
 
#     pygame.quit()
#     quit()
 
 
# gameLoop()

##//////////////////////////////////////////////////
##PRODUCTION Affichage du score: Brique 9
##/////////////////////////////////////////////////

#Dernier point mais non le moindre, en devra 
# afficher le score du joueur. Pour ce faire, 
# créons une nouvelle fonction comme "Votre_score". 
# Cette fonction affichera la longueur du serpent soustraite 
# de 1 car c'est la taille initiale du serpent.

import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by fabrice')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def Your_score(score):
    value = score_font.render("ton Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            dis.fill(blue)
            message("Tu as perdu! Appuyez à nouveau sur C-Play ou sur Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()



#Avec cela, nous sommes arrivés à la fin du Snake Game en Python. 
#J'espère que vvous avais mieu compris
#Assurez-vous de pratiquer autant que possible et inversez votre expérience. Moi méme je l'utilise encore ... 

#Vous avais fait un exelent travail good jobe CCI 2020 ...



