# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    secretDict = makeSecretDict(secretWord)
    for letter in lettersGuessed:
        if letter in secretWord:
            secretDict[letter][0] = True
    for key in secretDict.keys():
        if secretDict[key][0] == False:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretDict = makeSecretDict(secretWord)
    secretList = list(secretWord)
    currentGuess = secretList
    for i in range(len(currentGuess)):
        currentGuess[i] = '_ '
    for letter in lettersGuessed:
        if letter in secretDict.keys():
            secretDict[letter][0] = True
            for position in secretDict[letter][1]:
                currentGuess[position] = letter
    printGuess = ''.join(currentGuess)
    return printGuess


import string

def makeSecretDict(secretWord):
    """
    :param secretWord: word to be guessed
    :return: A dictionary with the constituent letters and the index of where they appear in secretWord
    """
    secretDict = {}
    for i in secretWord:
        secretDict[i] = [False, []]
        for x in range(len(secretWord)):
            if secretWord[x] == i:
                secretDict[i][1].append(x)
    return secretDict

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = list(string.ascii_lowercase)
    for i in lettersGuessed:
        pos = alphabet.index(i)
        del alphabet[pos]
    remainingLetters = ''.join(alphabet)
    return remainingLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    def lineBreak():
        print('-------------')
    # secretWord = chooseWord(wordlist).lower()
    makeSecretDict(secretWord)
    guesses = 8
    lettersGuessed = []
    isWordGuessed(secretWord,lettersGuessed)
    repeatedLines = {
        'intro': "Welcome to the game, Hangman!\nI am thinking of a word that is %s letters long" % (len(secretWord)),
        'guessesLeft': "You have %s guesses left" % (guesses),
        'availableLetters': "Available Letters: %s" % (getAvailableLetters(lettersGuessed)),
        'askForLetter': "Please guess a letter: ",
        'right': "Good guess: ",
        'wrong': "Oops! That letter is not in my word: "
    }
    print(repeatedLines['intro'])
    while True:
        lineBreak()
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
            break
        elif guesses == 0:
            print('Sorry, you ran out of guesses. The word was %s' % (secretWord))
            break
        print("You have %s guesses left" % (guesses))
        print("Available Letters: %s" % (getAvailableLetters(lettersGuessed)))
        letter = input(repeatedLines['askForLetter'])
        letter = letter.lower()
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(letter)
            if letter in secretWord:
                print(repeatedLines['right'] + getGuessedWord(secretWord, lettersGuessed))
            else:
                print(repeatedLines['wrong'] + getGuessedWord(secretWord, lettersGuessed))
                guesses -= 1

hangman('apples')
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
