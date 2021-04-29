#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 21:57:36 2021

@author: enkh-orgilbatkhuu
"""

#avant de commencer il faut installer pygame by pip install pygame
import pygame
from game import Game
pygame.init()
        
#génerer la fênetre de notre jeu
pygame.display.set_caption("BRAVE I")
#dimention de la fênetre
screen = pygame.display.set_mode((1080, 720))

# importer de charger l'arriere plan de notre jeu
background = pygame.image.load("assets/bg.jpg")

#charger notre jeu
game = Game()

running = True

#boucle tant que cett condition est vraie
while running:
    
    #appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, 0))

    #appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)
    
    #mettre à jour l'ecran
    pygame.display.flip()
    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # que l'evenement est fermeeturee de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            # quelle touche a été uttiliséee
            if event.key == pygame.K_RIGHT:
                print("Déplacement vers droite")
            elif event.key == pygame.K_LEFT:
                print("Déplacement vers gauche")
