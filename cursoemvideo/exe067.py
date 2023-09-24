while True:
    print('-' * 15)
    num = int(input('Quer ver a tabuada de qual valor? '))
    if num <= 0:
        break
    else:
        for c in range(1, 11):
            multi = num * c
            print(f'{num} x {c} = {multi}')
    print('-' * 15)
print('Fim')
print('-' *15)