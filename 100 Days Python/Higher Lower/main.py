#grabs a random data and start the game
#grabs a new date and ask for user if higher or lower
#if response is right, repeat, else finish the game
#This game could be a lot improved but I don't have much time right now
#Most of the bad part is the repeating p2 and p1, that I probably could use the dictionary

import random
from gamedata import data
import gameart

r_person1 = random.randint(0,49)
p1_name = data[r_person1]['name']
p1_description = data[r_person1]['description']
p1_country = data[r_person1]['country']
p1_follower = data[r_person1]['follower_count']
won = True
counter = 0

print(gameart.logo)

while won:
    print(f'Your current count is {counter}')
    print(f'Compare A: {p1_name}, a {p1_description}, from {p1_country}', end='')
    print(gameart.vs)
    r_person2 = random.randint(0,49)
    
    p2_name = data[r_person2]['name']
    p2_description = data[r_person2]['description']
    p2_country = data[r_person2]['country']
    p2_follower = data[r_person2]['follower_count']
    print(f'Against B: {p2_name}, a {p2_description}, from {p2_country}')
    
    while True:
        choice = input('Who has more followers? (A/B): ').lower()
        if choice == 'b':
            if p2_follower > p1_follower:
                counter += 1
                p1_name = p2_name
                p1_description = p2_description
                p1_country = p2_country
                p1_follower = p2_follower
                break
            else:
                won = False
                break
        elif choice == 'a':
            if p1_follower > p2_follower:
                counter += 1
                p1_name = p2_name
                p1_description = p2_description
                p1_country = p2_country
                p1_follower = p2_follower
                break
            else:
                won = False
                break
        else:
            print('Wrong input')
    print('\n#################################\n')
            
if counter == 0:
    print(f'You already missed? Try Again!')

elif counter < 3:
    print(f'You know a bit huh, you got {counter} rights')
elif counter < 5:
    print(f'You know a lot of Instagram Celebrities. You got {counter} rights')
else:
    print(f'Wow, you waste a lot of time on Instagram... You got {counter} rights')
  