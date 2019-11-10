import sys
sys.path.append('../BlackjackModel/')

from Card import *

#View:
#Handles the logic for displaying information and reading input.

class Output:
    def __init__(self, input, output):
        self.output = output
        self.input = input
        
    #..........Input functions............
    
    def read(self):
        return self.input.readline()
        
    #..........Output functions.............
        
    def welcomeMessage(self):
        self.output.write("Welcome to Jenny's Blackjack Casino >:)\n")
        self.output.write("The dealer will now deal out two cards.\n")
        
    #Ask for input
    def prompt(self):
        self.output.write("Would you like to \"hit\" or \"stand\"?\n")
        
    #Print the player's card
    def printCard(self, card):
        self.output.write(card.name + "\n")
        
    #Print the dealer's card
    def printCardDealer(self, card):
        self.output.write("The dealer has: " + card.name + "\n")
        
    def printWin(self):
        self.output.write("You won!\n")
        
    def printLoss(self):
        self.output.write("You lost :(\n")
        
    def printTie(self):
        self.output.write("You have tied with the dealer.\n")