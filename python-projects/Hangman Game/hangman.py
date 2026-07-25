import random
import string

with open("words.txt", "r") as file:
    words = file.read().splitlines()


while True:   

    chosen_word = random.choice(words).lower()
    letters_of_cw = list(chosen_word)

    display_word = ["_"] * len(chosen_word)
    guessed_letters = []


    def check_for_letter(user_input, letters_of_cw, display_word, chances):

        if user_input in letters_of_cw:
            print("Correct letter.")

            for i in range(len(letters_of_cw)):
                if letters_of_cw[i] == user_input:
                    display_word[i] = user_input

        else:
            print("Wrong guess.")
            chances -= 1

        return chances


    print("\nWelcome to Hangman!")
    print("Guess the word before you run out of attempts.")

    print(f"\n1. Easy (10 attempts)\n"
          "2. Medium (6 attempts)\n"
          "3. Difficult (3 attempts)")


    while True:
        try:
            difficulty = int(input("Choose difficulty: "))
        except ValueError:
            print("Invalid Input")
            continue

        if difficulty < 1 or difficulty > 3:
            print("Invalid Input")
            continue

        break


    if difficulty == 1:
        chances = 10
    elif difficulty == 2:
        chances = 6
    else:
        chances = 3


    print(f"\nThe word has {len(chosen_word)} letters.")


    while True:   # Game loop

        print("\nWord:", " ".join(display_word))

        user_input = input("Guess a letter: ").lower()


        if len(user_input) != 1 or user_input not in string.ascii_lowercase:
            print("Please enter only one letter.")
            continue


        if user_input in guessed_letters:
            print("You already guessed this letter.")
            continue


        guessed_letters.append(user_input)


        chances = check_for_letter(
            user_input,
            letters_of_cw,
            display_word,
            chances
        )


        print(f"Remaining guesses: {chances}")


        if display_word == letters_of_cw:
            print("\nCongratulations! You won!")
            break


        if chances == 0:
            print(f"\nYou lost! The word was: {chosen_word}")
            break


    # Play again option

    while True:
        play_again = input("\nDo you want to play again? (y/n): ").lower()

        if play_again == "y":
            break   # breaks play_again loop and starts a new game

        elif play_again == "n":
            print("\nThanks for playing!")
            exit()

        else:
            print("Invalid input. Please enter y or n.")