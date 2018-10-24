import random


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
        
        self.cardDictionary = {}
        temp = 100
        for card in self.cardList:
            self.cardDictionary[card] = temp
            temp += 1
        
        for player in self.players:
            for card in self.startingCards:
                self.decks[player] += [self.generateCardId(card)]
        
        self.discardPiles = {player : [] for player in players}
        self.hands = {player : random.sample(self.decks[player], 5) for player in players}
        
        for player in self.players:
            for card in self.hands[player]:
                self.decks[player].remove(card)
        
    def moveCard(self, cardID, player, cardLocation, cardDestination):
        if cardLocation == 'decks':
            if cardDestination == 'trash':
                self.decks[player].remove(cardID)
                self.trash += [cardID]
        
    
        
         
 
    
    def generateCardId(self, cardName):
        if cardName in self.cardsInUse.values():
            cardID = str(int(max(self.cardsInUse.keys())) + 1)
            self.cardsInUse[cardID] = cardName
        else: 
            cardID = str(self.cardDictionary[cardName]) + '01'
            self.cardsInUse[cardID] = cardName 
        return cardID
    
    

