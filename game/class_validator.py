import unittest

class Validator:
    
    def check_if_it_is_not_isogram(self, word):
        letter_list = []
        
        for letter in word:
            if letter in letter_list:
                return True
            letter_list.append(letter) 
        return False
    
test = Validator()

def test_check_if_it_is_not_isogram():
    assert test.check_if_it_is_not_isogram('KOT') == False
    assert test.check_if_it_is_not_isogram('TOTEM') == True
    