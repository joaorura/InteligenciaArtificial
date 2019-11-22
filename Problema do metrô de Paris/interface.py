from data import graph


def start():
    a = int(input('Initial station: '))
    if a not in graph['stations']:
        raise ValueError()

    b = input('Initial Line: ')
    if b not in graph['colors']:
        raise ValueError()

    c = int(input('Final station: '))
    if c not in graph['stations']:
        raise ValueError()

    return a, b, c
