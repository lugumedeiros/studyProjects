"""This doesn't work in a normal console, the project was intended to be
made in replit using clear() method that would clear console."""

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the Secret Auction!\n\
This program will ask for a name and a bid for each person.\n\
\nLet's start!\n")
bidder_list = [
    {"name": "none", "bid": 1},
    ]

def bidder():
    name = input("What is your name?: ")
    bid = input("What is yout bid?: ")
    bidder_list.append({"name": name, "bid": bid})

has_more_bidder = True
while has_more_bidder:
    bidder()
    more_bidder = input("\nAre there any other bidders? Y/N: ").lower()
    if more_bidder == "n":
        has_more_bidder = False
        
biggest_bid = 0
biggest_bidder = "none"
is_draw = False
for i in range(0, len(bidder_list)):
    current_bidder = bidder_list[i]
    current_bid = int(bidder_list[i]["bid"])
    
    if current_bid == biggest_bid:
        is_draw = True
        
    #tests print((current_bid),type(current_bid)),type(biggest_bid))

    if current_bid > biggest_bid:
        biggest_bid = int(current_bidder["bid"])
        biggest_bidder = current_bidder["name"]
        is_draw = False

if is_draw:
    print(f"\nThere's a DRAW, biggest bid was {biggest_bid}")    
else:
    print(f"\nThe winner is {biggest_bidder} with a bid of {biggest_bid} dollars!")
    
