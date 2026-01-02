#!usr/bin/env python3

import sys


def generate_buidlings(building, floor, room):
    empty_buildings = {
            key: [[0 for col in range(room)] for row in range(floor)]
            for key in range(1, building+1)
    }
    return empty_buildings


def occupy_buildings(empty_buildings):
    occupied_buildings = generate_buidlings(4, 3, 10)
    n = int(sys.stdin.readline())

    for i in range(n):
        lst = [int(num) for num in sys.stdin.readline().split()]
        occupied_buildings[lst[0]][lst[1]-1][lst[2]-1] += lst[3]

    return occupied_buildings


def print_residents():
    separator = '####################'
    occupied_buildings = occupy_buildings(generate_buidlings(4, 3, 10))

    for idx, (key, value) in enumerate(occupied_buildings.items()):
        for floor in value:
            print(' %s %s %s %s %s %s %s %s %s %s' % tuple(floor))
        if idx < 3:
            print(separator)


def main():
    print_residents()


if __name__ == '__main__':
    main()