number = 10
max_guesses = 3  
remaining_guesses = max_guesses

print(f"I'm thinking of a number. You have {max_guesses} guesses...")

while remaining_guesses > 0:
    guess = input("What number am I thinking of? (Enter 'q' to quit): ")

    if guess.lower() == 'q':
        print(f"The number was {number}.")
        break
    elif guess.isdigit():
        guess = int(guess)
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
    else:
        print("Invalid input. Please enter a number or 'q'.")

    remaining_guesses -= 1
    print(f"You have {remaining_guesses} guesses left.")

    if remaining_guesses == 0:
        print(f"Sorry, you've run out of guesses. The correct number was {number}.")

