#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) #nTimes
nr_symbols = int(input(f"How many symbols would you like?\n")) #nTimes
nr_numbers = int(input(f"How many numbers would you like?\n")) #nTimes

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

'''value_list = is the new password list
nTimes = is the amount of characters of a list(nr_letters, nr_symbols, nr_numbers)
list_choice = is the list of characters used (letters, numbers, symbols)'''

def randomKey(nTimes, list_choice):
#def that will create a new list with N characters from already made list.
    value_list = []
    for i in range(0, nTimes):
        value_list.append(list_choice[random.randint(0, len(list_choice) - 1)])
    return value_list

#def randomKey for each list
letterKey = randomKey(nr_letters, letters)
symbolKey = randomKey(nr_symbols, symbols)
numberKey = randomKey(nr_numbers, numbers)

#password but in sequence list1+list2+list3
password = letterKey + symbolKey + numberKey

#password test
#print(password)

#empty new list
sortPassword = []

#code to randomize new password
for i in range(0, len(password)):
    lengthPass = len(password) - 1
    randomNumber = random.randint(0, len(password) - 1)
    sortPassword += password[randomNumber]
    password.pop(randomNumber)

print(sortPassword)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
