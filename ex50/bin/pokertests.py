from assertions import printErrors, assertEqual
from poker import cardNumber, cardSuit, highestCard, twoOfAKind, threeOfAKind, fourOfAKind, twoPair
# Red -> Green -> Refactor
assertEqual(2, cardNumber("2H"))
assertEqual(3, cardNumber("3H"))
assertEqual(10, cardNumber("TH"))
assertEqual(12, cardNumber("QD"))
assertEqual(11, cardNumber("JD"))
assertEqual(13, cardNumber("KS"))
assertEqual(14, cardNumber("AS"))

assertEqual("S", cardSuit("2S"))
assertEqual("H", cardSuit("2H"))
assertEqual("D", cardSuit("3D"))
assertEqual("C", cardSuit("3C"))

#print "The highest value is 'highestcard'"
assertEqual("6H", highestCard(["3H", "6H", "4H", "5H", "2H"]))
assertEqual("7H", highestCard(["7H", "3S", "4H", "5H", "6H"]))
assertEqual("AH", highestCard(["TH", "3S", "AH", "5H", "6H"]))


assertEqual(3, twoOfAKind(["3H", "3S", "AH", "5H", "6H"]))
assertEqual(14, twoOfAKind(["3H", "AS", "AH", "5H", "6H"]))
assertEqual(None, twoOfAKind(["3H", "7S", "AH", "5H", "6H"]))

assertEqual(3, threeOfAKind(["3H", "3S", "3H", "5H", "6H"]))

assertEqual(3, fourOfAKind(["3H", "3S", "3H", "3H", "6H"]))

assertEqual((3,4), twoPair(["3H", "3S", "4H", "4S", "6H"]))
assertEqual((4,6), twoPair(["6H", "6S", "4H", "4S", "AH"]))
assertEqual(None, twoPair(["5H", "6S", "4H", "4S", "AH"]))
# assertEqual(None, twoPair(["5H", "6S", "7H", "4S", "AH"]))

printErrors()