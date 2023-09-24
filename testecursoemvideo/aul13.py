for num in range(1, 11):
    print(' ')
    for c in range(1, 11):
        if num != 3 and c != 3:
            print('{} x {} = {}'.format(num, c, (num*c)))
        else:
            print('Censurado!')

