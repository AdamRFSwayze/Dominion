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
               
        #dictionary of card names keyed on card ID
        self.cardsInUse = {}
        
        #dictionary of card PositionIDs keyed on cardID
        self.cardPositions = {}
        
        #initiating 
        self.decks = {player : []  for player in self.players}
        
        for player in self.players:
            for card in self.startingCards:
                self.decks[player] += [self.generateCardId(card)]
        
        self.discardPiles = {player : [] for player in players}
        self.hands = {player : random.sample(self.decks[player], 5) for player in players}
        
        
        for player in self.players:
            for card in self.hands[player]:
                self.decks[player].remove(card)
        
        #for all cards that could be in the game, for all card IDs, whatever:
            #cardPositions[card] = 
        
    def moveCard(self, startPosition, endPosition):
        #Reassigns position IDs.
        #If the destination is deck, shift.
        #If the starting location is deck, unshift.
        
        thisCard = [card for card, position in cardPositions.items() if position == startPosition][0]
        
        for card in [
            card for card, position in self.cardPositions.items() \
            if position[1] == startPosition[1] and position[2] > startPosition[2]]:
                self.cardPositions[card] = (position[0], position[1], position[2] - 1)
        
        for card in [
            card for card, position in self.cardPositions.items() \
            if position[1] == endPosition[1] and position[2] >= endPosition[2]]:
                self.cardPositions[card] = (position[0], position[1], position[2] + 1)
        
        self.cardPositions[thisCard] = endPosition
    
        
    def generateCardId(self, cardName):
        cardID = uuid4()
        self.cardsInUse[cardID] = cardName
        return cardID
    
    def generatePositionID(self, cardID, player, pile, position):
        positionID = uuid()
        self.cardPositions[cardID] = (player, pile, position)
        return positionID
    
    
    


    

