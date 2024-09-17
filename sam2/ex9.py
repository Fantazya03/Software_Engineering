import random

a = int(input("угадайте число от 0 до 5: "))
b = random.randint(0,5)
if a==b:
    print("вы угадали")
else:
    print("вы не угадали")
