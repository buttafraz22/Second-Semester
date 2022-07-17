from words import words_list
from stages import stages
import random


def get_random_word():
    word = random.choice(words_list)
    return word.upper()


def get_hangman_stage(tries):
    return stages[tries]


def game_play(word):
    user_input = "_" * len(word)  # prints underscores in the first iteration
    guess = False
    guess_letter = []  # list for holding letters input by user
    guess_word = []  # list for holding words input by user
    user_tries = 6  # corresponds to hangman's "body parts"

    print("Welcome to Hangman")
    print(get_hangman_stage(user_tries))
    print(user_input)
    print("\n")

    while not guess and user_tries > 0:             # the main game loop
        entry = input("Please guess a letter or word  ").upper()

        if len(entry) == 1 and entry.isalpha():
            if entry in guess_letter:
                print("You already guessed the letter",entry)
                
            elif entry not in word:
                print("Entry is not in word",entry)
                user_tries -= 1
                guess_letter.append(entry)
                
            else:
                print("Well done, ",entry," is in the word")
                guess_letter.append(entry)
                word_as_list = list(user_input)
                indices = [i for i , letter in enumerate(word) if letter == entry] # generates an indexed list
                for index in indices:
                    word_as_list[index] = entry
                    user_input = "".join(word_as_list)
                    if"_"not in user_input:
                        guess = True
        
        elif len(entry) == len(word) and entry.isalpha():
            if entry in guess_word:
                print("You already guessed the word")
                
            elif entry != word:
                print(entry," is not the word")
                user_tries -= 1
                guess_word.append(entry)
            
            else:
                guess = True
                user_input = word
                
        else:
             print("Not a valid guess,Try again")
             
        print(get_hangman_stage(user_tries))
        print(user_input)
        print("\n")
        
    if guess:
        print("Congrats, You won!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")