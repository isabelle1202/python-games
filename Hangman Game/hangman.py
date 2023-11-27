# print start of game
# let the player choose which list they would like to guess from
# while game isnt over, continue letting the player make individual guesses of letters
# if a guess is wrong, add 1 to incorrect guesses. once it hits 11, end the game and display the correct answer.
# let the player run the game again. at the end of the session. list how many games they won out of total games.


import random
import hangman_wordlist


def start_game():
    """starts a hangman game"""

    end_of_game = False

    # values
    incorrect_guesses = 0
    incorrect_word = 0
    total_games = 0
    won_games = 0
    MAX_ATTEMPTS = 11
    WORD_GUESSES = 3
    chosen_category = " "

    # game mechanics

    # choose a category, program chooses a word from list

    user_chosen_category = (input(
        "\nHello! To start a hangman game, please select a category. \n'1' for Animals \n'2'"
        " for Countries \n'3' for Random Words \n "))

    if user_chosen_category == str(1):
        chosen_category = hangman_wordlist.animal_list
    elif user_chosen_category == str(2):
        chosen_category = hangman_wordlist.countries_list
    elif user_chosen_category == str(3):
        chosen_category = hangman_wordlist.random_list
    else:
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

        if guess in wrong_letters:
            print("\nYou've already guessed this letter! Try again :)")

        # lets the player guess the whole word.

        elif len(guess) == len(chosen_word):

            # check if player guessed the word and let them end or continue the game
            if guess == chosen_word:
                print("\n Congratulations! You guessed the word. ")
                while True:
                    continue_game = input(
                        "\nWould you like to play another game? y for yes, n for no ").lower()
                    if continue_game == "y":
                        start_game()
                        break
                    if continue_game == "n":
                        print("Thank you for playing!")
                        end_of_game = True
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
            else:
                incorrect_word += 1
                if WORD_GUESSES - incorrect_word > 1:
                    print(f"\nSorry! That is not the word. You can guess the word"
                          f" {WORD_GUESSES - incorrect_word} more times!")
                if WORD_GUESSES - incorrect_word == 1:
                    print(f"\nSorry! That is not the word. You can guess the word"
                          f" {WORD_GUESSES - incorrect_word} more time!")
                if incorrect_word == WORD_GUESSES:
                    print(
                        f"\nSorry! You ran out of guesses. The word was: {chosen_word}")
                    while True:
                        continue_game = input(
                            "\nWould you like to play another game? y for yes, n for no ").lower()
                        if continue_game == "y":
                            start_game()
                            break
                        if continue_game == "n":
                            print("Thank you for playing!")
                            end_of_game = True
                            break
                        else:
                            print("Invalid input. Please enter 'y' or 'n'.")

        # checks if the player has made a guess of multiple letters that is not the length of the word.

        elif len(guess) > 1:
            print("\nPlease only guess one letter at a time.")

        # checks the player's guess. if correct, replace it in the display.
        # if wrong, add the letter to the list of wrong letters, add to incorrect guesses to keep track of lives
        else:
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter

            if guess not in chosen_word:
                wrong_letters.append(guess)
                incorrect_guesses += 1

                if MAX_ATTEMPTS - incorrect_guesses > 1:
                    print(f"\nSorry! That letter is not in the word. You have"
                          f" {MAX_ATTEMPTS - incorrect_guesses} lives left!")
                if MAX_ATTEMPTS - incorrect_guesses == 1:
                    print(f"\nSorry! That letter is not in the word. You have"
                          f" {MAX_ATTEMPTS - incorrect_guesses} life left!")

        # prints the wrong letters the player has guessed

            print(
                "\nYou have guessed the following wrong letters: " + str(wrong_letters))

            # separates each underscore (_) with a space for readability
            print(" ".join(display))

            # check if player won or lost

            if "_" not in display:
                print("\nCongratulations! You guessed the word.\n")
                while True:
                    continue_game = input(
                        "\nWould you like to play another game? y for yes, n for no ").lower()
                    if continue_game == "y":
                        start_game()
                        break
                    if continue_game == "n":
                        print("Thank you for playing!")
                        end_of_game = True
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")

            if incorrect_guesses == MAX_ATTEMPTS:
                print(
                    f"\nSorry! You ran out of guesses. The word was: {chosen_word}")
                while True:
                    continue_game = input(
                        "\nWould you like to play another game? y for yes, n for no ").lower()
                    if continue_game == "y":
                        start_game()
                        break
                    if continue_game == "n":
                        print("Thank you for playing!")
                        end_of_game = True
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")


start_game()
