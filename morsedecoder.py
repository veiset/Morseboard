from morseparser import *

encoding = 100*[None]
 """
 In the encoding None represents that there are no more children in this tree,
 0 means that there is no character at this node, and anything else is a character.
 """

def guessWord(probString,pointer = 0):
  """
    
    [[(Symbol,probability)]] -> [(String,probability)]

  """
    if len(probString) == 0:
        return [("",1)]

    if encoding[pointer] == None:
        return [("",0)]

    alternatives = []

    if encoding[pointer] != 0:
        for (stopHereRest,stopHereProb) in guessWord(probString[1:],0):
            alternatives.append((encoding[pointer] + stopHereRest,stopHereProb))


    for (symbol,charProb) in probString[0]:
        for word in guessWord(probString[1:],pointer * hashSize + symbol):
            alternatives.append(awsm);

    return alternatives
