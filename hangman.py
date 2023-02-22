import random

def hangman_game(state = 'y'):
    word_options = find_hangman_words()
    
    


def find_hangman_words():    
    my_file = open("leeds.txt",encoding='utf-8-sig')
    hangman_words = []
    for line in my_file:
        if len(str(line)) > 5:
            hangman_words.extend(line.split())
    my_file.close()
    return hangman_words
    



print('----------------------------------------\n', "Hangman!\n",\
          "guess the word one letter at a time\n",\
        '----------------------------------------')
hangman_game()