import unittest

import sys
sys.path.append('../BlackjackModel/')
from Player import *
from Deck import *
from Card import *

#Unit tests for BlackjackModel/Player.py

class PlayerTest(unittest.TestCase):
    #..........Setup/teardown.............

    def setUp(self):
        print("Beginning test.")
        
    def tearDown(self):
        print("Test finished.")
        
    #...........Tests..............
    
    def test_setGamestate(self):
        player = Player()
        player.setGameState("waiting")
        self.assertEqual("waiting", player.gameState())

    #Amount of cards in the player's hand should increase by 1 after hit
    def test_hit(self):
        deck = Deck()
        player = Player()
        sizeBefore = len(player.hand())
        player.hit(deck.draw())
        
        self.assertEqual(len(player.hand()), sizeBefore + 1)
    
    #Ace should count as 11 while the hand is less than 21
    def test_countHand1(self):
        player = Player()
        player.hit(Card.ACE)
        player.hit(Card.TEN)
        self.assertEqual(21, player.countHand())
        
    #Aces should count as 1 in a hand worth over 21
    def test_countHand2(self):
        player = Player()
        player.hit(Card.ACE) #11 here
        player.hit(Card.TEN) #10 here (21 total)
        player.hit(Card.ACE) #1 here and the previous ace is also worth 1 (12 total)
        self.assertEqual(12, player.countHand())
        
    #Jack, Queen, and King should all count as 10
    def test_countHand3(self):
        player = Player()
        player.hit(Card.JACK)
        player.hit(Card.QUEEN)
        player.hit(Card.KING)
        self.assertEqual(30, player.countHand())
        
        
if __name__ == "__main__":
    unittest.main()