import random
from uuid import uuid4


class BoardState():
    def __init__(self, players, startingCards, supply, trash, turnState, cardList):
        self.players = players
        self.startingCards = startingCards
        #self.hands = hands
        #self.decks = decks
        #tuples such as (CARDS, # in supply)
        self.supply = supply
        self.trash = trash
        self.turnState = turnState
        #self.cardsInUse = cardsInUse
        self.cardList = cardList
               
       
        self.cardsInUse = {}
       

        
        self.decks = {player : []  for player in self.players}
        
        
        for player in self.players:
            for card in self.startingCards:
                self.decks[player] += [self.generateCardId(card)]
        
        self.discardPiles = {player : [] for player in players}
        self.hands = {player : random.sample(self.decks[player], 5) for player in players}
        
        for player in self.players:
            for card in self.hands[player]:
                self.decks[player].remove(card)
        
    def moveCard(self, cardID, player, cardLocation, cardDestination):
        pass
        
    
        
    def generateCardId(self, cardName):
        cardID = uuid4()
        self.cardsInUse[cardID] = cardName
        return cardID
    
    

