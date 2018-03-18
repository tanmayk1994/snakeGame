#Tanmay H. Karadkar <karadkarth@gmail.com>
#Snake Game
#This project is from the free Udacity course to develop a pygame. 
#Course link: https://www.udemy.com/python-game-development-creating-a-snake-game-from-scratch
#Note: I'm developing this game just for the sake of getting an experience in pygame
#Feel free to download it, and modify it the way you want.


import pygame                       #straighforward importing of pygame
import sys          
import random                       #because the random function is most useful in many games
import time                         #to keep track of certain time units 

#Here, import can also be written as import pygame, sys, random, time
#I just wanted to explain the purpose of each import statement
#Now, initializing pygame in a variable

check_error = pygame.init()         #storing pygame initialization value in variable check_error

#On printing pygame.init, we get a tuple (6,0)
#6 indicates no. of successfully completed tasks and 0 indicates no. of errors
#Datatype unspecified, so default datatype is int

if check_error[1] > 0:
    print("(!) Had {0} initialized errors. Exiting...").format(check_error[1]())
    sys.exit(-1)
else:
    print("(+)Pygame Initialization Successful!")
    
#if else statement to check if any error are present during initialization
#The .format is a string formatter used in the same way as %d

