import math 

def highestCard(cards):
	sortedCards = sorted(cards, key=cardNumber)
	return sortedCards[4]
	
def twoPair(cards):
	count = 0
	firstAsk = anyOfAKind(cards, 2, False) 
	if (firstAsk > 0):
		count = count + 1
		secondAsk = anyOfAKind(cards, 2, True) 
		if (secondAsk > 1):
			count = count + 1
	return (firstAsk, secondAsk)
	
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
	
