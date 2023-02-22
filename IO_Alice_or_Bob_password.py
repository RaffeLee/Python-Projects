name = input('Are you Bob or Alice?\n')


if name == 'Alice':
    age = int(input('How old are you...Alice?\n'))
if name == 'Bob':
    print ('How is it hanging B0b?')
elif age == 69:
    print('I\'ve been hard at work fending off these imposters!')
elif age < 12:
    print('You are not Alice, kiddo')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100 and age<129:
    print('You are not Alice granny')
else :
    print('Maybe next time sugarplum ;)')
