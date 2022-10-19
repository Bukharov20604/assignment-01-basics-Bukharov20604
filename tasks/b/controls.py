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


b = ((abs(x - y) - 1))
print (b)
def collatz(n):
    if n:
         return 0

    while n:
        n = (n/2) if n % 2 else (3 * n +1)
        cnt
    return cnt

print(collatz(n))
a = (s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") + s.count("y"))
print(a)
