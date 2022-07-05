"""
Дан массив чисел, состоящий из некоторого количества подряд идущих единиц, за которыми следует какое-то количество подряд идущих нулей: 111111111111111111111111100000000.
Найти индекс первого нуля (то есть найти такое место, где заканчиваются единицы, и начинаются нули)
"""


def task_1(array: str):
    try:
        index = list(array).index('0') - 1
        return index
    except ValueError:
        return 'Не нашёл нулей'


assert task_1('111111111110000000000000000') == 10

"""
В функцию передаются координаты двух противоположных вершин одного прямоугольника и двух противоположных вершин второго прямоугольника. Найти, пересекаются ли эти прямоугольники?
Немного посложнее – найти площадь пересечения
"""


def task_2(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    ax_coord = (ax1, ax2)
    bx_coord = (bx1, bx2)
    ay_coord = (ay1, ay2)
    by_coord = (by1, by2)
    if any((
            max(ax_coord) < min(bx_coord),
            min(ax_coord) > max(bx_coord),
            max(ay_coord) < min(by_coord),
            min(ay_coord) > max(by_coord))):
        return False
    area = (max(ax_coord) - min(bx_coord)) * (max(ay_coord) - min(by_coord))
    return area
