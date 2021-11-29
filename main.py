import re

print('Добро пожаловать в игру!')
print('Правила игры очень простые: загадайте число от 1 до 100, запишите его себя на листочке.')
print('Компьютер попробует у вас его отгадать, предлагая числа, ваша задача в ответ вводить:')
print('  знак >, если число, которое предлагает компьютер, больше вашего числа')
print('  знак <, если число, которое предлагает компьютер, меньше вашего числа')
print('  знак =, если число, которое предлагает компьютер, совпадает с вашим числом')
print('Приступаем!')

minRange = 1
maxRange = 100
result = None
inputString = None

while not inputString=='=':
    result = ((maxRange - minRange) // 2) + minRange
    print('Предлагаю такое число: ',result)
    while True:
        inputString = input('Введите ">" или "<" или "=": ')
        if not re.search('[=<>]', inputString):
            print('Неверный ввод')
        else:
            break
    if inputString=='>':
        maxRange = result
    else:
        minRange = result

print('Я угадал! Число: ', result)


