#!/usr/bin/env python3
import sys
from statistics import median


def count_steps(numbers):
    target_number = int(median(numbers))
    return sum(map(lambda x: abs(target_number - x), numbers))


if __name__ == '__main__':
    numbers_file = sys.argv[1]

    with open(numbers_file) as file:
        numbers = list(map(int, file.read().split()))

    print(count_steps(numbers))
