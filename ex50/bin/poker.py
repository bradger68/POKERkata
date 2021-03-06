import math 

# Domain Logic 

def highestCard(cards):
	sortedCards = sorted(cards, key=cardNumber)
	return sortedCards[4]

def twoPair(cards):
	firstAsk = anyOfAKind(cards, 2, False) 
	if (firstAsk != None):
		secondAsk = anyOfAKind(cards, 2, True) 
		if (secondAsk != None and secondAsk != firstAsk):
			return (firstAsk, secondAsk)

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


def flush(cards): 
	sortBySuit = sorted(cards, key=cardSuit)
	initialCardSuit = cardSuit(sortBySuit[0])
	finalCardSuit = cardSuit(sortBySuit[4])
	if initialCardSuit == finalCardSuit:
		return cardNumber(highestCard(cards))
	
	
def straightFlush(cards):
	if flush(cards):
		return straight(cards)
	

def fullHouse(cards):
	if twoOfAKind(cards):
		return threeOfAKind(cards)
	

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

# Anti-corruption layer (Abstractions)

def cardNumber(card): 
	firstCharacter = card[0]
	if(firstCharacter == "1"):
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
	if card[0] == "1":
		return card[2]
	return card[1]
	

	
# Now we gotta rank these bad boyz 

# Name, rank, highest card
def identify(cards):
	if straightFlush(cards):
		rank = 1
		return ("Straight Flush", rank, straightFlush(cards))
	elif fourOfAKind(cards):
		rank = 2
		return ("Four Of A Kind", rank, fourOfAKind(cards))
	elif fullHouse(cards):
		rank = 3
		return ("Full House", rank, fullHouse(cards))
	elif flush(cards):
		rank = 4
		return ("Flush", rank, flush(cards))
	elif straight(cards):
		rank = 5
		return ("Straight", rank, straight(cards))
	elif threeOfAKind(cards):
		rank = 6
		return ("Three Of A Kind", rank, threeOfAKind(cards))
	elif twoPair(cards):
		rank = 7
		return ("Two Pair", rank, twoPair(cards))
	elif twoOfAKind(cards):
		rank = 8
		return("Two Of A Kind", rank, twoOfAKind(cards))
	elif highestCard(cards):
		rank = 9
		return ("Highest Card", rank, highestCard(cards))


def winner(blackEntry, whiteEntry):
	blackHand = identify(blackEntry)
	whiteHand = identify(whiteEntry)
	if blackHand[1] < whiteHand[1]:
		return "Black"
	elif blackHand[1] > whiteHand[1]:
		return "White"
	elif blackHand[1] == whiteHand[1]:
		if blackHand[2] > whiteHand[2]:
			return "Black"
		elif blackHand[2] < whiteHand[2]:
			return "White"
		else:
			return "Tie"