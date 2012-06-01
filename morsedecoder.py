from morseparser import *

class MorseDecoder:
  encoding = 1000*[None]
  """
  In the encoding None represents that there are no more children in this tree,
  0 means that there is no character at this node, and anything else is a character.
  """
  def __init__(self):
      for code in range(65,90):
          self.encoding[getHashFromChar(chr(code))] = chr(code)

      self.encoding[0] = 0
      for code in range(65,90):
           bools = getBoolsFromChar(chr(code))
           morse = getMorseFromBools(bools)
           for i in range(len(bools)):
               theHash = getHashFromMorse(morse[:i+1])
               if self.encoding[theHash] == None:
                   self.encoding[theHash] = 0
 
  def guessWord(self,probString,pointer = 0,i=0):
      """
        
        [[(Symbol,probability)]] -> [(String,probability)]
  
      """
      print pointer
      print probString
      if len(probString) == 0 and self.encoding[pointer] == 0:
          return [("",0)]
      elif len(probString) == 0 and self.encoding[pointer] != 0:
          return [(self.encoding[pointer],1)]
  
      if self.encoding[pointer] == None:
          print pointer
          return [("",0)]
  
      alternatives = []
  
      print "lookie",self.encoding[pointer]
      if self.encoding[pointer] != 0:
          for (stopHereRest,stopHereProb) in self.guessWord(probString[1:],0):
              print stopHereRest
              alternatives.append((self.encoding[pointer] + stopHereRest,stopHereProb))
  
  
      for (symbol,charProb) in probString[0]:
          for word in self.guessWord(probString[1:],pointer + (symbol*(hashSize**i)),i+1):
              alternatives.append(word);
  
      return alternatives
