import random


def NIM(nim_state = {'a':10 , 'b':10 , 'c':10}):
    gaming = game_on(nim_state)
    while (gaming == True) :
        move = input ("your move: ").split()
        user_letter = str(move[0])
        user_number = int(move [1])
        if nim_state[user_letter] >= user_number and user_number > 1: 
            score = math_result (user_number, user_letter, nim_state)
            gaming = game_on(nim_state)
            find_winner(gaming, score)
        
        score = computer_move(nim_state, user_number, user_letter)
        gaming = game_on(nim_state)
        find_winner(gaming, score)


def math_result (user_number, user_letter, nim_state)  :  
    nim_state[user_letter] -= user_number 
    print ("removing ", user_number, " from ", user_letter, "gives")
    print("NIM State ", nim_state)
    score = 0
    return score
       

def computer_move(nim_state, user_number, user_letter):
    valid = True
    while (valid == True):
        try :
            computerabc = ['a','b','c']
            computer_letter = computerabc[random.randint(0, 2)]
            computer_number = random.randint(1, (nim_state[computer_letter]))
            nim_state[computer_letter] -= computer_number
            print("computer move: ", computer_letter, computer_number)
            print ("removing ", computer_number, " from ", computer_letter, "gives")
            print("NIM State ", nim_state)
            valid = False
            score = 1
            
        except:
            valid = True
    return score

def game_on(nim_state): 
    a_leftover = nim_state['a'] = 0
    b_leftover = nim_state['b'] = 0
    c_leftover = nim_state['c'] = 0
    gaming = True 
    if a_leftover == True and b_leftover == True and c_leftover == True:
        gaming = False
    return gaming
    
    
def find_winner(gaming, score):
    if gaming == False and score == 1:
        print ("You win! Computer loses.")
    elif gaming == False and score == 0:
        print ("Computer wins! You lose.")


print ("Let's play NIM")
NIM ()
