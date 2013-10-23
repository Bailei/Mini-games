# Rock-paper-scissors-lizard-Spock template
import random

# helper functions

def number_to_name(number):
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
        print ("Error: the number is not in the correct range")
    
def name_to_number(name):
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
        print ("Error: the name does not match any of the five correct input strings")

def rpsls(name): 
    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)
    s = (comp_number - player_number) % 5
    print ("player chooses " + name)
    print ("computer chooses " + number_to_name(comp_number))
    if s == 0:    
        print ("Player and computer tie!")
        print ("")
    elif s == 1 or s == 2:
        print ("Computer wins!")
        print ("")
    elif s == 3 or s == 4:
        print ("Player wins!")
        print ("")

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


