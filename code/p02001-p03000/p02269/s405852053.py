# -*- coding:utf-8 -*-
import sys


class Hash(object):
    def __init__(self, size):
        self._array = [None] * size
        self._size = size

    def _hash(self, key):
        return key % self._size

    def insert(self, key, value):
        j = self._hash(key)
        if self._array[j] is None:
            self._array[j] = [value]
        else:
            self._array[j].append(value)

    def find(self, key, value):
        j = self._hash(key)
        if self._array[j] is None:
            return False
        elif value in self._array[j]:
            return True
        else:
            return False


def stoi(s):
    ret = 0
    p = 1
    ctoi = {"A": 1, "C": 2, "G": 3, "T": 4}
    for c in s:
        ret += ctoi[c] * p
        p *= 7
    return ret


def dictionary(lst):
    h = Hash(1046527)
    ret = []
    for val in lst:
        if val[0] == "insert":
            h.insert(stoi(val[1]), val[1])
        elif val[0] == "find":
            if h.find(stoi(val[1]), val[1]):
                ret.append("yes")
            else:
                ret.append("no")
        else:
            raise ValueError
    return ret


if __name__ == "__main__":
    lst = [val.split() for val in sys.stdin.read().splitlines()]
    n = int(lst.pop(0)[0])
    print("\n".join(dictionary(lst)))