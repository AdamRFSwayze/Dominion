class Card():
    def __init__(self, name, cardType, effect, cost, **kwargs):
        self.cardType = cardType 
        self.name = name
        self.effect = effect
        self.cost = cost
        if 'startingNumber' in kwargs:
            self.startingNumber = kwargs['startingNumber']
        elif 'Victory' in self.cardType:
            self.startingNumber = 8
        else:
            self.startingNumber = 10
        
    def __str__(self):
        return self.name
    
baseCardList = [
    'copper',
    'silver',
    'gold',
    'estate',
    'duchy',
    'province',
    'artisan', 
    'bandit', 
    'cellar', 
    'chapel',
    'council room', 
    'festival', 
    'garden'
]


def plusMoney(amount):
    BoardState.turnState.plusMoney(amount)
    return amount
    

def plusVictoryPoints(amount, player):
    BoardState.victoryPoints[player] += amount
    return amount

def plusCards(amount, startPosition, endPosition):
    BoardState.moveCard(startPosition, endPosition)
    return amount

def plusBuys(amount):
    BoardState.turnState.plusBuys(amount)
    retlist ofurn amount
    
    
    
    
#List of Cards

copper = Card(
    name = 'copper',
    cardType = 'Treasure',
    effect = [
        (plusMoney, 1)
    ],
    startingNumber = 70,
    cost = 0
)
      
silver = Card(
    name = 'silver',
    cardType = 'Treasure',
    effect = [
        (plusMoney, 2)
    ],
    startingNumber = 40,
    cost = 3
)

gold = Card(
    name = 'gold', 
    cardType = 'Treasure',
    effect = [
        (plusMoney, 3)
    ],
    startingNumber = 30,
    cost = 6
)

estate = Card(
    name = 'estate', 
    cardType = 'Victory', 
    effect = [],
    startingNumber = 8, 
    cost = 2
)


duchy = Card(
    name = 'duchy',
    cardType = 'Victory',
    effect = [],
    startingNumber = 8,
    cost = 5
)

province = Card(
    name = 'province', 
    cardType = 'Victory', 
    effect = [],
    startingNumber = 8,
    cost = 8
)

artisan = Card(
    name = 'artisan',
    cardType = ['Action'], 
    effect = [
        #Wat
        (moveCard, supply, hand)
        (moveCard, hand, topOfDEck)
    ],
    cost = 6
)


bandit = Card(
    name = 'bandit',
    cardType = ['Action', 'Attack'],
    effect = [
        (moveCard, 'goldFromSupply', discardPile), 
        (moveCard, 'goodTreasure', trash)
    ], 
    cost = 5
)


bureaucrat = Card(
    name = 'bureaucrat', 
    cardType = ['Action', 'Attack'],
    effect = [
        (moveCard, 'SilverFromSupply', 'topofDEck'),
        (moveCard, 'VictoryhandofOpponent', 'topofdeck')
    ],
    cost = 4
)


cellar = Card(
    name = 'cellar', 
    cardType = ['Action'], 
    effect = [
        (plusActions, 1)
        (moveCard, 'hand', 'discard'),
        (moveCard, 'deck', 'hand')
    ],
    cost = 2
)

chapel = Card(
    name = 'chapel', 
    cardType = ['Action'],
    effect = [
        (moveCard, 'hand', 'trash')
    ],
    cost = 2
)

council_room = Card(
    name = 'council room',
    cardType = ['Action'],
    effect = [
        (moveCard, 4fromdeck, hand), 
        (moveCard, fromOtherPLayerDeck, hand), 
        (plusBuys, 1)
    ],
    cost = 5
)

festival = Card(
    name = 'festival', 
    cardType = ['Action']
    effect = [
        (plusMoney, 2), 
        (plusActions, 2), 
        (plusBuys, 1)
    ],
    cost = 5
)


gardens = Card(
    name = 'gardens', 
    cardType = 'Victory',
    effect = [],
    startingNumber = 8, 
    cost = 4
)

harbinger = Card(
    name = 'harbinger', 
    cardType = ['Action'], 
    effect = [
        (moveCard, deck, hand),
        (moveCard, discard, deck)
    ], 
    cost = 3

)






    
    


    
  