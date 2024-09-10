import simplegui
import random
import math

# Initialize global variables
secret_number = 0
guesses_remaining = 7
range_low = 0
range_high = 100

# Helper function to start and restart the game
def new_game():
    global secret_number, guesses_remaining
    secret_number = random.randrange(range_low, range_high)
    if range_low == 0 and range_high == 100:
        guesses_remaining = 7
    else:
        guesses_remaining = 10
    print "New game. Range is from", range_low, "to", range_high - 1
    print "Number of remaining guesses is", guesses_remaining

# Define event handlers for control panel
def range100():
    global range_low, range_high
    range_low = 0
    range_high = 100
    new_game()

def range1000():
    global range_low, range_high
    range_low = 0
    range_high = 1000
    new_game()
    
def input_guess(guess):
    global guesses_remaining
    guess = int(guess)
    guesses_remaining -= 1
    print "Guess was", guess
    print "Number of remaining guesses is", guesses_remaining

    if guess == secret_number:
        print "Correct!"
        new_game()
    elif guess < secret_number:
        print "Higher!"
    else:
        print "Lower!"

    if guesses_remaining == 0:
        print "You ran out of guesses. The number was", secret_number
        new_game()

# Create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# Register event handlers for control elements and start frame
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# Call new_game to start the first game
new_game()
frame.start()
