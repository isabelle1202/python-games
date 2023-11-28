# print start of game
# let the player choose which list they would like to guess from
# while game isnt over, continue letting the player make individual guesses of letters
# if a guess is wrong, add 1 to incorrect guesses. once it hits 11, end the game and display the correct answer.
# let the player run the game again. at the end of the session. list how many games they won out of total games.


import random
import sys
import os
import hangman_wordlist
import hangman_art
from defined_functions import clear_screen

total_games = 0
won_games = 0


def start_game():
    """starts a hangman game"""

    end_of_game = False

    # values

    global total_games, won_games
    incorrect_guesses = 6
    incorrect_word_guess = 3

    chosen_category = " "

    # game mechanics

    total_games += 1

    # define key functions

    def replay(continue_game):
        """Returns function if input == y, otherwise forces code to halt"""
        while True:
            if continue_game == "y":
                start_game()
            if continue_game == "n":
                print(
                    f"Thank you for playing! You played {total_games} games! Out of those, you won {won_games} times!")
                return sys.exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def print_display():
        """Prints the current state of the display and wrong letters."""

        print("\nYou have guessed the following wrong letters: " + str(wrong_letters))
        print(" ".join(display))

     # choose a category, program chooses a word from list

    while True:
        user_chosen_category = (input(
            "\nHello! To start a hangman game, please select a category. \n'1' for Animals \n'2'"
            " for Countries \n'3' for Random Words \n "))

        if user_chosen_category == str(1):
            chosen_category = hangman_wordlist.animal_list
            break
        elif user_chosen_category == str(2):
            chosen_category = hangman_wordlist.countries_list
            break
        elif user_chosen_category == str(3):
            chosen_category = hangman_wordlist.random_list
            break
        else:
            os.system("cls()")
            print("Please input a valid number to pick your options.")

    chosen_word = random.choice(chosen_category)
    word_length = len(chosen_word)

    wrong_letters = []

    # displays the length of the word in underscores (_)

    display = ["_" for _ in range(word_length)]

    # make a guess
    print(" ".join(display))

    while not end_of_game:
        guess = input("\nPlease make a guess!: ").lower()

        # check if player has already guessed this letter

        if len(guess) == 1 and guess in wrong_letters:
            print("\nYou've already guessed this letter! Try again :)")

        # check if player has already guessed this letter

        # lets the player guess the whole word.

        elif len(guess) == len(chosen_word):

            # check if player guessed the word and let them end or continue the game
            if guess == chosen_word:
                won_games += 1
                print("\nCongratulations! You guessed the word. ")
                continue_game = input(
                    "\nWould you like to play another game? y for yes, n for no ")
                replay(continue_game=continue_game)

            else:
                incorrect_word_guess -= 1
                if incorrect_word_guess > 1:
                    print(f"\nSorry! That is not the word. You can guess the word"
                          f" {incorrect_word_guess} more times!")
                if incorrect_word_guess == 1:
                    print(f"\nSorry! That is not the word. You can guess the word"
                          f" {incorrect_word_guess} more time!")
                if incorrect_word_guess == 0:
                    print(
                        f"\nSorry! You ran out of guesses. The word was: {chosen_word}")
                    continue_game = input(
                        "\nWould you like to play another game? y for yes, n for no ")
                    replay(continue_game)

        # checks if the player has made a guess of multiple letters that is not the length of the word.

        elif len(guess) > 1:
            print("\nPlease only guess one letter at a time.")

        # checks the player's guess. if correct, replace it in the display.
        # if wrong, add the letter to the list of wrong letters, add to incorrect guesses to keep track of lives
        else:
            if len(guess) == 1 and guess in chosen_word:
                clear_screen()
                for position in range(word_length):
                    letter = chosen_word[position]
                    if letter == guess:
                        display[position] = letter
                print(hangman_art.stages[incorrect_guesses])
                print_display()

            if guess not in chosen_word and guess not in wrong_letters:
                clear_screen()
                wrong_letters.append(guess)
                incorrect_guesses -= 1
                print(hangman_art.stages[incorrect_guesses])
                print_display()
                if incorrect_guesses > 1:
                    print(f"\nSorry! That letter is not in the word. You have"
                          f" {incorrect_guesses} lives left!")
                if incorrect_guesses == 1:
                    print("\nSorry! That letter is not in the word. You have"
                          " 1 life left!")

            # check if player won or lost

            if "_" not in display:
                won_games += 1
                print("\nCongratulations! You guessed the word.\n")
                continue_game = input(
                    "\nWould you like to play another game? y for yes, n for no ")
                replay(continue_game)

            if incorrect_guesses == 0:
                print(
                    f"\nSorry! You ran out of guesses. The word was: {chosen_word}")
                continue_game = input(
                    "\nWould you like to play another game? y for yes, n for no ")
                replay(continue_game)


start_game()


# FUTURE ADDITIONS:

# some words have spaces: figure out how to properly integrate this so that the game isn't confusing

# consider adding a difficulty function (easy, normal, hard, expert)
# different amounts of lives, difficulty of words, limited guesses, timers
# subcategories in each category
