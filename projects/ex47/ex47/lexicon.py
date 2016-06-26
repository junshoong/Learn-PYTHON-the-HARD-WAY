# -*- coding: utf-8 -*-

DIRECTION = ['east', 'west', 'south', 'north']
VERB = ['go', 'kill', 'eat', 'attack']
STOP = ['the', 'in', 'of']
NOUN = ['bear', 'princess']

def scan(stuff):
    words = stuff.split()
    result = []

    for word in words:
        low_word = word.lower()
        try:
            tup = ('number', int(word))

        except ValueError:
            if low_word in DIRECTION:
                tup = ('direction', word)
            elif low_word in VERB:
                tup = ('verb', word)
            elif low_word in STOP:
                tup = ('stop', word)
            elif low_word in NOUN:
                tup = ('noun', word)
            else:
                tup = ('error', word)

        result.append(tup)
    return result
