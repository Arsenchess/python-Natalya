# -*- coding: utf-8 -*-
"""6_2_string_operator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PeYKhON7nfEqPPuaFUic-KFOSNJbBq40

# В Python строковый тип данных имеет название str (сокращение от string — струна, ряд).
"""

s1 = 'Python rocks!'
s2 = "Python rocks!"

# s = input()  # переменная s имеет строковый тип str

# s1 = ''   # пустая строка
# s2 = ' '  # строка состоящая из одного символа пробела

#Не стоит путать пустую строку и строку состоящую из одного символа пробела. Это абсолютно разные строки.

"""# Длина строки
## Длиной строки называется количество символов из которых она состоит.
## Чтобы посчитать длину строки используем встроенную функцию len() (от слова length – длина).
"""

s1 = 'abcdef'
length1 = len(s1) # считаем длину строки из переменной s1
length2 = len('Python rocks!')  # считаем длину строкового литерала
print(length1)
print(length2)

"""## При подсчете длины строки считаются все символы, включая пробелы.

# Преобразование чисел в строку
## Для преобразования строки к числу мы использовали функции int() и float().
## Для обратного преобразования, то есть из числа в строку мы используем функцию str():
"""

num1 = 1777    # целое число
num2 = 17.77   # число с плавающей точкой
s1 = str(num1) # преобразовали целое число в строку '1777'
s2 = str(num2) # преобразовали число с плавающей точкой в строку '17.77'

"""## Иногда работать со строками намного проще, чем с числами. Даже если в условии задачи сказано, что дается число, нам ничто не мешает работать с ним как со строкой.

# Конкатенация строк
## Строки, как и числа, можно складывать. Операция сложения строк называется конкатенацией или сцеплением.
"""

s1 = 'ab' + 'bc'
s2 = 'bc' + 'ab'
s3 = s1 + s2 + '!!'
print(s1)
print(s2)
print(s3)

"""# Операция сложения строк в отличие от операции сложения чисел не является коммутативной, то есть, от перестановки мест слагаемых-строк результат меняется!
## С помощью конкатенации строк можно эмулировать вывод данных, который раньше мы делали используя необязательные параметры sep и end.
## Следующие две строки кода делают одно и то же:
"""

print('a', 'b', 'c', sep='*', end='!')
print()  # переход на новую строку
print('a' + '*' + 'b' + '*' + 'c' + '!')

"""# Умножение строки на число
## В Python также можно умножать строку на число. Такой оператор повторяет строку указанное количество раз.
"""

s = 'Hi' * 4
print(s)

"""# Оператор умножения строки на число (repetition) очень удобен на практике. Например, мы хотим распечатать строку состоящую из 75 символов -. Мы можем это сделать с помощью кода:"""

print('-' * 75)

"""## Строку можно умножать на число, но нельзя умножать на строку.

# Тройные кавычки в Python используются для многострочного (multiline) текста.
"""

text = '''Python is an interpreted, high-level, general-purpose programming language.
Created by Guido van Rossum and first released in 1991, Python design
philosophy emphasizes code readability with its notable use of significant whitespace.'''
print(text)

s1 = 'Мы можем использовать в одиночных кавычках двойные кавычки "Война и мир"'
s2 = "Мы можем использовать в двойных кавычках одиночные кавычки 'Война и мир'"
print(s1)
print(s2)

mystr = 'да'
mystr = mystr + 'нет'
mystr = mystr + 'да'
print(mystr)

str1 = '1'
str2 = str1 + '2' + str1
str3 = str2 + '3' + str2
str4 = str3 + '4' + str3
print(str4)

mystr = '123' * 3 + '456' * 2 + '789' * 1
print(mystr)

# напишите программу, которая выводит текст:
# "Python is a great language!", said Fred. "I don't ever remember
# having this much fun before."
#Примечание. Используйте конкатенацию строк.
print('"Python is a great language!"' + ', said Fred.' + ' "' +
      "I don't ever remember having this much fun before." + '"')

s1 = '"Python is a great language!", said Fred. '
s2 = '"I don'
s3 = "'"
s4 = 't ever remember having this much fun before."'

res = s1 + s2 + s3 + s4
print(res)

print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')

firstname = input()
lastname = input()
print('Hello '+ firstname + ' '+ lastname +'! ' + 'You have just delved into Python')

# длина строки тоже целое число. И нужен обязательный перевод в строку)
footballname = input()
lenght1 = str(len(footballname))
print('Футбольная команда '+ footballname + ' имеет длину ' + lenght1 + ' символов')

"""# Задача Три города
Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
Формат входных данных
На вход программе подаётся названия трех городов, каждое на отдельной строке.
Формат выходных данных
Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.
Примечание. Гарантируется, что длины названий всех трех городов различны.
Тестовые данные 🟢














Sample Input 1:
Москва
Санкт-Петербург
Екатеринбург
Sample Output 1:
Москва
Санкт-Петербург
Sample Input 2:
Нью-Йорк
Вашингтон
Чикаго
Sample Output 2:
Чикаго
Вашингтон
Sample Input 3:
Париж
Марсель
Лион
Sample Output 3:
Лион
Марсель
"""

city1 = input()
city2 = input()
city3 = input()
length1 = len(city1)
length2 = len(city2)
length3 = len(city3)
a = max(length1, length2, length3)
b = min(length1, length2, length3)
if b == length1:
    print(city1)
elif b == length2:
    print(city2)
elif b == length3:
    print(city3)
if a == length1:
    print(city1)
elif a == length2:
    print(city2)
elif a == length3:
    print(city3)

"""# Задача Арифметические строки
Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.

Формат входных данных
На вход программе подаются три строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, «NO» в ином случае.

Примечание. Почитать про арифметическую прогрессию можно по ссылке.

Тестовые данные 🟢
Sample Input 1:

abc
a
abcde
Sample Output 1:

YES
Sample Input 2:

2434
90099
21
Sample Output 2:

NO
Sample Input 3:

aaaaaaaaaa10
1111111Nm
22222r
Sample Output 3:

YES
"""

a = len(input())
b = len(input())
c = len(input())
d = min(a, b, c)
e = max(a, b, c)
f = (a+b+c) - d - e
if e - f == f - d:
    print('YES')
else:
    print('NO')

a = len(input())
b = len(input())
c = len(input())
if ((a + b + c)%3) == 0:
    print('YES')
else:
    print('NO')

"""# Оператор in
В Python есть специальный оператор in, который позволяет проверить, что одна строка находится внутри другой.
"""

s = input()
if 'a' in s:
    print('Введенная строка содержит символ а')
else:
    print('Введенная строка не содержит символ а')

s = input()
if '.' not in s:
    print('Введенная строка не содержит символа точки')
else:
    print('Содержит')

# С помощью оператора in мы можем упростить следующий код, проверяющий,
# что в переменной s находится один из 5 символов a, e, i, o, u:
s = input()
if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
    print('YES')
else:
    print('NO')

# if len(s) == 1 and s in 'aeiou':
    print('YES')

"""## Если строка s1 содержится в строке s2, то говорят, что строка s1 является подстрокой для строки s2. Другими словами, оператор in определяет является ли одна строка подстрокой другой.

# Задача Цвет настроения синий
Напишите программу, которая считывает одну строку, после чего выводит «YES», если во введенной строке есть подстрока «синий» и «NO» - в противном случае.
Формат входных данных
На вход программе подается одна строка.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Примечание. Учитывайте регистр при поиске подстроки «синий».
Тестовые данные 🟢
Sample Input 1:
Какой хороший день!
Sample Output 1:
NO
Sample Input 2:
Как называется этот красивый синий камень в Вашем кольце?
Sample Output 2:
YES
Sample Input 3:
Разглядите синий густой цвет.
Sample Output 3:
YES
"""

s = input()
if 'синий' in s:
    print('YES')
else:
    print('NO')

"""# Отдыхаем ли?
Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.
Формат входных данных
На вход программе подается одна строка.
Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.
Тестовые данные 🟢
Sample Input 1:
Какой сегодня день недели?
Sample Output 1:
NO
Sample Input 2:
Была суббота, и ему хотелось поскорее уехать домой.
Sample Output 2:
YES
Sample Input 3:
День в воскресенье выдался тёплым и солнечным.
Sample Output 3:
YES
"""

s = input()
if 'суббота' in s or 'воскресенье' in s:
    print('YES')
else:
    print('NO')

"""# Задача Корректный email
Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую корректность email адреса.
Формат входных данных
На вход программе подаётся одна строка – email адрес.
Формат выходных данных
Программа должна вывести строку «YES», если email адрес является корректным и «NO» в ином случае.
Примечание. Наличие символов @ и . недостаточно для корректности email адреса, однако их отсутствие гарантировано влечёт за собой неверный email.
Тестовые данные 🟢
Sample Input 1:
aaaa@bbb.com
Sample Output 1:
YES
Sample Input 2:
aaaa@bbbcom
Sample Output 2:
NO
Sample Input 3:
qwerty.com
Sample Output 3:
NO
"""

email = input()
if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')