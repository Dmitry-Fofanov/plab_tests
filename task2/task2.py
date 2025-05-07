#!/usr/bin/env python3
import sys
from math import isclose


def circle_checker(circle_x, circle_y, radius):
    squared_radius = radius ** 2

    def check_if_inside(x, y):
        x -= circle_x
        y -= circle_y
        squared_distance = x ** 2 + y ** 2
        if isclose(squared_radius, squared_distance):
            return 0
        if squared_distance < squared_radius:
            return 1
        return 2

    return check_if_inside


if __name__ == '__main__':
    circle_file, points_file = sys.argv[1:3]

    with open(circle_file) as file:
        circle_x, circle_y, radius = map(float, file.read().split())

    checker = circle_checker(circle_x, circle_y, radius)
    with open(points_file) as file:
        for line in file:
            split = line.split()
            if len(split) != 2:
                continue
            x, y = map(float, split)
            print(checker(x, y))
