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
    total_games = 0
    won_games = 0
    MAX_ATTEMPTS = 11
    chosen_category = " "

    # game mechanics

    # choose a category, program chooses a word from list

    user_chosen_category = (input(
        "Hello! To start a hangman game, please select a category. \n'1' for Animals \n'2' for Countries \n'3' for Random Words \n "))

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

    display = ["_" for _ in range(word_length)]

    # make a guess
    print(" ".join(display))

    while not end_of_game:
        guess = input("\nPlease make a guess!: ").lower()

        if guess in wrong_letters:
            print("\nYou've already guessed this letter! Try again :)")

        elif len(guess) > 1:
            print("\nPlease only guess one letter at a time.")

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

            print(
                "\nYou have guessed the following wrong letters: " + str(wrong_letters))
            print(" ".join(display))

            # check if player won or lost

            if "_" not in display:
                end_of_game = True
                print("\nCongratulations! You guessed the word.\n")
                break

            if incorrect_guesses == MAX_ATTEMPTS:
                end_of_game = True
                print(f"\nYou ran out of guesses. The word was: {chosen_word}")
                break


start_game()
