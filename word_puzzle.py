print("Welcome to the word guessing game!")

secret = "mosiah"
initial_hint = ("_") * len(secret)
guess = -1
num_guesses = 0
print(f"Your hint is: {initial_hint}" )

while guess != secret:

    guess = (input("What is your guess? "))
    num_guesses += 1
    for letter in guess:
        if guess.lower() == secret.lower():
            print(letter.upper())
        elif letter.lower() != secret.lower():
            print("_")
        else:
            print(letter.lower(), end="")
        
    print(f"Your hint is: {guess}" )

print("Congratulations! You guessed it!")
print("It took you 4 guesses.")