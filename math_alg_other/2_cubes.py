import random
import pprint


def func_cubes():
    x = random.randint(1, 6) + random.randint(1, 6)
    return x


dict_cubes = {}
for i in range(1000):
    x = func_cubes()
    if x not in dict_cubes:
        dict_cubes[x] = 0.1
    else:
        dict_cubes[x] += 0.1


pprint.pprint(dict_cubes,sort_dicts=True)
