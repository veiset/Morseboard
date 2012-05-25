# -*- coding: utf-8 -*-
morseMap = [None] * 100
morseMap[7] = 'A'
morseMap[41] = 'B'
morseMap[50] = 'C'
morseMap[14] = 'D'
morseMap[1] = 'E'
morseMap[49] = 'F'
morseMap[35] = 'G'
morseMap[40] = 'H'
morseMap[4] = 'I'
morseMap[79] = 'J'
morseMap[23] = 'K'
morseMap[43] = 'L'
morseMap[8] = 'M'
morseMap[5] = 'N'
morseMap[26] = 'O'
morseMap[52] = 'P'
morseMap[71] = 'Q'
morseMap[16] = 'R'
morseMap[13] = 'S'
morseMap[2] = 'T'
morseMap[22] = 'U'
morseMap[67] = 'V'
morseMap[25] = 'W'
morseMap[68] = 'X'
morseMap[77] = 'Y'
morseMap[44] = 'Z'

def getCharFromMorse(x): 
  """
  Takes a list of booleans as an input, representing
  a morsecode, false for "dot" and true for "dash".
  returns the character it represents.
  """
  hash = 0

  for i in range(len(x)):
    if x[i]:
      hash += 2 * (3**i)
    else:
      hash += 1 * (3**i)
     
  return morseMap[hash]

def getMorseFromChar(c):
  return {
      'A' : [False,True],
      'B' : [True,False,False,False],
      'C' : [True,False,True,False],
      'D' : [True,False,False],
      'E' : [False],
      'F' : [False,False,True,False],
      'G' : [True,True,False],
      'H' : [False,False,False,False],
      'I' : [False,False],
      'J' : [False,True,True,True],
      'K' : [True,False,True],
      'L' : [False,True,False,False],
      'M' : [True,True],
      'N' : [True,False],
      'O' : [True,True,True],
      'P' : [False,True,True,False],
      'Q' : [True,True,False,True],
      'R' : [False,True,False],
      'S' : [False,False,False],
      'T' : [True],
      'U' : [False,False,True],
      'V' : [False,False,False,True],
      'W' : [False,True,True],
      'X' : [True,False,False,True],
      'Y' : [True,False,True,True],
      'Z' : [True,True,False,False]}[c]
