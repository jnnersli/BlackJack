package BlackjackModel;

/*One of the blackjack players*/

import java.util.*;

public class Player {
    private List<Card> hand;
    private BlackjackState gameState; //To determine when their turn is
    private int score; //Total number of games won. This isn't necessarily needed, but might as well include it.
    
    public Player() {
        hand = new LinkedList<Card>();
        gameState = BlackjackState.PLAYING;
        score = 0;
    }
    
    //Getters
    public List<Card> hand() { return hand; }
    public BlackjackState gameState() { return gameState; }
    public int totalScore() { return score; }
    
    public void setGameState(BlackjackState state) {
        if(state.equals(BlackjackState.WON))
            score++;
        
        gameState = state;
    }
    
    public void hit(Card c) {
        if(gameState.equals(BlackjackState.PLAYING))
            hand.add(c);
    }
    
    public int countHand() {
        int total = 0;
        int aceCount = 0;
        
        for(Card c : hand) {
            switch(c) {
                //Keep a count of the number of aces in the hand
                case ACE: {
                    total += 11; 
                    aceCount++; 
                    break;
                }
                case TWO: total += 2; break;
                case THREE: total += 3; break;
                case FOUR: total += 4; break;
                case FIVE: total += 5; break;
                case SIX: total += 6; break;
                case SEVEN: total += 7; break;
                case EIGHT: total += 8; break;
                case NINE: total += 9; break;
                default: total += 10;
            }
        }
        
        //Count aces as 1, not 11 as needed.
        while(aceCount > 0 && total > 21) {
            total -= 10;
            aceCount--;
        }
        
        return total;
    }
}