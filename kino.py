# Import random module
import random
globalChoices = []

# Define a function to play Keno
def play_keno():
    # Ask the player how many numbers they want to pick (1-15)
    num_picks = int(input("How many numbers do you want to pick? (1 -10): "))
    # Validate the input
    while num_picks < 1 or num_picks > 10:
        print("Invalid input. Please enter a number between 1 and 10.")
        num_picks = int(input("How many numbers do you want to pick? (1-10): "))

    # Ask the player how much they want to wager
    wager = float(input("How much do you want to wager? ($): "))
    # Validate the input
    while wager <= 0:
        print("Invalid input. Please enter a positive amount.")
        wager = float(input("how much do you want to wager? ($): "))

    # Create a klist of numbers from 1 to 80
    numbers = list(range(1, 81))

    # Create an empty list to store the player's choices
    choices = []

    # Check Global variable
    global globalChoices
    if len(globalChoices) == 0:
        choices.append(globalChoices)
    else: choices = globalChoices

    # Ask the player to pick their numbers
    print("Please pick your numbers (1-80): ")
    # Loop for num_picks times
    for i in range(num_picks):
        # Ask the player to enter a number
        choice = int(input(f"Number {i+1}: "))
        # Validate the input
        while choice < 1 or choice > 80 or choice in choices:
            print("Invalid input. Please enter a number between 1 and 80 that you have not picked before")
            choice = int(input(f"Number {i+1}: "))
        # Append the choice to the choices list
        choices.append(choice)

    # Print the player's choices
    print(f"Your choices are: {choices}")

    # Create an empty list to store the random numbers
    draws = []

    # Loop for 20 times
    for i in range(20):
        # Generate a random number from the numbers list
        draw = random.choice(numbers)
        # Remove the draw from the numbers list
        numbers.remove(draw)
        # Append the draw to the draws list
        draws.append(draw)

    # Print the random numbers
    print(f"The drawn numbers are: {draws}")

    # Create an empty list to store the matches
    matches = []

    # Loop through the choices lists
    for choice in choices:
        # Check if the choice is in the draws list
        if choice in draws:
            # Append the choice to the matches list
            matches.append(choice)

    # Print the matches
    print(f"You matched {len(matches)} numbers: {matches}")

    # Define a payout table based on num_picks and number of matches
    payout_table = {
        0: {0: 1},
        1: {0: 1, 1: 2},
        2: {0: 0, 1: 0, 2: 8},
        3: {0: 0, 1: 0, 2: 2, 3: 16},
        4: {0: 0, 1: 0, 2: 0, 3: 8, 4: 50},
        5: {0: 0, 1: 0, 2: 0, 3: 2, 4: 16, 5: 200},
        6: {0: 1, 1: 0, 2: 0, 3: 1, 4: 2, 5: 20, 6: 600},
        7: {0: 1, 1: 0, 2: 0, 3: 0, 4: 2, 5: 10, 6: 100, 7: 4000},
        8: {0: 1, 1: 0, 2: 0, 3: 0, 4: 1, 5: 4, 5: 40, 6: 400, 7: 20000},
        9: {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 3, 6: 20, 7: 200, 8: 2000, 9: 50000},
        10: {0: 1, 1: 0, 2: 0, 3: 0, 4: 0, 5: 3, 6: 10, 7: 20, 8: 500, 9: 10000, 10: 200000},
    }

    # Calculate the payout based on num_picks and number of matches
    payout = payout_table[num_picks][len(matches)] * wager
    
    # Print the payout
    print(f"Your payout is ${payout:.2f}")

    # Ask the player if they want to play again
    answer = input("Do you want to play again? (Y/N): ")
    # Validate the input
    while answer not in ["Y","N"]:
        print("Invalid input. Please enter Y or N.")
        answer = input("Do you want to play again (Y/N): ")
    # If yes, call the play_keno function again
    if answer == "Y":
        play_keno()
    # If no, print a farewell message and end the program
    else:
        print("Thank you for playing!")

# Call the play_keno function for the first time
# Define a function to play keno with a reuse parameter

play_keno()