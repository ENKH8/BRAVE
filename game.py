#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:16:26 2021

@author: enkh-orgilbatkhuu
"""
import pygame

from player import Player
#creer une seconde classe qui va representer notre jeu
class Game:
    
    def __init__(self):
        #generer notre joueur
        self.player = Player()
        self.pressed = {}
