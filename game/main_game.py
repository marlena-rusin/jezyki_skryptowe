from class_dictionary import *
from class_validator import Validator
from class_stats import Stats
from engine import game_is_on

# Menu
choice = 0

while(choice !=5):
    print("1 - New game \n2 - Rules \n3 - Choose the length of the word \n4 - Change number of tries \n5 - End of the game") 
    choice = int(input("What do you choose? - "))
    key_word = key_words.get_random_word(list_of_words)
    
    # New game
    if choice == 1:
        game_is_on(10, key_word)
    
    # Rules
    elif choice == 2:
        print("\n************************************************************************* RULES *************************************************************************\n")
        print("1. The host draws a word, which is an isogram (a word in which no letters are repeated) and informs the player about the number of letters."
                "\n2. The player tries to guess the word."
                    "\n3. The host returns the number of Cows & Bulls after each attempt (Cows - the number of letters\n   in the word, but in the wrong position, Bulls - the number of letters in the word in the correct position)"
                        "\n4. The game ends when the number of Bulls is equal to the number of letters of the secret word.")
        print("\n*********************************************************************************************************************************************************\n")
       
    # Choose the length of the word 
    elif choice == 3:
        length_of_the_word = int(input("How many letters should a random word have? From three to six. - "))
        
        while (length_of_the_word < 3 or length_of_the_word > 6):
            length_of_the_word = int(input("Wrong number of letters. Try again. - "))
 
        while(len(key_word) != length_of_the_word):
            key_word = key_words.get_random_word(list_of_words)
        
        game_is_on(10, key_word)

    # Change number of tries
    elif choice == 4:
        tries = int(input("How many attempts would you like to have? - "))
        game_is_on(tries, key_word)
    
    # End of the game
    elif choice == 5:
        print("Thank you for the game! See you soon.")
    
    # Wrong choice
    else:
        print("Sorry. You chose the wrong number. Try again.")
