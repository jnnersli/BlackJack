import sys

sys.path.append('../BlackjackModel/')
from Card import *
from Deck import *
from Player import *

sys.path.append('../BlackjackView/')
from Output import *

#Controller:
#Asks the view for input and waits for it.
#Once input is received, it passes it to the model to update itself
#and then passes the updated information to the view to display it to the user.

class Dealer:
    def main():
        #Initialize model
        player = Player()
        dealer = Player()
        deck = Deck()
    
        #Initialize input/output
        input = sys.stdin #console input
        output = sys.stdout #console output
        view = Output(input, output)
    
        view.welcomeMessage()
        deck.shuffle()
        
        #Both the player and the dealer are given 2 cards.
        for i in range(0, 2):
            player.hit(deck.draw())
            dealer.hit(deck.draw())
            
        #The player can see both of their cards but only one of the dealers cards.
        view.printCardDealer(dealer.hand()[0])
        
        for c in player.hand():
            view.printCard(c)
        
        #Player goes first
        dealer.setGameState("waiting")
        
        #The player now has two options: (1) ”hit”, or (2) ”stand”.
        view.prompt()
        nextMove = view.read()
        
        #The player can hit as many times as they wish until they stand.
        while nextMove == "hit\n":
            c = deck.draw()
            view.printCard(c)
            player.hit(c)
            
            #If at any point their hand goes over 21, they automatically lose.
            if player.countHand() > 21:
                view.printLoss()
                break
                
            nextMove = view.read()
            
        if nextMove == "stand\n":
            #Switch turns
            player.setGameState("waiting")
            dealer.setGameState("playing")
            
            #If the value of the dealers hand is 17 or more they automatically stand otherwise they automatically keep taking more cards until it is at least 17.
            while dealer.countHand() < 17:
                dealer.hit(deck.draw())
                
            for c in dealer.hand():
                view.printCardDealer(c)
                
            #If the dealers hand goes over 21 the player wins.
            if dealer.countHand() > 21:
                view.printWin()
                
            #If the dealers hand is between 17 and 21 (inclusive), then the winner is whoever has the bigger hand.
            else:
                if player.countHand() > dealer.countHand():
                    view.printWin()
                    
                elif player.countHand() < dealer.countHand():
                    view.printLoss()
                    
                else:
                    view.printTie()
    
if __name__ == '__main__':
    Dealer.main()