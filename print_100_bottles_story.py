for i in range(99,0,-1):
        if i == 1:
                print('1 more bottle of beer on the wall, only one bottle of beer!')
                print('So I TAKE it DOWN pass it aROUND, no more bottles of beer on the wall!')
        elif i == 2:
                print('2 more bottle of beer on the wall, only bottles of beer')
                print('So I take one down, pass it around, one more bottle of beer on the wall')
        else:
            print('{0} bottles of beer on the wall, {0} bottles of beer!'.format(i))
            print('So I take one down, pass it around, {0} more bottle of beer on the wall'.format(i-1))
            
            
