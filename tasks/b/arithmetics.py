"""
Вам даны три переменные x, y и z, в которые записаны два случайных целых и
одно случайное вещественное число, соответственно.

В этом задании вам запрещено заводить новые переменные и подключать модули.

Выведите по очереди:
- сами три числа через пробел
    > уже написано за вас
- [a] их сумму
- [b] их произведение
- [c] округленное вверх до целого произведение x и z
- [d] частное x и z
- [e] неполное частное при делении x на z
- [f] остаток от деления x на y
- [g] y в степени z
- [h] куб произведения трех их попарных сумм
- [i] число z с ровно пятью знаками после точки
    > подсказка: используйте форматную строку (f-string)

Запишите в переменную FLOATS, сколько среди пунктов [a]-[h] нецелых результатов
в смысле type(результата) == float.
"""

from test.common.context import get_integer, get_float  # не обращайте внимание

x = get_integer()
y = get_integer()
z = get_float()

print(x, y, z)  # 567 8 5454.42343248234
print((x + y + z))
print( x*y*z)
print(round(x*y))
print( x //z)
print(x % y)
print( y**z)
print(((x+y)*(x+z)*(z+y))**3)
print("{0:.5f}".format(z))
FLOATS = 6