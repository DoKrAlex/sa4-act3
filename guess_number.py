number = 10
max_guesses = 3
print("I'm thinking of a number...")
for _ in range(max_guesses):
    guess = input("What number am I thinking of? ")
    if guess.lower() == 'q':
        print(f"The number was {number}.")
        break
    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    elif int(guess) < number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")
else:
    print(f"Sorry, you've run out of guesses. The number was {number}.")
