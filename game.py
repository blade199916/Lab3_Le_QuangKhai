# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26, 2023

@author: Quang Khai Le
"""

import pgzrun
import pygame
import pgzero
from pgzero.builtins import Actor
from random import randint

#Introducing the Actors
pacman = Actor("pacman")
pacman.pos = 118, 124

ball = Actor("ball")
ball.pos = 200, 200

#the size of the playing area
WIDTH = 500
HEIGHT = 500

score = 0
game_over = False


#These lines draw the pacman  and ball on the screen.
def draw():
    screen.fill("purple")
    pacman.draw()
    ball.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10), fontsize=40)
    
    if game_over:
        screen.fill("Pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

#The ball will be placed at least 20 pixels in from the sides of the screen
def place_ball():
    ball.x = randint(20, (WIDTH-20))
    ball.y = randint(20, (HEIGHT-20))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    
    #This moves the pacman two pixels to the left if the left arrow is pressed.
    if keyboard.left:
        pacman.x = pacman.x - 5
    #The else-if branches are used to move the pacman depending on which arrow key is pressed. 
    elif keyboard.right:
        pacman.x = pacman.x + 5
    elif keyboard.up:
        pacman.y = pacman.y - 5
    elif keyboard.down:
        pacman.y = pacman.y + 5
        
    ball_collected = pacman.colliderect(ball)
    
    if ball_collected:
        score = score + 10 #this will increase the score by ten
        place_ball()
    
clock.schedule(time_up, 10.0) #run the function 10s after the game start
place_ball()    
     


#Run it
pgzrun.go()