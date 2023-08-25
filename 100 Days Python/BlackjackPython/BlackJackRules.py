def rules():
    print('''Blackjack Rules: Hit or Stop

    Objective:
    The objective of Blackjack is to have a hand total higher than the dealer's hand
    total without going over 21.

    Card Values:
    Number cards (2-10) are worth their face value.
    Face cards (Jack, Queen, King) are each worth 10 points.
    The Ace can be worth either 1 or 11 points, whichever is more beneficial for your 
    hand.
                                                                                    
    Gameplay:
    At the beginning, you and the dealer are dealt two cards each.
    You can see both of your own cards, but you can only see one of the dealer's cards.
    After the initial deal, you will have the option to "Hit" or "Stop."

    Hit:
    If you choose to "Hit," you will be dealt an additional card.
    You can continue to "Hit" as many times as you like, but be careful not to 
    21 points, which results in a "bust."

    Stop:
    If you choose to "Stop," you will keep your current hand total and it will be 
    compared to the dealer's hand total.

    Dealer's Turn:
    After you have made your decision, the dealer will reveal their hidden card.
    The dealer must "Hit" if their hand total is 16 or less, and "Stop" if their hand 
    total is 17 or more.

    Winning:
    If your hand total is closer to 21 than the dealer's without going over, you win.
    If your hand total exceeds 21, you bust and lose automatically.
    If the dealer's hand total exceeds 21, they bust and you win.
    If both you and the dealer have the same hand total, it's a push (tie).

    Blackjack:
    If your initial two cards are an Ace and a 10-point card (10, Jack, Queen, King), 
    you have a "Blackjack" and usually win immediately unless the dealer also has a 
    Blackjack.\n
    ''')
