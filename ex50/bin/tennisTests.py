from assertions import printErrors, assertEqual
from tennis import *


assertEqual("love-love", tennis(0,0))
assertEqual("love-fifteen",tennis(0,1))
assertEqual("fifteen-love",tennis(1,0))
assertEqual("love-thirty", tennis(0,2))
assertEqual("thirty-love", tennis(2,0))
assertEqual("love-forty", tennis(0,3))
assertEqual("forty-love", tennis(3,0))
assertEqual("forty-thirty", tennis(3,2))
assertEqual("thirty-forty", tennis(2,3))
assertEqual("forty-fifteen", tennis(3,1))
assertEqual("fifteen-forty", tennis(1,3))
assertEqual("thirty-fifteen", tennis(2,1))
assertEqual("fifteen-thirty", tennis(1,2))
assertEqual("thirty-thirty", tennis(2,2))
assertEqual("forty-forty", tennis(3,3))
# winning
assertEqual("player 2 wins", tennis(2,4))
assertEqual("player 1 wins", tennis(4,2))
assertEqual("player 1 wins", tennis(5,3))
assertEqual("player 2 wins", tennis(3,5))

# duece
assertEqual("deuce", tennis(4,4))
assertEqual("deuce", tennis(5,5))
assertEqual("deuce", tennis(6,6))

# advantage
assertEqual("advantage player 1", tennis(4,3))
assertEqual("advantage player 1", tennis(5,4))
assertEqual("advantage player 1", tennis(6,5))

assertEqual("advantage player 2", tennis(3,4))
assertEqual("advantage player 2", tennis(4,5))
assertEqual("advantage player 2", tennis(5,6))
printErrors()