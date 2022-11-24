
#Black jack Class
"""Attributes of this Blackjack class are as follows.
       INSTANCE VARIABLES

        dealerHand: a list of PlayingCard objects representing the dealer's hand
        playerHand: a list of PlayingCard objects representing the player's hand
        playingDeck: a Deck object representing the deck of cards the game is being played with
        
       METHODS
       
        __init__(self, dHand=[], pHand=[])
            constructor that initializes instance variables
            it also gives the playingDeck an initial shuffle
        initDeal(self,gwin,xposD,yposD,xposP,yposP):
            deals out initial cards, 2 per player and 
            displays dealer and player hands on graphical win
            xposD and yposD give initial position for dealer cards
            xposP and yposP are analogous
        hit(self, gwin, xPos, yPos)
            adds a new card to the player's hand and places it at xPos, yPos
        evaluateHand(self, hand)
            totals the cards in the hand that is passed in and returns total
            (ace counts as 11 if doing so allows total to stay under 21)
        dealearPlays(self, gwin, xPos, yPos)
            dealer deals cards to herself, stopping when hitting "soft 17"
    """
from Deck import Deck
from ButtonClassBlackJack import *
from graphics import *
class BlackJack:
    
    def __init__(self, dHand=[], pHand=[]):

        self.DealerHand=dHand
        self.PlayerHand=pHand
        self.MyDeck=Deck()
        #self.MyDeck.shuffle()
        
        
    def initDeal(self,gwin,xposD,yposD,xposP,yposP):

        self.DealerHand.append(self.MyDeck.dealCard())
        self.DealerHand.append(self.MyDeck.dealCard())
        imD = Image(Point(xposD,yposD), "playingcards/" + self.DealerHand[0].getSuit() + str(self.DealerHand[0].getRank()) + ".gif")
        imD2 = Image(Point(xposD + 10,yposD), "playingcards/" + self.DealerHand[1].getSuit() + str(self.DealerHand[1].getRank()) + ".gif")
        imD.draw(gwin)
        imD2.draw(gwin)
        
        self.PlayerHand.append(self.MyDeck.dealCard())
        self.PlayerHand.append(self.MyDeck.dealCard())
        imP = Image(Point(xposP,yposP), "playingcards/" + self.PlayerHand[0].getSuit() + str(self.PlayerHand[0].getRank()) + ".gif")
        imP2 = Image(Point(xposP + 5 ,yposP), "playingcards/" + self.PlayerHand[1].getSuit() + str(self.PlayerHand[1].getRank()) + ".gif")
        imP.draw(gwin)
        imP2.draw(gwin)
        
    def hit(self, gwin, xPos, yPos):
        card = self.MyDeck.dealCard()
        self.PlayerHand.append(card)
        img = Image(Point(xPos,yPos), "playingcards/" + card.getSuit() + str(card.getRank()) + ".gif")
        img.draw(gwin)

    def evaluateHand(self, hand):
        total=0
        for card in hand:
            total=card.getRank() + total
            if card.getRank()==1 and total + 10  <= 21:
                total= total+ 10

        
            

def main():
    win = GraphWin("BlackJack",800,600)
    win.setCoords(0, 0, 100, 100)
    game=BlackJack()
    
    
    dHand=[]
    pHand=[]
    game.__init__(dHand, pHand)
    game.initDeal(win, 20, 80, 20, 20)
    
    HitButton= Button(win, Point(30,50), 15, 10, 'Hit')
    
    StandButton=Button(win, Point(60,50), 15, 10, 'Stand')

    QuitButton=Button(win, Point(90, 10), 10, 5, 'Quit')
    
    pt=win.getMouse()
    
    while not QuitButton.clicked(pt):
##        if HitButton.clicked(pt):
##            #game.hit
##        elif StandButton.clicked(pt):
                  
            
        pt=win.getMouse()
        
    win.close()
        
    
    
main()
