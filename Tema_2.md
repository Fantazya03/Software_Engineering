# Тема 2. Базовые операции языка Python
Отчет по Теме #2 выполнил(а):
- Баянова Даяна Салаватовна
- АИС-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | + |
| Задание 7 | + | + |
| Задание 8 | + | + |
| Задание 9 | + | + |
| Задание 10 | + | + |



знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №2
##1.
  ```python
  print(123)
  print('123')
  print(1.23)
```
Три принта первый число второй строку так как там ковычки и число с плавающей точкой
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/lab2/ex1.png)

##2.
  ```python
  print(1823-486)
  print(5.1 + 8.37)
  print(3+7.04+2.33)
```
Показали как работаю операторы сложения и вычитания с числами и с числами с плавающей точкой
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/lab2/ex2.png)
##3.
  ```python   
  print('Привет, Мир!')
  
  world = 'Мир!'
  print(f"Привет, {world}")
  
  one = 'Привет, '
  two = 'Мир!'
  print(one+two)
```
в первом принте мы просто выводим строку, во втором мы используем f строку которая позволяет использовать переменные в строке для вывода, ну и в третьем мы просто сложили две строковые переменые
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/lab2/ex3.png)
##4.
  ```python
  one = 'hello'
  print(bool(one))
  
  two = 142
  print(float(two))
  
  three = None
  print(str(three))
```

в первом выводе true говорит нам о том что строка one не пуста, вторая переводит переменую two в число с плавющей точкой, в третьем переводит в строку None
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/lab2/ex4.png)
##5.
  ```python
  one = input('one:')
  two = input('two:')
  three = input('three:')
  
  print(one, two, three)
  ```

пользовательский ввод в три переменые затем выводим их
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/lab2/ex5.png)
  
##6.
  ```python
  a =12
  b = 5
  print('Возведение в степеню:', a**b)
  print('Обычное деление:', a/b)
  print('Целочисленное деление:', a//b)
  print('Нахождение остатка деления:', a%b)
```

в первом выводе используем операто** чтобы возвести перменную a в степень b
оператор // целочисленного деления делит без остатка тоесть если будет 10//3 ответ будет 3 остаток 1 отбрасывается
и операто % как раз таки оставляет остаток 10%3 ответ будет 1
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/lab2/ex6.png)
##7.
  ```python
  line = 'Hello!'
  print(line*6)
```

Шесть раз перемножает строку line и выводит ее
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/lab2/ex7.png)
##8.
  ```python
  sentence = 'hello World!'
  print(sentence.count('o'))
```
функция count строковых переменных считает сколько вхождений о в строке
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/lab2/ex8.png)
##9.
  ```python
  print('Hello \nWorld')
```
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/lab2/ex9.png)
##10.
  ```python
  sentence = 'Hello World'
  print(sentence[1])
  print(sentence[:5])
```
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/lab2/ex10.png)
## Самостоятельная работа №2

##1.
  ```python
  str = ''
  print(bool(str))
  ```

так как строка пуста перевод в булевую перемуную покажет false
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/sam2/ex1.png)
##2.
  ```python
  a , b, c = 1, 2, 3
  print(a,b,c)
  ```
можно создавать переменные в одну строку через запятую и также определять их через запятую
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/sam2/ex2.png)
##3.
  ```python
  num = int(input())
  print(num)
  ```
int() перед инпут не даст вписывать строковые значения иначе будетт выдавать ошибку
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/sam2/ex3.png)
##4.
  ```python
  s = input()[:5]
  print(s*16)
  ```
[:5] означает что какая бы строка не была она запомнит только первые 5 символов
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/sam2/ex4.png)
##5.
  ```python
  day, month , year = int(input()),str(input()) ,int(input())
  print(f"Сегодня {day} {month} {year}", end = ' Всего хорошего!')
  ```
в одну строку создаем три переменные через запятую и использую f строку в выводе мы выводим переменные ввиде даты
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/sam2/ex5.png)
##6.
  ```python
  sentence = "Hello World"; print(sentence.replace(" ", " my "))
  ```
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/sam2/ex6.png)
##7.
  ```python
  sentence = "Hello World"
  print("Длина строки:", len(sentence))
  ```
строковая функция len определяет из скольки символов состоит строка
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/sam2/ex7.png)
##8.
  ```python
  sentence = "HELLO WORLD"
  print(sentence.lower())
  ```
строковая функция lower понижает все символы в нижний реестр
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/sam2/ex8.png)
##9.
  написать программу где пользователь старается угадать загаданное число 
  ```python
  import random

a = int(input("угадайте число от 0 до 5: "))
b = random.randint(0,5)
if a==b:
    print("вы угадали")
else:
    print("вы не угадали")
  ```
вводим только число и далее с помощью if else проверяем равно ли случайному числу b
функция randint дает возможность выбрать диапозон из чисел из которых уже будет выбираться случайное
  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/sam2/ex9.png)
##10.
   Нужно вывести три символа с третьего индекса шагом в 1
  ```python
  string = input("Введите строку: ")
print(string[3:6:1])
```
[3:6:1] говорит нам о том что начиная с 4 символа(третьего индекса) до 7 символа (6 индекса) мы выводим сиволы с шагом 1

  ![Меню](https://github.com/Fantazya03/Software_Engineering/blob/Tema_2/sam2/ex10.png)
