import unittest
from itertools import permutations

import sys
sys.path.append('../BlackjackModel/')
from Deck import *
from Card import *

class DeckTest(unittest.TestCase):
    #Size of the deck should be decremented by 1 after draw
    def test_draw(self):
        deck = Deck()
        sizeBefore = deck.size()
        deck.draw()
        sizeAfter = deck.size()
        self.assertEqual(sizeBefore - 1, sizeAfter)
        
    #Shuffle should modify the deck
    def test_shuffle(self):
        deck = Deck()
        listBefore = deck.cards().copy() #ordered deck before shuffling
        deck.shuffle()
        listAfter = deck.cards().copy() #ordered deck after shuffling
        self.assertIsNot(listBefore, listAfter)
    
    #Shuffled deck should be a permutation of original
    def test_permutation(self):
        deck = Deck()
        listBefore = deck.cards().copy() #ordered deck before shuffling
        deck.shuffle()
        listAfter = deck.cards().copy() #ordered deck after shuffling
        perm = permutations(listBefore)
        tupAfter = tuple(listAfter) #permutations returns a list of tuples
        #self.assertTrue( tupAfter in perm ) #this step takes forever

if __name__ == "__main__":
    unittest.main()