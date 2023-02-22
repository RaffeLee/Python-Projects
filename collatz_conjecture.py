#This takes the number and does something for even or odd cases
#This function is based off of the collatz conjecture
def collatz(number):

#when even, the function divides the number by 2 and returns that value
    if number % 2 == 0:
        print(number // 2)
        return number // 2

#when odd, the function multiplies by 3 and adds one then returns that value
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

#user input for beginning value to be checked even or odd then processed until 1
n = input("Please provide an integer:  ")
while n != 1:
    n = collatz(int(n))




