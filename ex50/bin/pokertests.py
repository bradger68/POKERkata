from assertions import printErrors, assertEqual
from poker import cardNumber, cardSuit, highestCard, twoOfAKind, threeOfAKind, fourOfAKind, twoPair, straight, flush, straightFlush, fullHouse, winner
# Red -> Green -> Refactor
assertEqual(2, cardNumber("2H"))
assertEqual(3, cardNumber("3H"))
assertEqual(10, cardNumber("10H"))
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
assertEqual("AH", highestCard(["10H", "3S", "AH", "5H", "6H"]))


assertEqual(3, twoOfAKind(["3H", "3S", "AH", "5H", "6H"]))
assertEqual(14, twoOfAKind(["3H", "AS", "AH", "5H", "6H"]))
assertEqual(None, twoOfAKind(["3H", "7S", "AH", "5H", "6H"]))

assertEqual(3, threeOfAKind(["3H", "3S", "3H", "5H", "6H"]))

assertEqual(3, fourOfAKind(["3H", "3S", "3H", "3H", "6H"]))

assertEqual((3,4), twoPair(["3H", "3S", "4H", "4S", "6H"]))
assertEqual((4,6), twoPair(["6H", "6S", "4H", "4S", "AH"]))
assertEqual(None, twoPair(["5H", "6S", "4H", "4S", "AH"]))
assertEqual(None, twoPair(["5H", "6S", "7H", "4S", "AH"]))


assertEqual(6, straight(["5H", "3S", "2H", "6H", "4H"]))
assertEqual(None, straight(["5H", "3S", "8H", "QH", "JH"]))


assertEqual(10, flush(["7H", "2H", "3H", "8H", "10H"]))
assertEqual(10, flush(["7H", "2H", "10H", "3H", "8H"]))
assertEqual(None, flush(["7S", "2H", "10H", "3H", "8H"]))

assertEqual(8 ,straightFlush(["6H", "7H", "8H", "4H", "5H"]))
assertEqual(None, straightFlush(["6H", "7H", "8H", "3H", "5H"]))

assertEqual(3, fullHouse(["3S", "3D", "3H", "2S", "2C"]))
assertEqual(None, fullHouse(["3S", "3D", "JH", "2S", "2C"]))
assertEqual(None, fullHouse(["3S", "3D", "3H", "KS", "2C"])) 
assertEqual(None, fullHouse(["3S", "3D", "3H", "3S", "2C"]))

#Black has a full house, white has a two pair
assertEqual(Black, winner(["3S", "3D", "3H", "3S", "2C"], ["3H", "3S", "AH", "5H", "6H"]))

printErrors()