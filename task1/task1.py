#!/usr/bin/env python3
import sys
from math import lcm


def calc_path(interval, step):
    step -= 1
    if step == 0:
        return [1] if interval == 1 else []

    path_length = lcm(interval, step) // step
    path = [i * step % interval + 1 for i in range(path_length)]
    return path


if __name__ == '__main__':
    interval, step = map(int, sys.argv[1:3])
    print(*calc_path(interval, step), sep='')
