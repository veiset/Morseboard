# -*- coding: utf-8 -*-

'''
Implementation of the International Morse Code,
see: http://en.wikipedia.org/wiki/Morse_code 

Using a Binary Trie with morse code inserted,
this is done because Binary would not catch
prefixes. 
'''
morseMap     = [None] * 100
morseMap[7]  = 'A'
morseMap[41] = 'B'
morseMap[50] = 'C'
morseMap[14] = 'D'
morseMap[1]  = 'E'
morseMap[49] = 'F'
morseMap[35] = 'G'
morseMap[40] = 'H'
morseMap[4]  = 'I'
morseMap[79] = 'J'
morseMap[23] = 'K'
morseMap[43] = 'L'
morseMap[8]  = 'M'
morseMap[5]  = 'N'
morseMap[26] = 'O'
morseMap[52] = 'P'
morseMap[71] = 'Q'
morseMap[16] = 'R'
morseMap[13] = 'S'
morseMap[2]  = 'T'
morseMap[22] = 'U'
morseMap[67] = 'V'
morseMap[25] = 'W'
morseMap[68] = 'X'
morseMap[77] = 'Y'
morseMap[44] = 'Z'

def getCharFromMorse(bools): 
    """
    Takes a list of booleans as an input, representing
    a morse code, false for "dot" and true for "dash".

    Keyword arguments:
    bools   -- A list of boolean values representing morse

    Return represented characters.
    """
    DOT  = 1
    DASH = 2

    hash = 0
    for (i, b) in enumerate(bools):
        print i,b
        if b:
            hash += DASH * (3**i)
        else:
            hash += DOT  * (3**i)

    if hash >= len(morseMap):
        return None 

    return morseMap[hash]


def getMorseFromChar(c):
    '''
    Returns a morse representation of a character
    in form a list of True/False values. 
    True represent a dash, and False a dot.

    Keyword arguments:
    c    -- Character

    Return morse representation of a character
    '''
    c = c.upper()

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

def getHashFromChar(c):
    DOT  = 1
    DASH = 2
    END  = 3

    bools = getMorseFromChar(c)
    states = []

    for b in bools:
        if b:
            states.append(DASH)
        else:
            states.append(DOT)
    states.append(END)

    states = states[::-1]

    hash = 0
    for (i, state) in enumerate(states):
        if state == DOT:
            hash += DOT * (4**i)
        if state == DASH:
            hash += DASH * (4**i)
        if state == END:
            hash += END * (4**i)

    return hash

getCharFromMorse([False,True])
print getHashFromChar('B')

