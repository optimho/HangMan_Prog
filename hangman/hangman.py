# Hangman game
# test change

# -----------------------------------
# Helper code+
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

import tkinter as tk
#global numberOfGuesses
#global lettersGuessed
#global Alphabet
global numberOfGuesses
global lettersGuessed
global Alphabet
#global lettersAvailable
#lettersGuessed = ()
#numberOfGuesses = 8
lettersGuessed = []
alphabet_list = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
    'x',
    'y', 'z')
alphabet = ('abcdefghijklmnopqrstuvwxyz')
lettersAvailable = list(alphabet)

WORDLIST_FILENAME = "words.txt"


class Keypres:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x200')
        self.root.bind('<KeyPress>', self.onKeyPress)

    def onKeyPress(self, event):
        self.key = event.char

    def __eq__(self, other):
        return self.key == other

    def __str__(self):
        return self.key


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

    guessedItems=0
    guessed_string = ''.join(lettersGuessed)
    for item in secretWord:
        if item in guessed_string:
            guessedItems=guessedItems+1

    if guessedItems==len(secretWord):
        return True
    else:
        return False


def NumberOfLetters(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: Number of letters remaining
    '''

    remainingletters = 0

    for letter in secretWord:
        if letter not in lettersGuessed:
            # print(letter)
            # print("No")
            remainingletters = remainingletters + 1

    return remainingletters


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    start = 0
    end = len(secretWord)
    lettersGuessedCorrectly = []

    for item in secretWord:
        if item in lettersGuessed:
            lettersGuessedCorrectly.append(item)

        else:
            lettersGuessedCorrectly.append('_')

    return ' '.join(lettersGuessedCorrectly)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    for letter in lettersGuessed:
        if letter in lettersAvailable:
            try:
                lettersAvailable.remove(letter)
            except ValueError:
                print("Invalid selection")

    return ''.join(lettersAvailable)


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

     Follows the other limitations detailed in the problem write-up. '''
    numberOfGuesses=8
    alphabet = ('abcdefghijklmnopqrstuvwxyz')
    lettersAvailable = list(alphabet)
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(NumberOfLetters(secretWord, lettersGuessed)))
    print("-------------")

    while numberOfGuesses > -1:

        print("You have {} guesses left.".format(numberOfGuesses))
        print("Available letters:{}{}".format(" ", ''.join(getAvailableLetters(lettersGuessed))))

        choice = input('Please guess a letter: ')    #enter a lower case letter

        if choice in lettersAvailable:                  #check that the letter is lower case alphabet
            pass                                     #Ok
        else:                                        #If not
            print("lower case letters only ")        #Warn user
            print('-----------')
            choice = ('')                            #clear user choice because it is not correct format

        if choice =='':                              #if choice is null bypass the nect two elif's
            pass

        elif choice not in lettersGuessed:  # your selection is not in letters already guessed
            lettersGuessed.append(choice)  # Then add it to the list of letters already guessed

        elif choice in lettersGuessed:  # your selection has already been used
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            choice = ''
            print('-----------')

        if choice =='':                              #if choice is null bypass next elifs
            pass

        elif choice not in secretWord:
            print('Oops! That letter is not in my word: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
            print('-----------')
            numberOfGuesses = numberOfGuesses - 1    # not correct selection loose one chance

        elif choice in secretWord:
            print('Good guess: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
            print('-----------')

            if isWordGuessed(secretWord, getGuessedWord(secretWord, lettersGuessed)):
                print("Congratulations, you won!")
                return 'Win'
        if numberOfGuesses == 0:
            print('Sorry, you ran out of guesses. The word was {}'.format(secretWord))
            return 'loose'

        # TODO make kepress work so that you do not have to press entre
        # print(keypress)s
        # if keypress.key == 'c':
        #  break
        # elif keypress.key == 'i':
        #   print(' iii ')
        # else:
        #   print("I dont understand %s" % keypress)
        # TODO make modification


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)


secretWord = chooseWord(wordlist).lower()
print(secretWord)
hangman(secretWord)
