import random
from Card import *

#Simple deck of cards with basic functions draw and shuffle

class Deck:
    #Constructs a deck and initializes the card names + values
    def __init__(self):
        self.__size = 52
        self.__cards = []
        #Loop through four suits
        for i in range(0, 4):
            #Loop through all Card enum values
            for c in (Card):
                self.__cards.append(c)
            
    def size(self):
        return self.__size
        
    #This is really only used for testing
    def cards(self):
        return self.__cards
        
    #Remove and return the last card (makes shuffling easier than taking the first card)
    def draw(self):
        if self.__size > 0:
            c = self.__cards[-1]
            self.__cards.pop()
            self.__size -= 1
            return c
        else:
            return None
            
    #Randomly shuffle the cards
    #This is using the Fisher-Yates algorithm (modern)
    #https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm
    def shuffle(self):
        for i in range(self.__size - 1, 1, -1):
            j = random.randint(0, i)
            self.__swap(i, j)
            
    #Helper function for shuffle
    def __swap(self, i, j):
        temp = self.__cards[i]
        self.__cards[i] = self.__cards[j]
        self.__cards[j] = temp