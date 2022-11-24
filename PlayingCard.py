#Playing Card class
#Proj 5


class PlayingCard:

    def __init__(self, rank, suit):

        self.rank=rank
        self.suit=suit


    def __str__(self):

        ranks=['1','2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
        suits=['c', 's', 'd', 'h']

        if self.suit=='c':
            cardname='c' + ranks[self.rank-1]

        if self.suit=='s':
            cardname='s' + ranks[self.rank-1]
        
        if self.suit=='d':
            cardname='d' + ranks[self.rank-1]

        if self.suit=='h':
            cardname='h' + ranks[self.rank-1]

        
        return cardname

    def getSuit(self):
        
        return self.suit
    
    def getRank(self):
        
        return self.rank
    

