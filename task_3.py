"""
Мы сохраняем время присутствия каждого пользователя на уроке в виде интервалов. В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах):

lesson – начало и конец урока
pupil – интервалы присутствия ученика
tutor – интервалы присутствия учителя
Интервалы устроены следующим образом – это всегда список из четного количества элементов. Под четными индексами (начиная с 0) время входа на урок, под нечетными - время выхода с урока.
Нужно написать функцию, которая получает на вход словарь с интервалами и возвращает время общего присутствия ученика и учителя на уроке (в секундах).
"""

from collections import namedtuple
from functools import reduce


def get_uniq_intervals(intervals):
    intervals = tuple(sorted(intervals, key=(lambda x: (x.start, x.end))))
    uniq_intervals = []
    start = intervals[0].start
    end = intervals[0].end
    for interval in intervals[1:]:
        if interval.start < end < interval.end:
            end = interval.end
        elif interval.end <= end:
            continue
        else:
            uniq_intervals.append((Range(start, end)))
            start = interval.start
            end = interval.end
    if Range(start, end) not in uniq_intervals:
        uniq_intervals.append(Range(start, end))
    return uniq_intervals


def intersect(range1, range2):
    new_range = Range(
        max(range1.start, range2.start),
        min(range1.end, range2.end)
    )
    return new_range if new_range.start < new_range.end else None


def intersect_two(ranges1, ranges2):
    for range1 in ranges1:
        for range2 in ranges2:
            intersection = intersect(range1, range2)
            if intersection:
                yield intersection


def intersect_all(ranges):
    return reduce(intersect_two, ranges)


def appearance(intervals):
    times_list = []

    lesson_intervals = tuple(
        Range(start=(intervals['lesson'][i]),
              end=(intervals['lesson'][i + 1]))
        for i in range(0, len(intervals['lesson']), 2)
    )
    pupil_intervals = tuple(
        Range(start=(intervals['pupil'][i]),
              end=(intervals['pupil'][i + 1]))
        for i in range(0, len(intervals['pupil']), 2)
    )
    tutor_intervals = tuple(
        Range(start=(intervals['tutor'][i]),
              end=(intervals['tutor'][i + 1]))
        for i in range(0, len(intervals['tutor']), 2)
    )

    times_list.append(get_uniq_intervals(lesson_intervals))
    times_list.append(get_uniq_intervals(pupil_intervals))
    times_list.append(get_uniq_intervals(tutor_intervals))
    return (sum(intersection.end - intersection.start for intersection in
                intersect_all(times_list)))


Range = namedtuple("Range", ["start", "end"])

tests = [
    {'data': {'lesson': [1594663200, 1594666800],
              'pupil': [1594663340, 1594663389, 1594663390, 1594663395,
                        1594663396, 1594666472],
              'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
     },
    {'data': {'lesson': [1594702800, 1594706400],
              'pupil': [1594702789, 1594704500, 1594702807, 1594704542,
                        1594704512, 1594704513, 1594704564, 1594705150,
                        1594704581, 1594704582, 1594704734, 1594705009,
                        1594705095, 1594705096, 1594705106, 1594706480,
                        1594705158, 1594705773, 1594705849, 1594706480,
                        1594706500, 1594706875, 1594706502, 1594706503,
                        1594706524, 1594706524, 1594706579, 1594706641],
              'tutor': [1594700035, 1594700364, 1594702749, 1594705148,
                        1594705149, 1594706463]},
     'answer': 3577
     },
    {'data': {'lesson': [1594692000, 1594695600],
              'pupil': [1594692033, 1594696347],
              'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
     'answer': 3565
     },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
        test_answer = appearance(test['data'])
        assert test_answer == test[
            'answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
