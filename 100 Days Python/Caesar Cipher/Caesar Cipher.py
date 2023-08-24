from dataclasses import asdict

"""Simple code to encrypt a message using caesar cipher,
This code can encrypt and decrypt the message"""

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(text="", shift=shift, direction="encode"):
        cypher_list = ""
        if direction == "encode" or direction == "decode":
            for i in text:
                for x in alphabet:
                    if i == x:
                        if direction == "encode":
                            current_letter = alphabet.index(x) + shift
                        if direction == "decode":
                            current_letter = alphabet.index(x) - shift
        
                        #current_letter will always be divided by len just in case
                        current_letter %= (len(alphabet))
                        cypher_list += alphabet[current_letter]
                if i.isdigit() or i == " ":
                    cypher_list += str(i)

            print(f"The text is \"{str(cypher_list)}\"")
        else:
            print("Error, did you made a typo?")
    caesar(text,shift,direction)

continue_playing = True
while continue_playing == True:
    caesar_cipher()
    restar_game = input("Want to restart? (yes/no): ").lower()
    if restar_game == "no":
        continue_playing = False
        print("Thanks for using my program!")
    print("\n")
