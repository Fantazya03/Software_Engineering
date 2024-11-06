# Тема 9. ООП на Python: концепции, принципы и примеры реализации
Отчет по Теме #9 выполнил:
- Даяна Баянова Салаватовна
- АИС-22-1

| Задание    | Лаб_раб | Сам_раб |
|------------|---------|---------|
| Задание 1  | +       | +       |
| Задание 2  | +       | +       |
| Задание 3  | +       | +       |
| Задание 4  | +       | +       |
| Задание 5  | +       | +       |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
```python
class Ivan:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Иван':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Иван"

person1 = Ivan('Алексей')
person2 = Ivan('Иван')
print(person1.name)
print(person2.name)
```
### Результат.

![Меню](images/task1.png)

### Выводы

`__slots__ = ['name']` параметры класса

## №2
```python
class Icecream:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}")
        else:
            print("Обычное мороженое")

icecream = Icecream()
icecream.composition()
icecream = Icecream('шоколадом')
icecream.composition()
icecream = Icecream(5)
icecream.composition()
```
### Результат.

![Меню](images/task2.png)

### Выводы

 проверяем, что переменная относится к стринг

## №3

```python
class MyClass:
    def __init__(self, value):
        self._value = value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        if hasattr(self, '_value'):
            return self._value
        else:
            return "value удалено"

    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value, "Свойство value")

obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj.del_value()
print(obj.get_value())
```
### Результат.

![Меню](images/task3.png)

### Выводы

Создали для класса геттер и сеттер, а также функцию удаления значения
Ошибка выводилась тк мы пытались выводить удаленное значение
  
## №4

```python
class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'

class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'

dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")
cat = Cat()
print(f"Dog is {cat.className}, but they say {cat.sounds}")
```
### Результат.

![Меню](images/task4.png)

### Выводы

создаем класс млекопитающие и два его наследника кошку и собаку

## №5



```python
class Russian:
    @staticmethod
    def greeting():
        print("Привет")

class English:
    @staticmethod
    def greeting():
        print("Hello")

def greet(language):
    language.greeting()

ivan = Russian()
greet(ivan)
john = English()
greet(john)
```
### Результат.

![Меню](images/task5.png)

### Выводы
Использовали статичные методы

## Задания для самостоятельного выполнения: Задание Садовник и помидоры.


```python
class Tomato:
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(index) for index in range(num_tomatoes)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    @staticmethod
    def knowledge_base():
        print("Справка по садоводству: ухаживайте за растениями, чтобы они созревали. "
              "Собирайте урожай только, когда все плоды созрели.")

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(f"{self.name} ухаживает за растением.")
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print("Все томаты созрели. Садовник собирает урожай.")
            self._plant.give_away_all()
        else:
            print("Томаты еще не созрели! Пожалуйста, продолжайте ухаживать за растением.")


Gardener.knowledge_base()

bush = TomatoBush(5)
gardener = Gardener("Иван", bush)

gardener.work()
gardener.work()

gardener.harvest()

gardener.work() 
gardener.harvest()
```
### Результат.

![Меню](images/test1.png)
![Меню](images/test2.png)
![Меню](images/test3.png)
![Меню](images/test4.png)
![Меню](images/test5.png)

### Выводы

Класс Tomato
Этот класс моделирует отдельный томат с его состояниями.

Атрибут states: Это словарь, который описывает возможные состояния томата:

0: "отсутствует" (томата нет),
1: "цветение" (томат только начал расти),
2: "зеленый" (томат растет, но еще не зрелый),
3: "красный" (томат созрел).
Метод __init__(self, index): Конструктор класса, который инициализирует объект томата с индексом (для различия между томатами) и состоянием по умолчанию, равным 0 (отсутствует).

Метод grow(self): Этот метод симулирует рост томата. Если его состояние меньше 3 (не созревшее), то оно увеличивается, переходя через стадии "цветение", "зеленый" и, в конечном итоге, "красный" (созревший).

Метод is_ripe(self): Этот метод проверяет, созрел ли томат (его состояние равно 3). Возвращает True, если томат созрел, и False в противном случае.

Класс TomatoBush
Этот класс моделирует куст с несколькими томатами.

Метод __init__(self, num_tomatoes): Конструктор принимает количество томатов (num_tomatoes), создавая список объектов класса Tomato. Каждый томат инициализируется с уникальным индексом.

Метод grow_all(self): Этот метод вызывает метод grow для каждого томата в кусте, тем самым заставляя все томаты расти.

Метод all_are_ripe(self): Этот метод проверяет, созрели ли все томаты на кусте. Он использует функцию all, которая возвращает True, если все томаты созрели (их состояние равно 3), и False в противном случае.

Метод give_away_all(self): Этот метод удаляет все томаты с куста, симулируя сбор урожая.

Класс Gardener
Этот класс моделирует садовника, который ухаживает за растением.

Метод knowledge_base(): Статический метод, который выводит справку по садоводству, давая советы по уходу за растениями и сбору урожая.

Метод __init__(self, name, plant): Конструктор, который инициализирует садовника с его именем и растением (кустом с томатами). Здесь объект садовника ассоциируется с конкретным кустом томатов.

Метод work(self): Этот метод симулирует работу садовника. Он заставляет садовника ухаживать за растением, вызывая метод grow_all() у растения (когда садовник ухаживает за растением, все томаты начинают расти).

Метод harvest(self): Этот метод позволяет садовнику собрать урожай. Он проверяет, созрели ли все томаты (с помощью метода all_are_ripe()), и если все томаты созрели, то собирает урожай, вызывая метод give_away_all(). Если томаты еще не созрели, выводится сообщение о том, что нужно продолжать ухаживать за растением.

Пример использования:
Создание садовника и куста с томатами: Сначала создается куст с пятью томатами (TomatoBush(5)), затем создается садовник по имени Иван, который будет ухаживать за этим кустом.

Уход за растением: Садовник дважды выполняет работу (gardener.work()), что заставляет все томаты расти.

Сбор урожая: После того, как садовник дважды поработал, он пытается собрать урожай. Если все томаты созрели, урожай будет собран; если нет — садовник получит уведомление о том, что томаты еще не созрели.


## Общие выводы по теме
Повторили основы ООП применили их на практике в самостоятельной работе.
