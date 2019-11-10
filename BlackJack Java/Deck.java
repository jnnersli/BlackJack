package BlackjackModel;

/*Simple deck of cards with basic functions draw and shuffle*/

import java.util.*;

public class Deck {
    private Card[] cards;
    private int deckSize;
    
    /*
    Constructs a deck and initializes the card names + values
    */
    public Deck() {
        deckSize = 52;
        cards = new Card[deckSize];
        
        //Loop through four suits
        for(int i = 0, j = 0; i < 4; i++) {
            //Loop through all Card enum values
            for(Card c : Card.values()) {
                cards[j] = c;
                j++;
            }
        }
    }
    
    public int size() {return deckSize;}
    
    /*
    Draw last card (makes shuffling easier)
    */
    public Card draw() {
        if(deckSize > 0) {
            deckSize--;
            return cards[deckSize-1];
        }
        
        return null;
    }
    
    /*
    This is using the Fisher-Yates algorithm (modern)
    https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle#The_modern_algorithm
    */
    public void shuffle() {
        Random rand = new Random();
        for(int i = deckSize-1, j; i > 0; i--) {
            j = rand.nextInt(i);
            swap(i, j);
        }
    }
    
    private void swap(int i, int j) {
        Card temp = cards[i];
        cards[i] = cards[j];
        cards[j] = temp;
    }
}