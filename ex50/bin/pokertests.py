from assertions import printErrors, assertEqual
from poker import cardNumber, cardSuit, highestCard, twoOfAKind
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

printErrors()