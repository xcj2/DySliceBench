from sys import stdin
from collections import deque
from copy import deepcopy


class State:
    def dup(self):
        ns = State()
        ns.b = self.b[:]
        ns.z = self.z
        ns.c = self.c
        return ns


def read_board():
    s = State()
    s.b = [int(x) for x in stdin.read().split()]
    s.z = s.b.index(0)
    s.c = 0
    return s


def move_zero(s, h):
    ns = s.dup()
    ns.z += h
    ns.b[s.z], ns.b[ns.z] = ns.b[ns.z], ns.b[s.z]
    ns.c += 1
    return ns


def push_hands(q, s):
    if s.z % 3 != 0:
        q.append(move_zero(s, -1))
    if s.z % 3 != 3 - 1:
        q.append(move_zero(s, 1))
    if s.z // 3 != 0:
        q.append(move_zero(s, -3))
    if s.z // 3 != 3 - 1:
        q.append(move_zero(s, 3))


def solve(s):
    hist = set()
    q = deque([])
    while True:
        t = tuple(s.b)
        if t == (1, 2, 3, 4, 5, 6, 7, 8, 0):
            return s.c
        if t not in hist:
            push_hands(q, s)
            hist.add(t)
        s = q.popleft()


def main():
    b = read_board()
    print(solve(b))


main()

