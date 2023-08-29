#This isaa simple coffee machine program
#The prof used a disctionary but I ended using just defs for each
#Maybe I will change later, idk.

water = 300
milk = 200
coffee = 100
money = 0
machine_onn = True

def expresso(water, coffee):
    return water > 50 and coffee > 18

def latte(water, coffee, milk):
    return water > 200 and coffee > 24 and milk > 150

def cappuccino(water, coffee, milk):
    return True if water > 250 and coffee > 24 and milk > 100 else False


def money_count(coffee):
    if coffee == "expresso":
        price = 1.5
    elif coffee == "latte":
        price = 2.5
    elif coffee == "cappuccino":
        price = 3.0
    print(f"A {coffee} is ${price}")
        
    quarter = int(input('How many quarters?: ')) * 0.25
    dime = int(input('How many dimes?: ')) * 0.10
    nickel = int(input('How many nickels?: ')) * 0.05
    penny = int(input('How many pennys?: ')) * 0.01
    result = quarter + dime + nickel + penny

    if result >= price:
        print(f"Your change is {result - price}")
    else:
        print(f"Not enough money, take you ${result} back.")                        
    return result >= price

print("Welcome to the fake coffee machine (T-T)")

while machine_onn:
    user_coffee = input('\nWhat would you like? (expresso/latte/cappuccino): ').lower()
    #Expresso
    if user_coffee == 'expresso':
        if expresso(water, coffee):
            if money_count("expresso"):
                print("Here is your expresso, enjoy!")
                money += 2
                water -= 50
                coffee -= 18
        else:
            print("There's no enough resoucers for your coffee, we are sorry!")
            break
    #Latte
    elif user_coffee == 'latte':
        if latte(water, coffee, milk):
            if money_count("latte"):
                print("Here is your latte, enjoy!")
                money += 2
                water -= 250
                coffee -= 24
                milk -= 150
        else:
            print("There's no enough resoucers for your coffee, we are sorry!")
            break
    #Cappuccino
    elif user_coffee == 'cappuccino':
        if cappuccino(water, coffee, milk):
            if money_count("cappuccino"):
                print("Here is your latte, enjoy!")
                money += 2
                water -= 200
                coffee -= 24
                milk -= 100
        else:
            print("There's no enough resoucers for your coffee, we are sorry!")
            break
    elif user_coffee == 'report':
        print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}ml\nMoney: ${money}')
    else: 
        print('Wrong input')
    try_again = input("Do you want to restart this machine? (y/n)").lower()
    if try_again == "n" or try_again == "no":
        machine_onn = False
