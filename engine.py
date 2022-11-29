from  class_dictionary import key_word
from class_validator import Validator
from class_stats import Stats

def lost_game():
    
        print("\n*********************************************************************************************************************************************************\n")
        print(f"                                                            Sorry. You lost :(")
        print("\n*********************************************************************************************************************************************************\n")
   

def game_is_on(number_of_tries, key_word = key_word):
    while(number_of_tries > 0):
            
        print(f"The secret word has {str(len(key_word))} letters.")
        
        # See the secret word as you play
        # print(key_word)
        
        test_word = input("Please enter a word that is the result of the game. - ").upper()
        number_of_tries -=1
        
        word_validation = Validator()
        
        while word_validation.check_if_it_is_not_isogram(test_word):
            test_word = input("\nOoopps! Try again. \nThe given word is not a isogram. \nEnter a word that is the result of the game. - ")  
            number_of_tries -=1
            
            print(f"{number_of_tries} tries left")
            if number_of_tries == 0:
                break
            
            
        while len(test_word) != len(key_word):
            test_word = input("\nOoopps! Try again. \nIncorrect number of letters in the given word. \nEnter a word that is the result of the game. - ")
            number_of_tries -=1
            
            print(f"{number_of_tries} tries left")
            if number_of_tries == 0:
                break
                            
        score = Stats(0,0)
        for letter_a in test_word:
            for letter_b in key_word:
                if letter_a == letter_b:
                    
                    # The letter is in the word, in the correct place
                        if test_word.find(letter_a) == key_word.find(letter_b):
                            score.bulls +=1
                                                    
                    # The letter is in the word, but in the wrong place
                        else:
                            score.cows +=1
                            
                                   
        score.show_score()
        if(score.bulls == len(key_word)):
                  
            print("\n*********************************************************************************************************************************************************\n")
            print(f"                                                Well done! The secret word was {key_word} :)\n")
            print("\n*********************************************************************************************************************************************************\n")
            
            break
         
        print(f"You have {str(number_of_tries)} attempts left in the game.\n")
        
        if number_of_tries == 0:
            lost_game()
            break         
           
 