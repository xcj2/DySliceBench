
import sys
from collections import deque


def input(): return sys.stdin.readline().strip()


def insert(x, l):
    l.appendleft(x)


def delete(x, l):
    if len(l) == 0:
        return
    index = l.index(x) if x in l else None
    if index is None:
        return
    else:
        l.remove(x)


def delete_first(l):
    if len(l) == 0:
        return
    l.popleft()


def delete_last(l):
    if len(l) == 0:
        return
    l.pop()


n = int(input())
l = deque()

for _ in range(n):
    command = input().split(' ')

    if command[0] == 'insert':
        insert(command[1], l)

    elif command[0] == 'delete':
        delete(command[1], l)

    elif command[0] == 'deleteFirst':
        delete_first(l)

    elif command[0] == 'deleteLast':
        delete_last(l)

print(' '.join(l))

