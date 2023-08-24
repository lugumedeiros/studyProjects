import random

''' The idea of this program is to calculate a rock, paper and scissors based in a simple calculation of 
(user_hand_id) - (cpu_hand_id), where scissors(1), paper(2) and rock(3). The result of such calculation
will be a Draw if equals to ZERO or (user_hand_id == cpu_hand_id).
For user winning hand the result must be 2(paper - rock) or -1(scissors - paper; paper - rock).
Everything else (-2, 1) is a win hand for CPU.'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_input = input("What is your choice? scissors, paper or rock?\n")
hands = [scissors, paper, rock]
random_hand = random.randint(0, 2) # random number

cpu_hand = hands[random_hand] # this selects the hand for cpu based on random
cpu_hand_id = random_hand + 1 # this is for the calculation in the end

user_hand = "none" #starts as none so it doen't give hand in error
user_hand_id = 9 #starts as 9 so it doesn't give a win in error

#This code transforms string into a working hand
if user_input.lower() == "scissors":
    user_hand = scissors #this variables = to the printing hand
    user_hand_id = 1 #this variable is for the calculation in the end
elif user_input.lower() == "paper":
    user_hand = paper
    user_hand_id = 2
elif user_input.lower() == "rock":
    user_hand = rock
    user_hand_id = 3
else:
    print("Error! You made a typo!") #error in case user wrote wrong string
    exit()

#test_inputs
#print(user_hand_id)
#print(cpu_hand_id)

#variable for result print
cpu_win = "\nCPU WON!"
user_win = "\nUSER WON!"
draw = "\nDRAW!"

#print results in ascii
print(f"You:\n{user_hand}\n")
print(f"CPU:\n{cpu_hand}\n")

#This code is to calculate the hand winner
win_hand = user_hand_id - cpu_hand_id

#code for choosing winner
if user_hand_id == cpu_hand_id:
    print(draw)
elif win_hand == 2 or win_hand -1:
    print(user_win)
else:
    print(cpu_win)
    
