#-----------------------------
#finalhangman
import random



def hangman_game(state = 'y'):
    '''
    This is the main function that combines the function to organize a game and stop the game when the player quits.
    '''

    get_word_options = find_hangman_words()

    while (state == 'y') :

        get_choice = find_word(get_word_options)
        quiz_section(get_choice)
        state = more_question_mark()
        
        


def find_hangman_words():    
    '''
    This creates string read from the file into a list of words that at least 5 characters in length.
    '''

     
    my_file = open("leeds.txt",encoding='utf-8-sig')

    words = my_file.read().split()

    hangman_words = []

    for w in words:

        if len(w) >= 5 and w.islower() and w.isalpha():

            hangman_words.append(w)



    return hangman_words

    

def find_word(hangman_words):
    '''
    This chooses a random word from the list of words that were previously sorted and returns the random word chosen.
    '''
    choice = random.choice(hangman_words)

    return choice


def quiz_section(choice):
    '''
    This function quizzes you on your hangman skills, asking for you to consider a letter to enter and comparing that to the list of letters that the hidden word contains
    It then continues this until you run out of your 7 given guesses or finsish the puzzle correctly.
    '''
    guesses=7

    letters = ['_']*len(choice)
    chosen = ''
    while (guesses > 0 and ''.join(map(str, letters)).isalpha() == False):

        print(''.join(map(str, letters)), '\n', guesses, " guesses left:", chosen, end = '\n')

        user_choose = input(str("next guess: "))
        iter = 0
        if user_choose not in chosen: 
            chosen += user_choose
            if user_choose in choice:
                for i in range(len(choice)):
                    if choice[i] == user_choose:
                        iter+=1
                        letters[i] = choice[i]


                print ("yes!" ,user_choose, "appears ", iter, "times\n")
                if (''.join(map(str, letters)).isalpha() == True):
                            print("!!!!!!!!!! You won! !!!!!!!!!!\n")
                            guesses = 0
            elif user_choose not in choice:
                    guesses-=1
                    print("Sorry",user_choose, "is not in the word\n")
                    if guesses == 0:
                        print("!!!!!!!!!! You lost. !!!!!!!!!!\n", "The word was ", choice) 

def more_question_mark():
    '''
    The function asks whether the program should continue asking hangman quizzes. If they don't answer properly then it will ask them to try again.
    '''
    more = input("more? (y or n) ")
        
    if more == 'n':
        print ("bye")
    elif more != 'y':
        print("try again")
    return more


print("If you want you\n",'----------------------------------------\n',\

          "Hangman!\n",\

          "guess the word one letter at a time\n",\

        '----------------------------------------')

hangman_game()