    
def tennis(score1, score2):
    if score1 >= 4 or score2 >= 4: 
        if score1 == score2:
            return "deuce"
        elif score1 > score2:
            return checkingScore(score1, score2, "player 1")
        else:
            return checkingScore(score2, score1, "player 2")
    else:
        return score(score1) + "-" + score(score2)


def checkingScore(bigger, smaller, biggerName):
    if bigger - smaller >= 2:
        return biggerName + " wins"
    elif bigger - smaller == 1:
        return "advantage " + biggerName


def score(score):
    if score == 0:
        return "love"
    elif score == 1:
        return "fifteen"
    elif score == 2:
        return "thirty"
    elif score == 3:
        return "forty"
