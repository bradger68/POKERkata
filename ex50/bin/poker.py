import math 

def highestCard(cards):
	sortedCards = sorted(cards, key=cardNumber)
	return sortedCards[4]
	
def straight(cards):
	sortedCards = sorted(cards, key=cardNumber)
	expectedNextCard = cardNumber(sortedCards[0])+1
	for card in sortedCards:
		if expectedNextCard == cardNumber(card) + 1:
		    expectedNextCard = expectedNextCard + 1
		else:
			return None
	theHighestCard = highestCard(cards)
	return cardNumber(theHighestCard)

def twoPair(cards):
	firstAsk = anyOfAKind(cards, 2, False) 
	if (firstAsk != None):
		secondAsk = anyOfAKind(cards, 2, True) 
		if (secondAsk != None and secondAsk != firstAsk):
			return (firstAsk, secondAsk)
	return None
		
def anyOfAKind(cards, desiredSize, reverse):
	cardCount = [0]*15
	for card in cards:
		value = cardNumber(card)
		cardCount[value] = cardCount[value] + 1
	for i in range(15):
		if (reverse):
			i = abs(i-14)
		if (cardCount[i] == desiredSize):
			return i
			
def twoOfAKind(cards):
	return anyOfAKind(cards, 2, False)
			
def threeOfAKind(cards):
	return anyOfAKind(cards, 3, False)
			
def fourOfAKind(cards):
	return anyOfAKind(cards, 4, False)
		
def cardNumber(card): 
	firstCharacter = card[0]
	if(firstCharacter == "T"):
		return 10
	elif (firstCharacter == "J"):
		return 11
	elif (firstCharacter == "Q"):
		return 12
	elif (firstCharacter == "K"):
		return 13
	elif (firstCharacter == "A"):
		return 14
	return int(firstCharacter)


def cardSuit(card):
	return card[1]
	
