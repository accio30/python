import cmp
import textwrap
import sys
import Time
import os
import random

screen_width = 100

class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.xp = 0
        self.status = []
        self.location = 'start'

player1 = player()

def title_screen_select():
    option = input("> ")
    if option.lower() == ("play"):
        start()
    elif option.lower() == ("help"):
        help()
    elif option.lower() == ("quit"):
        sys.exit
    while option.lower() not in ["play", "help", "quit"]:
      print("Enter a valid command")
      option = input("> ")
      if option.lower() == ("play"):
        start()
      elif option.lower() == ("help"):
        help()
      elif option.lower() == ("quit"):
        sys.exit
def pre_start():
   os.system('clear')
   print()
   title_screen_select()
def helpm():
   print()
   title_screen_select()

def start():
   