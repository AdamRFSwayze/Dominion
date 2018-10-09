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


def createCardDictionary(cardList):
    cardDictionary = {}
    temp = 100
    for card in cardList:
        cardDictionary[card] = temp
        temp += 1
    return cardDictionary


def generateCardId(cardName):
    if cardName in cardsInUse.values():
        cardsInUse[str(int(max(cardsInUse.keys())) + 1)] = cardName
    else: 
        cardsInUse[str(cardDictionary[cardName]) + '01'] = cardName 
        

def plusMoney(value):
    BoardState.turnState.plusMoney(value)
    
    
    
    
#List of Cards

duchy = Card(
    name = 'duchy',
    cardType = 'Victory',
    effect = None,
    startingNumber = 8,
    cost = 5
)


copper = Card(
    name = 'copper',
    cardType = 'Treasure',
    effect = [
        (plusMoney, 1)
    ],
    startingNumber = 70,
    cost = 0
)
        