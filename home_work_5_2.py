# number1 = int(input('Введіть перше число: '))
# number2 = int(input('Введіть друге число: '))
# action = input('Введіть дію(+, -, *, /) : ')

i = 'Y'
while i == 'Y':
    number1 = int(input('Введіть перше число: '))
    number2 = int(input('Введіть друге число: '))
    action = input('Введіть дію(+, -, *, /) : ')
    if action == '+':
        print(number1 + number2)
    elif action == '-':
        print(number1 - number2)
    elif action == '*':
        print(number1 * number2)
    elif action == '/':
        if number2 != 0:
            print(number1 / number2)
        else:
            print('Дільник не може дорівнювати 0!')
    else:
         print('Не вірно введено дію')
    i = input('Щоб продовжити натисніть "Y" на клавіатурі: ')