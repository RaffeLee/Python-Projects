import random

def hangman_game(state = 'y'):
    get_word_options = find_hangman_words()
    while (state == 'y') :
        get_choice = find_word(get_word_options)
        quiz_section(get_choice)


def find_hangman_words():    
    my_file = open("leeds.txt",encoding='utf-8-sig')
    hangman_words = []
    for line in my_file:
        if len(str(line)) > 5:
            hangman_words.extend(line.split())
    my_file.close()
    return hangman_words
    
def find_word(hangman_words):
    randomizer = random.sample(range(0, len(hangman_words)), 1)
    choice = hangman_words[randomizer[0]]
    return choice

def quiz_section(choice):
    print('_'*(int(len(choice))))



print('----------------------------------------\n', "Hangman!\n",\
          "guess the word one letter at a time\n",\
        '----------------------------------------')
hangman_game()