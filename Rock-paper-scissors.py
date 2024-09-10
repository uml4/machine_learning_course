# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def name_to_number(name):
    """
    Converts the string name into a number between 0 and 4 as described above.
    """
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print("Error: Invalid name.")
        return -1  # Indicate an error


def number_to_name(number):
    """
    Converts a number in the range 0 to 4 into its corresponding name as a string.
    """
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print("Error: Invalid number.")
        return ""  # Indicate an error


def rpsls(player_choice):
    """
    Simulates playing a round of Rock-paper-scissors-lizard-Spock against the computer.
    """

    # Print a blank line to separate consecutive games
    print()

    # Print the player's choice
    print(f"Player chooses {player_choice}")

    # Convert the player's choice to a number
    player_number = name_to_number(player_choice)

    # Generate a random guess for the computer
    comp_number = random.randrange(0, 5)

    # Convert the computer's number to a name
    comp_choice = number_to_name(comp_number)

    # Print the computer's choice
    print(f"Computer chooses {comp_choice}")

    # Determine the winner
    difference = (comp_number - player_number) % 5
    if difference == 0:
        print("Player and computer tie!")
    elif difference <= 2:
        print("Computer wins!")
    else:
        print("Player wins!")


# Test the game
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
