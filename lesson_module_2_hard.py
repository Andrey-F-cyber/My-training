def password(number):
    if number > 20:
            print('это число превышает 20')
    a = ''
    for i in range(1, number):
        for j in range(i + 1, number):

            if number % (i + j) == 0:
                a = a + str(i) + str(j)
    return a

print('Введите число от 3 до 20: ')
print(password(int(input())))















