import random

def hangman_game(state = 'y', score = 0):
    get_word_options = find_hangman_words()
    while (state == 'y') :
        get_choice = find_word(get_word_options)
        state = quiz_section(get_choice, score)

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

def quiz_section(choice, score):
    guesses=7
    letters = ['_']*len(choice)
    while (guesses > 0):
        print('_'*(int(len(choice))), '\n', guesses, " guesses left:")
        user_choose = input(str("next guess: "))
        for i in range(len(choice)):
            if choice[i] == user_choose:
                letters[i] = user_choose
                print ('yes!')
                guesses +=1
            else :
                guesses-=1
                
        print (choice)
        print (letters)
    state = 'n'    
    return state    
                




print("If you want you\n",'----------------------------------------\n',\
          "Hangman!\n",\
          "guess the word one letter at a time\n",\
        '----------------------------------------')
hangman_game()