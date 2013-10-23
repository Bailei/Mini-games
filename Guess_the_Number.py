import simplegui
import random

# initialize global variables used in your code
secret_num = 0
num_range = 0

# helper function to start and restart the game
def new_game():
    global secret_num, guess_num, num_range, remain_guess
    remain_guess = remain_guess - 1
    if remain_guess >= 0:
        print ('Number of remaining guess is ', remain_guess)
        if guess_num > secret_num:
            print ('Lower!')
            print ('')
        elif guess_num < secret_num:
            print ('Higher!')
            print ('')
        else:
            print ('Correct!')
            print ('')
    else:
        print ('You ran out of guesses. The number was ', secret_num)
        

# define event handlers for control panel
def range100():
    global secret_num, num_range, remain_guess
    num_range = 100
    remain_guess = 7
    secret_num = random.randrange(0, 100)
    print ('New game. Range is from 0 to 100')
    print ('Number of remaining guess is ', remain_guess)
    print ('')

def range1000():
    global secret_num, num_range, remain_guess
    num_range = 1000
    remain_guess = 10
    secret_num = random.randrange(0, 1000)
    print ('New game. Range is from 0 to 1000')
    print ('Number of remaining guess is ', remain_guess)
    print ('')
    
def input_guess(guess):
    global guess_num, remain_guess
    guess_num = int(guess)
    print ('Guess was ', guess)
    new_game()
    
# create frame
f = simplegui.create_frame('Guess the number', 200, 200)

# register event handlers for control elements
f.add_button('Range is [0, 100)', range100, 200)
f.add_button('Range is [0, 1000)', range1000, 200)
f.add_input('Enter a guess', input_guess, 200)


# call new_game and start frame
f.start()

