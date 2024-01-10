# hangman
# we need a selection of words from which the computer will choose randomly
# the user must guess a letter, if the letter is in the word, all instances of that word will be filled
#and the unguessed letters will be displayed as dashes
import random
import string
from words import words # ensure that words.py is in the same file path as the the current file
# words.py has some weird words with dashes and spaces in them. we don't want these to be chosen
# this function solves that problem
def get_valid_word():
    word = random.choice(words)
    while '-' in words or ' ' in words:
        word = random.choice(words)
    return word.upper()

# Now for the game itself
# Logic behind the game:
# computer chooses a random word
# user guesses a letter, so we need user input
# we want to check if they have already guessed this character before, or if its an invalid character
# we will store the used letters into a set
# we want the user to guess until there are no more letters to guess
# we want to show the user the letters they have guessed so far
# we want to show them the progress of the word so far
# display dashes if it hasn't been guessed, ie not in word_letters and used_letters
def hangman():
    word = get_valid_word()
    word_letters = set(word) # set of the letters in the word, (no dupication in sets)
    alphabet = set(string.ascii_uppercase) # this defines the set of valid characters for guesses
    used_letters = set() # declaring an empty set
    lives = 10 # gives the user 10 attempts to guess the word
    while len(word_letters) > 0 and (lives > 0) :
        print("You have guessed these letters: ", " ".join(used_letters)) # try with "," as well
        current_word = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: "," ".join(current_word))
        guess = input("Guess a character: ").upper()
        # if the guess is in the word
        if guess in (alphabet - used_letters):
            used_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
            else:
                lives -= 1
                print(f"{guess} is not in the word, you have {lives} lives remaining!")
        # if the guessed letter has already been used
        elif guess in used_letters:
            print("You have already used this character, try another one!\n")
        else:
            print("Invalid character, try another one!\n")
    if lives == 0:
        print("You have died, better luck next time!")
    else:
        print(f"Congratulations, you have guessed the word. The word is: {word}")
hangman()
