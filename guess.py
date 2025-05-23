import random  # Import the random module to generate random numbers

# Ask the user to enter the upper limit for the random number
top_of_range = input("Type a number (greater than 0): ")

# Check if the input is a digit (i.e., a valid positive number)
if top_of_range.isdigit():
    top_of_range = int(top_of_range)  # Convert input from string to integer

    # Check if the number is greater than 0
    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')  # Show error message
        quit()  # Exit the program
else:
    print('Please type a number next time.')  # Show error if input is not a digit
    quit()  # Exit the program

# Generate a random number between 0 and top_of_range - 1
random_number = random.randint(0, top_of_range - 1)
guesses = 0  # Initialize the guess counter

# Start a loop for the user to make guesses
while True:
    guesses += 1  # Increment the guess counter
    user_guess = input("Make a guess: ")  # Prompt the user to guess

    # Check if the user's guess is a valid number
    if user_guess.isdigit():
        user_guess = int(user_guess)  # Convert the guess to integer
    else:
        print('Please type a number next time.')  # Invalid input message
        continue  # Skip the rest of the loop and ask again

    # Check if the guess is correct
    if user_guess == random_number:
        print("You got it!")  # Success message
        break  # Exit the loop
    elif user_guess > random_number:
        print("You were above the number!")  # Hint: too high
    else:
        print("You were below the number!")  # Hint: too low

# Print how many guesses the user took
print("You got it in", guesses, "guesses")