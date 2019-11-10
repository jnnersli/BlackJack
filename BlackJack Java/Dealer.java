package BlackjackController;

/*Simple console-based two-player blackjack game*/
/*User plays against the dealer*/

import BlackjackModel.*;
import BlackjackView.BlackjackView;
import java.util.Scanner;
import java.io.PrintWriter;

public class Dealer {
    private static void playerWon(Player player, Player dealer) {
        player.setGameState(BlackjackState.WON);
        dealer.setGameState(BlackjackState.LOST);
    }
    
    private static void playerLost(Player player, Player dealer) {
        player.setGameState(BlackjackState.LOST);
        dealer.setGameState(BlackjackState.WON);
    }
    
    private static void tie(Player player, Player dealer) {
        player.setGameState(BlackjackState.WON);
        dealer.setGameState(BlackjackState.WON);
    }
    
    public static void main(String[] args) {
        //Initialize model
        Player player = new Player();
        Player dealer = new Player();
        Deck deck = new Deck();

        //Initialize input
        Scanner input = new Scanner(System.in);
        String nextMove = "";

        //Initialize view
        PrintWriter output = new PrintWriter(System.out);
        BlackjackView view = new BlackjackView(output);

        view.welcomeMessage();
        deck.shuffle();

        /*..........Playing.............*/

        //Both the player and the dealer are given 2 cards.
        for(int i = 0; i < 2; i++) {
            player.hit(deck.draw());
            dealer.hit(deck.draw());
        }

        //The player can see both of their cards but only one of the dealers cards.
        view.printCardDealer(dealer.hand().get(0));

        for(Card c : player.hand())
            view.printCard(c);

        //Player goes first
        dealer.setGameState(BlackjackState.WAITING);

        //The player now has two options: (1) ”hit”, or (2) ”stand”.
        view.prompt();
        nextMove = input.next();

        //The player can hit as many times as they wish until they stand.
        Card c;
        while(nextMove.equals("hit")) {
            c = deck.draw();
            view.printCard(c);
            player.hit(c);
            
            // If at any point their hand goes over 21, they automatically lose.
            if(player.countHand() > 21) {
                playerLost(player, dealer);
                view.printLoss();
                break;
            }
            
            nextMove = input.next();
        }

        if(nextMove.equals("stand")) {
            //Switch turns
            player.setGameState(BlackjackState.WAITING);
            dealer.setGameState(BlackjackState.PLAYING);
            
            //If the value of the dealers hand is 17 or more they automatically stand otherwise they automatically keep taking more cards until it is at least 17.
            while(dealer.countHand() < 17)
                dealer.hit(deck.draw());

            //If the dealers hand goes over 21 the player wins.
            if(dealer.countHand() > 21) {
                playerWon(player, dealer);
                view.printWin();
            }

            else {
                if(player.countHand() > dealer.countHand()) {
                    for(Card c1 : dealer.hand())
                        view.printCardDealer(c1);
                    
                    playerWon(player, dealer);
                    view.printWin();
                }
                
                else if(player.countHand() < dealer.countHand()) {
                    for(Card c1 : dealer.hand())
                        view.printCardDealer(c1);
                    
                    playerLost(player, dealer);
                    view.printLoss();
                }
                
                else {
                    for(Card c1 : dealer.hand())
                        view.printCardDealer(c1);
                    
                    tie(player, dealer);
                    view.printTie();
                }
            }
        }
    }
}