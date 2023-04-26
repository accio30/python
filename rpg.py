#Pre start#

import cmd
import textwrap
import sys
import time
import os
import random


#Define things#

screen_width = 100


#Define PLayer#

class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.xp = 0
        self.status = []
        self.location = 'start'

player1 = player()

#Title Screen setup#

def pre_start():
   os.system('clear')
   print("################################")
   print("#########   -WELCOME-   ########")
   print("##-To this rpg text adventure-##")
   print("################################")
   print("################################")
   print("##########   -PLAY-   ##########")
   print("########## -OPTIONS-  ##########")
   print("##########   -QUIT-   ##########")
   print("################################")

   title_screen_select()

#Title Screen interactivity#

def title_screen_select():
    option = input("> ")
    if option.lower() == ("play"):
        start()
    elif option.lower() == ("options"):
        help_screen()
    elif option.lower() == ("quit"):
        sys.exit
    while option.lower() not in ["play", "help", "quit"]:
      print("Enter a valid command")
      option = input("> ")
      if option.lower() == ("play"):
        start()
      elif option.lower() == ("options"):
        help_screen()
      elif option.lower() == ("quit"):
        sys.exit
        



#help Screen#

   
def help_screen():
   os.system('clear')
   print("################################")
   print("#########   -OPTIONS-   ########")
   print("###-TYPE THE OPTION DESIRED- ###")
   print("################################")
   print("################################")
   print("#########  -CONTROLS- ##########")
   print("############  -a1- #############")
   print("##########   -MENU-   ##########")
   print("################################")
   help_screen_select()
   
#help interactivity#

def help_screen_select():
    option = input("> ")
    if option.lower() == ("controls"):
        controls_help_screen()
    elif option.lower() == ("a1"):
        a1()
    elif option.lower() == ("menu"):
          start()
          
    while option.lower() not in ["controls", "a1", "a2"]:
      print("Enter a valid command")
      option = input("> ")
      if option.lower() == ("controls"):
        controls_help_screen()
      elif option.lower() == ("a1"):
        a1()
      elif option.lower() == ("menu"):
          start()

#control Screen#

def controls_help_screen():
   print("################################")
   print("#########  -CONTROLS-   ########")
   print("################################")
   print("################################")
   print("################################")
   print("##     -UNDER DEVELOPMENT-    ##")
   print("##     -UNDER DEVELOPMENT-    ##")
   print("##########   -MENU-   ##########")
   print("################################")
   controls_screen_select()       

#control Screen interactivity#

def controls_screen_select():
    option = input("> ")
    if option.lower() == ("controls"):
        controls_help_screen()
    elif option.lower() == ("a1"):
        a1()
    elif option.lower() == ("menu"):
          start()
          
    while option.lower() not in ["controls", "a1", "a2"]:
      print("Enter a valid command")
      option = input("> ")
      if option.lower() == ("controls"):
        controls_help_screen()
      elif option.lower() == ("a1"):
          a1()
      elif option.lower() == ("menu"):
          start()

def a1():
    print("Under Develpment")
    start()


def start():
  pre_start()

    
        


start()
        
        
    



        
    


