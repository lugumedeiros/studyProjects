from operator import contains
import random
import BlackJackRules

'''I made a whole code for this game and in the end I was not satfied, there was some
loopholes and the sum was not calculating the best possibilites of a hand.
It worked, but like I said, it was mediocre.
That's why this code is a lot more close to the proffesor's. But the problem still 
appears here.
Let me explain the problem, this code gives a 11 for Aces, and if the sum is bigger 
than 21, then the **last** 11 will be changed to a 1.
But that's not how we do in real life, getting multiples Aces is a bit improbable,
but when that happens, the whole math will be different because we are dealing with
multiple cards that equals to 2 different numbers.
exemple: If you get [A, A] you have 2 or 12 or 22. It's 3 different results.
so if [A, A, 2] equals to [4, 14, 24].
The problem of this code is that when we check the first A, if A <21 it will
stay as 11 and will not change later.
It's important to change later because we can also get a [A, A, 2, 6] and sum options
for this hand is [10, 19, 30]. We have 2 working possibilities yet, and we can even
draw more cards to try a better result, but this code can bust if we try another card
because older Aces will not be changed.
I don't need to say how bad will be if the hand is [A,A,A]
Another problem is that the cards are ilimited, that means that both dealer and user
can have [A,A,...,A,A] hand. Very unlikely, but can happen. This code ignores this and
I agree, it's so unlikely and I believe that doesn't need to be cared right now in
this level. Or maybe I'm wrong.
I don't know how to fix it, it is what it is, maybe in the future I will try again.
'''

user_hand = []
dealer_hand = []
is_game_continue = True

game_rules = input("Do you want to read the rules? (y/n): ").lower()

if game_rules == "y" or game_rules == "yes":
    BlackJackRules.rules()
    print("Let's start then!\n")

def card_draw():
    '''Draw one card'''
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8 ,9 ,10 , 10, 10, 10]
    card = random.choice(card_deck)
    return card

def calculation_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,dealer_score):
    if user_score == dealer_score:
        return "Tie"
    elif user_score == 0:
        return "You WON"
    elif dealer_score == 0:
        return "Dealer WON"
    elif user_score > 21:
        return "You busted! Dealer WON!"
    elif dealer_score > 21:
        return "Dealer Busted! You WON!"
    elif dealer_score > user_score:
        return "Dealer WON"
    else:
        return "You WON"
        

for i in range(2):
    user_hand.append(card_draw())
    dealer_hand.append(card_draw())
    
user_score = calculation_score(user_hand)
dealer_score = calculation_score(dealer_hand)

while is_game_continue:
    user_score = calculation_score(user_hand)
    dealer_score = calculation_score(dealer_hand)

    print(f" Dealer card is: [{dealer_hand[0]}]")
    print(f" Your hand is: {user_hand}")

    if user_score == 0 or dealer_score == 0 or user_score > 21:
        is_game_continue = False
    else:
        user_should_deal = input("Do you want to draw more? (y/n): ").lower()
        
        if user_should_deal == "y" or user_should_deal == "yes":
            user_hand.append(card_draw())
        else:
            print("bye")
            is_game_continue = False
            
while dealer_score != 0 and dealer_score < 17:
    dealer_hand.append(card_draw())
    dealer_score = calculation_score(dealer_hand)
        
print(compare(user_score, dealer_score))

###############################################################################
''' This is the old code, kind of.
I tried to fix a lot of times and in the end I gave up.
This code here is not the exactly the one I made,
it's a fragment of it + some attempts to make it work like expected
It's here if you want to check.
'''

'''

def change_a(hand):
    "This function will change all 'A' in list to [1,11]"
    new_list = []
    for i in hand:
        if i == "A":
            new_list.append(11)
        else:
            new_list.append(i)
    return new_list

def hit_or_stand():
   "Will conitnue only stop with right input"
    hit_again = input("Do you want to hit or stand?:\n")
    if hit_again == "hit":
        return True
    elif hit_again == "stand":
        return False
    else:
        print("Something went wrong. Try again!")
            
def who_won(user_number_hand, user_hand_sum, dealer_number_hand, dealer_hand_sum):
    if blackjack(user_number_hand):
        print(f"You have a BlackJack. You WON!")
    elif blackjack(dealer_number_hand):
        print(f"Dealer has a BlackJack. You lose!")
    elif busted:
        print(f"You busted. You lose!")
    elif dealer_hand_sum < 17:
        print(f"Dealer Busted. You won!")
    elif dealer_hand_sum > user_hand_sum:
        print(f"Dealer hand is closer to 21 than you. You lose!")
    elif dealer_hand_sum == user_hand_sum:
        print(f"Dealer hand has the same value of your hand. It's a tie!")
    else:
        print(f"Your hand is closer to 21 than Dealer's. You won!")

def blackjack(hand):
    if (hand[0] == 11 and hand[1] == 1) or (hand[1] == 11 and hand[0]):
        return True
    else:
        return False

user_want_game_rules = input("Welcome to the Simple BlackJack Python!\n\
The rules are simpler with only Stand or Hit actions.\n\
Do you want to read all rules? (yes/no): ").lower()
if user_want_game_rules == "yes":
    print(game_rules)
    BlackJackRules.rules()

print("Okay, let's start then!\n")

for i in range(0,2):
    card_draw(user_hand)
    
card_draw(dealer_hand)

while sum(dealer_number_hand) < 17:
    card_draw(dealer_hand)
    print(dealer_hand)
    dealer_number_hand = change_a(dealer_hand)
    for i in dealer_number_hand:
        if i != 11:
            
        elif i == 11:
            if current_sum + 11 < 21:
                current_sum += 11
            else:
                current_sum += 1

while True:
    print(f"Dealer: [{dealer_hand[0]}]")
    print(f"\nYour hand is {user_hand}")
    if hit_or_stand():
        card_draw(user_hand)
    else:
        break

print(f"\nThis is your final hand: {user_hand}")

current_sum = 0
for i in user_hand:
    if i != 11 or i != 1:
        current_sum += i
    elif i == 11:
        if current_sum + 10 > 21:
            current_sum += 10
        else:
            current_sum += 1
user_hand_sum = current_sum

print(f"Dealer: [{dealer_number_hand}]")
print("")

who_won(user_hand, dealer_hand)
'''
