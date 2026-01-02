from collections import deque

dll = [[-1,-1, None]]
first = 0
cursor = 0

def insert(x):
    global cursor, first
    dll.append([dll[cursor][0],cursor,x])
    new_cursor = len(dll) - 1
    if dll[cursor][0] != -1:
        dll[dll[cursor][0]][1] = new_cursor
    dll[cursor][0] = new_cursor
    if cursor == first:
        first = new_cursor
    cursor = new_cursor

def move(d):
    global cursor
    if d > 0:
        for _ in range(d):
            cursor = dll[cursor][1]
    elif d < 0:
        for _ in range(-d):
            cursor = dll[cursor][0]

def erase():
    global cursor, first
    if dll[cursor][0] != -1:
        dll[dll[cursor][0]][1] = dll[cursor][1]
    if dll[cursor][1] != -1:
        dll[dll[cursor][1]][0] = dll[cursor][0]
    if cursor == first:
        first = dll[cursor][1]
    cursor = dll[cursor][1]

def main():
    Q = int(input())
    for _ in range(Q):
        query = input().split()
        if query[0] == '0':
            insert(query[1])
        elif query[0] == '1':
            move(int(query[1]))
        elif query[0] == '2':
            erase()

    i = first
    while dll[i][2] != None:
        print(dll[i][2])
        i = dll[i][1]

main()

