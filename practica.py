def play_word_guessing_game():
    secret_word = "mosiah"
    guessed_word = ["_"] * len(secret_word)
    num_guesses = 0

    print("Welcome to the word guessing game!\n")
    print("Your hint is: " + " ".join(guessed_word))

    while True:
        guess = input("What is your guess? ").lower()
        num_guesses += 1

        if len(guess) != len(secret_word):
            print("Sorry, the guess must have the same number of letters as the secret word.\n")
            continue

        if guess == secret_word:
            print("Congratulations! You guessed it!")
            print("It took you", num_guesses, "guesses.")
            break

        hint = ""

        for i, letter in enumerate(guess):
            if letter == secret_word[i]:
                hint += letter.upper()
            elif letter in secret_word:
                hint += letter.lower()
            else:
                hint += "_"

        print("Your hint is: " + " ".join(hint))
        print()

play_word_guessing_game()
