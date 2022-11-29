import random

class Dictionary:
    
    def get_dictionary_word_list(self):
        with open('dictionary.txt', 'r') as f:
            list_of_words = []
            for word in f.read().split():
                list_of_words.append(word)
        return list_of_words
    
    def get_random_word(self, list):
        return random.choice(list)
    

key_words = Dictionary()
list_of_words = key_words.get_dictionary_word_list()
key_word = key_words.get_random_word(list_of_words)

    
