while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)\nYou can give up with "Stop"')
    password = input()
    if password =='swordfish':
        break
    elif password == 'Stop':
        break
print('Access granted.')
