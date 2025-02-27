import random

# List of words to guess
word_list = ["python", "hangman", "developer", "internship", "shadowfox","Ambedkar"]

def choose_word():
    return random.choice(word_list).upper()

def display_hangman(tries):
    stages = [
        "  -----\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
        "  -----\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
        "  -----\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
        "  -----\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
        "  -----\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
        "  -----\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
        "  -----\n  |   |\n      |\n      |\n      |\n      |\n========="
    ]
    return stages[tries]

def hangman():
    word = choose_word()
    word_letters = set(word)  # Letters in the word
    guessed_letters = set()   # Letters guessed by the user
    incorrect_guesses = 0
    max_attempts = 6

    print("🎮 Welcome to Hangman! 🎮")
    print(display_hangman(incorrect_guesses))
    print("Word: " + "_ " * len(word))

    while incorrect_guesses < max_attempts and word_letters:
        guess = input("\nGuess a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print(" Good guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")

        # Show the hangman figure and progress
        print(display_hangman(incorrect_guesses))

        # Display the current progress of the word
        word_display = [letter if letter in guessed_letters else "_" for letter in word]
        print("Word: " + " ".join(word_display))

    if not word_letters:
        print("\n Congratulations! You guessed the word:", word)
    else:
        print("\n You lost! The word was:", word)

    # Play again option
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()

# Run the game
hangman()
