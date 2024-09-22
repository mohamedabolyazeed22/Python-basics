print("Welcome to the Number Guessing Game!")
print("Think of a number between 0 and 100, and I'll try to guess it.")

# Initialize the lower and upper bounds for the guessing range
low = 0
high = 100
state = True

while state:
    # Calculate the midpoint of the current range
    medium = (low + high) // 2
    
    # Prompt the user with the current guess
    print("\nIs your secret number " + str(medium) + "?")
    
    # Ask the user for feedback on the guess
    guess = input("Enter 'h' if the guess is too high, 'l' if it's too low, or 'c' if it's correct: ").lower()
    
    if guess == 'c':
        # If the guess is correct, end the game
        print(f"🎉 Game over! Your secret number was: {medium}. Thanks for playing!")
        state = False
    elif guess == 'h':
        # Adjust the upper bound if the guess is too high
        high = medium
        print("I'll guess lower next time.")
    elif guess == 'l':
        # Adjust the lower bound if the guess is too low
        low = medium
        print("I'll guess higher next time.")
    else:
        # Handle unexpected input
        print("Oops! I didn't catch that. Please enter 'h', 'l', or 'c'.")
