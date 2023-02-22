import random
 

def main():
    score = 0
    quizzing = True
    while quizzing == True:
        score = binomial_question(score)
        quizzing = keep_quizzing(quizzing, score)

    


def binomial_question(score):
    a = random.randint(-10,10)
    b = random.randint(-10,10)
    c = random.randint(-10,10)
    d = random.randint(-10,10)
    u = a*c ; v = a*d+b*c ; w = b*d

    user_answer = input("Find the product of these two binomials(Don't include spaces, enter exponents as x^2, enter 0 as a coefficient if necessary, and enter subtraction as +-):\n (%dx+%d)*(%dx+%d)\n" % (a,b,c,d) )
    binomial_answer = str("%dx^2+%dx+%d" % (u,v,w))
    if (user_answer == binomial_answer):
        score +=1 
        print('\ncorrect')
    elif (user_answer != binomial_answer):
        print('\nincorrect')

    return score

    
def keep_quizzing(quizzing, score):
    again_answer = input('\nWould you like to keep practicing? (y or n) :')
    if (again_answer == 'y'):
        quizzing = True
    elif (again_answer == 'n'):
        print ('\nYour total score:', score)
        quizzing = False
    return quizzing




main()
