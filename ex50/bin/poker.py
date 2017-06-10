def highestCard(cards):
	sortedCards = sorted(cards, key=cardNumber)
	return sortedCards[4]
	
def twoOfAKind(cards):
	cardCount = [0]*15
	for card in cards:
		value = cardNumber(card)
		cardCount[value] = cardCount[value] + 1
	for i in range(15):
		if (cardCount[i] == 2):
			return i
		
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
