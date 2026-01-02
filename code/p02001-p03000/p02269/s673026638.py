#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


def h1(key):
    return key % m


def h2(key):
    return 1 + (key % (m - 1))


def h(key, i):
    return (h1(key) + i * h2(key)) % m


def insert(T, key):
    i = 0
    while True:
        j = h(key, i)
        if T[j] == 'NULL':
            T[j] = key
            return j
        else:
            i += 1


def search(T, key):
    i = 0
    while True:
        j = h(key, i)
        if T[j] == key:
            print('yes')
            return j
        elif T[j] == 'NULL' or i >= m:
            print('no')
            return 'NULL'
        else:
            i += 1


def str_to_key(_str):
    _length = len(_str)
    _sum, p = 0, 1
    for i in range(_length):
        _sum += p * (ord(_str[i]) - 64)
        # why choose p=5 ?
        p *= 5

    # key = sum([ord(each) - 64
    #            for each in _str])
    # print(key, _str)
    return _sum


def action(command, content):
    key = str_to_key(content)
    if command[0] == 'i':
        insert(T=T, key=key)
    elif command[0] == 'f':
        search(T=T, key=key)
    return None


if __name__ == '__main__':
    _input = sys.stdin.readlines()
    m = 1046527
    length = int(_input[0])
    command_list = list(map(lambda x: x.split(), _input[1:]))
    T = ['NULL' for _ in range(m)]
    for command, content in command_list:
        action(command=command, content=content)