import random



def hangman_game(state = 'y', score = 0):

    get_word_options = find_hangman_words()

    while (state == 'y') :

        get_choice = find_word(get_word_options)

        score = quiz_section(get_choice, score)
        


def find_hangman_words():    

    my_file = open("leeds.txt",encoding='utf-8-sig')

    words = my_file.read().split()

    hangman_words = []

    for w in words:

        if len(w) >= 5 and w.islower() and w.isalpha():

            hangman_words.append(w)



    return hangman_words

    

def find_word(hangman_words):

    choice = random.choice(hangman_words)

    return choice


def quiz_section(choice, score):
    print (choice)
    guesses=7

    letters = ['_']*len(choice)

    while (guesses > 0 and ''.join(map(str, letters)).isalpha() == False):
        print(''.join(map(str, letters)), '\n', guesses, " guesses left:")

        user_choose = input(str("next guess: "))
        iter = 0
        if user_choose in choice:
            
            for i in range(len(choice)):
                if choice[i] == user_choose:
                    iter+=1
                    letters[i] = choice[i]
                    if (''.join(map(str, letters)).isalpha() == True):
                        print("!!!!!!!!!! You won! !!!!!!!!!!")
                        score +=1
                        guesses = 0
                
            print ("yes!" ,user_choose, "appears ", iter, "times")
        elif choice[i] != user_choose:
                guesses-=1
                print("Sorry",user_choose, "is not in the word")
    return score


print("If you want you\n",'----------------------------------------\n',\

          "Hangman!\n",\

          "guess the word one letter at a time\n",\

        '----------------------------------------')

hangman_game()