import random
from asciiart import art

print(art)
print("\nWelcome to the Number Guessing Game!")
try_again = True
while try_again:
    random_number = random.randint(1,101)
    life = 0
    user_won = False
    difficulty = "none"

    def is_d_input_right(value):
        '''Will return true if value is easy, mid or hard'''
        return True if value == "easy" or value == "mid" or value == "hard" else False

    def is_user_input_valid(value):
        '''return true if value is a number'''
        return value.isnumeric()

    def is_win_or_wrong(value,cpu_value):
        '''True if user found the right number, False will print if bigger or smaller'''
        if value == cpu_value:
            return True
        elif value > cpu_value:
            print(f"{value} is bigger!")
            return False
        elif value < cpu_value:
            print(f"{value} is smaller!")
            return False

    def continue_playing():
        '''Will ask if player wants to try again.'''
        user_input = input("\nDo you want to try again? (yes/no)").lower()
        if user_input == "yes" or user_input == "y":
            print("Okay, let's restart!\n\n")
            return True
        else:
            print("Bye bye, see you next time!")
            return False

    while not is_d_input_right(difficulty):
        difficulty = input("Choose your difficulty (easy / mid / hard):\n").lower()
        if not is_d_input_right(difficulty):
            print("Make sure to type only 'easy', 'mid' or 'hard'")
        else:
            print(f"Let's start with {difficulty} level then!")

    if difficulty == "easy":
        life = 10
    elif difficulty == "mid":
        life = 7
    elif difficulty == "hard":
        life = 5

    while life > 0:
        print(f"\nYou have {life} heart(s)!")
        user_number = input("Guess a Number: ")
        if is_user_input_valid(user_number):
            user_number = int(user_number)
            if is_win_or_wrong(user_number, random_number):
                user_won = True
                break
            else:
                print("Try again")
                life -= 1
        else:
            print("only numbers are allowed!")
        
    if is_win_or_wrong(user_number, random_number):
        print(f"Congratulations!!! You found the Number {random_number}")
    else:
        print(f"You ran out of hearts, the number was {random_number}!")
    try_again = continue_playing()
