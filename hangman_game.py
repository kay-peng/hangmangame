#create a hangman game
#get the user to select how many incorrect guesses they want (between 6 and 12)
#get ther user to choose how long the word is (between 4 and 10)
#search through english_words.csv to randomly select a word that is x letters long (as decided by the player)
#get the player to start guessing letters. if the letter is in the word, show it in place
#if not, countdown the number of guesses
#if the player guesses the word, congratulate them

import random

def replace_letters(letter):
    letter_indexes = list(index for index, val in enumerate(hangman_word) if val == letter)
    for index in letter_indexes:
        hangman_word_asterisks[index] = letter
    print("".join(hangman_word_asterisks))
    if "_" not in hangman_word_asterisks:
        print("Congratulations! You won the game!")
        exit()

def countdown(remaining_guesses):
    if remaining_guesses >= 2:
        print("You have {} guesses left. ".format(remaining_guesses))
    elif remaining_guesses == 1:
        print("You have 1 guess left. ")
    else:
        print("Game over! You have no more guesses left.")
        print("The mystery word was {}.".format(hangman_word))
        exit()

##STARTS HERE

print("Welcome to hangman!")
while True:
    try:
        number_of_guesses = int(input("How many incorrect guesses would you like to have? [6-12] "))
        if number_of_guesses < 6 or number_of_guesses > 12:
            raise ValueError
        else:
            break
    except ValueError:
        print("Something has gone wrong - please choose a number between 6 and 12.")

while True:
    try:
        length_of_words = int(input("How long would you like the word to be? [4-10] "))
        if length_of_words < 4 or length_of_words > 10:
            raise ValueError
        else:
            break
    except ValueError:
        print("Something has gone wrong - please choose a number between 4 and 10.")

possible_words = []
for word in open('english_words.csv').readlines():
    if len(word) == length_of_words+1:
        possible_words.append(word.strip())

wrong_guesses = []
correct_guesses = []
remaining_guesses = number_of_guesses
hangman_word = random.choice(possible_words).upper()
hangman_word_asterisks = ["_"]*(len(hangman_word))
print("".join(hangman_word_asterisks))

while True:
    try:
        guess_input = input("Guess a letter. ").upper()
        if len(guess_input) > 1:
            raise ValueError
        elif guess_input in wrong_guesses:
            raise NameError
        elif guess_input in correct_guesses:
            raise NameError
    except ValueError:
        print("Sorry, there was an issue. Please choose one letter.")
        guess_input = input("Guess a letter. ").upper()
    except NameError:
        print("You've already guessed that letter! ")
        guess_input = input("Guess a letter. ").upper()
    if guess_input in hangman_word:
        print(guess_input + " is in the word.")
        correct_guesses.append(guess_input)
        replace_letters(guess_input)
    else:
        print("Unfortunately {} is not in this word. ".format(guess_input))
        remaining_guesses -= 1
        wrong_guesses.append(guess_input)
        print("Wrong guesses: {}".format(wrong_guesses))
        countdown(remaining_guesses)