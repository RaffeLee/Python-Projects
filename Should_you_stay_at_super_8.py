import random
def getAnswer(myNumber):
    if myNumber == 1:
        return 'It is certain'
    elif myNumber == 2:
        return 'I suppose so'
    elif myNumber == 3:
        return 'Yes!'
    elif myNumber == 4:
        return 'Hmm try again'
    elif myNumber == 5:
        return 'Check back later'
    elif myNumber == 6:
        return 'Concentrate and try again'
    elif myNumber == 7:
        return 'I would say neigh'
    elif myNumber == 8:
        return 'Bad Outlook there'
    elif myNumber == 9:
        return 'Much doubt'
myNum = random.randint(1,9)
fortune = getAnswer(myNum)
print(fortune)
