#Deck Class
#Proj 5

from random import*
from PlayingCard import PlayingCard

class Deck:
    
    def __init__(self):
        
        self.cardList =[]
        
        for s in ["d", "c", "h", "s"]: 
            for r in range(1,14):
                self.cardList.append(PlayingCard(r, s))
    
        
        
    def shuffle(self):

        return random.shuffle(self.cardList)
                
    def dealCard(self):
        
        return self.cardList.pop()

    def cardsLeft(self):

        return self.cardList


def main():
    deck = Deck()

    n=5
    
    
    for i in range(n):
        print(deck.dealCard())
    #initial=self.cardList.pop(randrange(1,53))
    #print(initial)

main()

##if __name__ == "__main__":
##    main()
