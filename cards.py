class Card():
    def __init__(self, name, cardType, effect, startingNumber, cost):
        self.cardType = cardType 
        self.name = name
        self.effect = effect
        startingNumber = startingNumber 
        self.cost = cost
    
    def __str__(self):
        return self.name
    
    
cardList = [
    'copper',
    'silver',
    'gold',
    'estate',
    'duchy',
    'province'
]


def plusMoney(value):
    BoardState.turnState.plusMoney(value)
    
    
    
    
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
  