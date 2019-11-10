from Card import *

#One of the blackjack players

class Player:
    def __init__(self):
        self.__hand = []
        self.__gameState = "playing" #Keeps players from playing out of turn
        
    def hand(self):
        return self.__hand.copy()
        
    def gameState(self):
        return self.__gameState
    
    def setGameState(self, state):
        self.__gameState = state
        
    #Add a card to the hand
    def hit(self, card):
        if self.__gameState == "playing":
            self.__hand.append(card)
            
    #Sum up the cards in the hand
    def countHand(self):
        total = 0
        aceCount = 0 #Keep a count of the number of aces in the hand
        
        for card in self.__hand:
            #The  ace  has  the  value  of  11...
            if card is Card.ACE:
                total += 11
                aceCount += 1
                
            #Jack, Queen, and King are all worth 10.
            elif card is Card.JACK or card is Card.QUEEN or card is Card.KING:
                total += 10
                
            else:
                total += card.value
            
        #...Unless it is in a hand with a value over 21 in which case it has the value of 1.
        while aceCount > 0 and total > 21:
            total -= 10
            aceCount -= 1
            
        return total
            