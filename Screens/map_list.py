import random


def enviroment():

    map1 = (
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        (1, 3, 2, 2, 3, 2, 2, 3, 2, 2, 3, 1, 1, 1, 3, 2, 2, 3, 2, 2, 3, 2, 2, 3, 1),
        (1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1),
        (1, 0, 1, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 1, 0, 1),
        (1, 3, 0, 3, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 3, 0, 3, 1),
        (1, 0, 1, 0, 1, 3, 0, 3, 0, 0, 0, 3, 1, 3, 0, 0, 0, 3, 0, 3, 1, 0, 1, 0, 1),
        (1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1),
        (1, 3, 0, 3, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 3, 0, 3, 1),
        (1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1),
        (1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1),
        (1, 3, 0, 3, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 3, 0, 3, 1),
        (1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1),
        (1, 0, 1, 0, 1, 3, 0, 3, 0, 0, 0, 3, 1, 3, 0, 0, 0, 3, 0, 3, 1, 0, 1, 0, 1),
        (1, 3, 0, 3, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 3, 0, 3, 1),
        (1, 0, 1, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 1, 0, 1),
        (1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1),
        (1, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 1, 1, 1, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 1),
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        )
    map2 = (
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        (1, 3, 2, 2, 3, 2, 2, 3, 2, 2, 3, 1, 1, 1, 3, 2, 2, 3, 2, 2, 3, 2, 2, 3, 1),
        (1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1),
        (1, 0, 1, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 1, 0, 1),
        (1, 3, 0, 3, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 3, 0, 3, 1),
        (1, 0, 1, 0, 1, 3, 0, 3, 0, 0, 0, 3, 1, 3, 0, 0, 0, 3, 0, 3, 1, 0, 1, 0, 1),
        (1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1),
        (1, 3, 0, 3, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 3, 0, 3, 1),
        (1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1),
        (1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1),
        (1, 3, 0, 3, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 3, 0, 3, 1),
        (1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1),
        (1, 0, 1, 0, 1, 3, 0, 3, 0, 0, 0, 3, 1, 3, 0, 0, 0, 3, 0, 3, 1, 0, 1, 0, 1),
        (1, 3, 0, 3, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 3, 0, 3, 1),
        (1, 0, 1, 3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 3, 0, 0, 0, 3, 0, 0, 0, 3, 1, 0, 1),
        (1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1),
        (1, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 1, 1, 1, 3, 0, 0, 3, 0, 0, 3, 0, 0, 3, 1),
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        )
    return random.choice((map1, map2))