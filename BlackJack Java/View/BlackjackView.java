package BlackjackView;

import BlackjackModel.*;
import java.io.PrintWriter;

public class BlackjackView {
    private PrintWriter output;
    
    public BlackjackView(PrintWriter pw) { output = pw; }
    
    public void welcomeMessage() {
        output.println("Welcome to Jenny's Blackjack Casino >:)");
        output.println("The dealer will now deal out two cards.\n");
        output.flush();
    }
    
    public void prompt() {
        output.println("Would you like to \"hit\" or \"stand\"?");
        output.flush();
    }
    
    public void printCard(Card c) {
        output.println(c);
        output.flush();
    }
    
    public void printCardDealer(Card c) {
        output.println("The dealer has: " + c);
        output.flush();
    }
    
    public void printWin() {
        output.println("You won!");
        output.flush();
    }
    
    public void printLoss() {
        output.println("You lost :(");
        output.flush();
    }
    
    public void printTie() {
        output.println("You have tied with the dealer.");
        output.flush();
    }
}