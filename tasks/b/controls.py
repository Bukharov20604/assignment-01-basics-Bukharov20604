"""
Вам даны три переменные x, y и s, в которые записаны два случайных целых числа и
случайная строка длины 30, соответственно.

Выведите по очереди:
- сами x, y и s через пробел
    > уже написано за вас
- [a] сколько целых чисел находятся строго между x и y по значению
- [b] количество шагов в гипотезе Коллатца, необходимое, чтобы получить из x единицу
    > если число x четное, оно заменяется половину от себя
    > если число x нечетное, оно заменяется на 3x + 1
- [c] количество гласных букв ('a', 'e', 'i', 'o', 'u', 'y') в строке s
"""

from test.common.context import get_integer, get_string

x = get_integer()
y = get_integer()
s = get_string()

print(x, y, s)

def between(lst, x, y):
    count = 0
    for i in lst:
        if x < i < y
            count+=1
    return count
counter = 0
while x != 1:
x = 3 * x + 1 if x % 2 else x // 2
counter += 1
print(counter)
a = (s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") + s.count("y"))
print(a)
