import random


def NIM(nim_state = {'a':10 , 'b':10 , 'c':10}):
    gaming = game_on(nim_state)
    while (gaming == True) :
        move = input ("your move: ").split()
        user_letter = str(move[0])
        user_number = int(move [1])
        if nim_state[user_letter] >= user_number and user_number > 1: 
            math_result (user_number, user_letter, nim_state)
            computer_move(nim_state, user_number, user_letter)



def math_result (user_number, user_letter, nim_state)  :  
    nim_state[user_letter] -= user_number 
    print ('removing ', user_number, " from ", user_letter, "gives")
    print("NIM State ", nim_state)
    return nim_state[user_letter]
       

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
            
        except:
            valid = True
    return nim_state[computer_letter]

def game_on(nim_state): 
    a_leftover = nim_state['a'] > 0
    b_leftover = nim_state['b'] > 0
    c_leftover = nim_state['c'] > 0
    if a_leftover  == True and b_leftover  == True and c_leftover == True :
        return True
    elif a_leftover == False and b_leftover == False and c_leftover == False :
        return False
print ("Let's play NIM")
NIM ()
