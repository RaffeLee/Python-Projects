import random


def NIM(nim_state = {'a':10 , 'b':10 , 'c':10}):
    move = input ("your move: ").split()
    try : 
        move_letter = str(move[0])
        move_number = int(move [1])
        if nim_state[move_letter] >= move_number and move_number > 1: 
            math_result (move_number, move_letter, nim_state)
        

    except : 
        print('Try again.')

def math_result (move_number, move_letter, nim_state)  :  
    nim_state[move_letter]  =  10-move_number 
    print ('\nremoving ', move_number, " from ", move_letter, "gives\n")
    print("NIM State ", nim_state)
       
NIM ()
