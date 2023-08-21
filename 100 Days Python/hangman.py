#First, there's too much comments here and most of them are
#reduntants. My idea is for me to remember and not someone else.
#I am a beginner, I can't process codes as my second(third) language 
#yet, and I don't have a good memory too, so for now, it is what it is

import random

#list of all words that will be used in the game.
word_list = ["aardvark", "baboon", "camel"]

#word selected from list (randomized).
word = word_list[random.randint(0, len(word_list) - 1)]

#live counter that will control winning conditions.
liveCounter = 6

#this code will create a empty list that represents the word
#it will be updated with the right letter each time that 
#user had a right input.
word_list_form = []
for i in range(0, len(word)):
    word_list_form.append("_")

#While that will be the main program and will repeat itself until
#there's no more empty spaces or if user run out of lives.
while "_" in word_list_form and liveCounter > 0:
    #User letter input
    userLetter = (input("Choose a Letter: ")).lower()
    
    #This first if exist to prevent loosing a live if a wrong
    #input was given.
    if len(userLetter) != 1 or userLetter.isdigit():
        print("\nWrong input! Input must be only one letter...")
    else:
    #This is the main body of the program, there's the testing of 
    #letters, lives counting, ascii art and win conditions.
        
        #This variable will be used to change the empty block of
        #word_list_form by respecting the letter position.
        userLetterX = 0
        
        #This variable will always start as False and will become
        #True in case of right input
        wasInputRight = False
        
        #This is where each letter from word will be tested and
        #updated if correct.
        for i in word:
            if userLetter == i:
                word_list_form[userLetterX] = i.upper()
                wasInputRight = True
            userLetterX += 1
        print(word_list_form)      
    
        #list of ascii art
        hangmanAscii = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''']

        #This is the end of each loop.
        #If input was wrong, a live will be dropped.
        if wasInputRight == False:
            liveCounter -= 1
            print(hangmanAscii[liveCounter])
            print("\nWrong Letter!")
        
        else:
            print(hangmanAscii[liveCounter])
            print("\nRight Letter!")
    
        print(f"You have {liveCounter} Lives!")
        print("")

#This is the end of the program.
#it will give a WIN or LOOSE based on live counter.
if liveCounter == 0:
    print("\nYou have no more lives!")
else:
    print("\nYou WON!")
