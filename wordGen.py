from random import randint, choice

vowels = ['a', 'e', 'o', 'u', 'i']
consonants = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
letters = [vowels, consonants]
def genSyllable():
    #includingDoubled = bool(randint(0, 1))

    syllableLength = randint(2, 3)
    syllable = ''

    if syllableLength == 1:
        syllable = choice(vowels)
    else:
        for i in range(0, syllableLength):
            syllable += choice(choice(letters))

    checkUp = []

    for i in syllable:
        if i in vowels:
            checkUp.append(True)
        else:
            checkUp.append(False)

    if not (True in checkUp):
        index = randint(0, len(syllable) - 1)
        syllable = syllable[:index] + choice(vowels) + syllable[index + 1:]
    if not (False in checkUp):
        index = randint(0, len(syllable) - 1)
        syllable = syllable[:index] + choice(consonants) + syllable[index + 1:]

    return syllable

def genWord(amount):
    syllableAmount = amount
    word = ''

    for i in range(0, syllableAmount):
        word += genSyllable()

    return word





    
