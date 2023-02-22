import random


def NIM(nim_state = {'a':10 , 'b':10 , 'c':10}):
    move = input ("your move: ").split()
    try : 
        move_letter = str(move[0])
        move_number = int(move [1])
        
    except : 
        print('Try again.')
    

NIM ()
