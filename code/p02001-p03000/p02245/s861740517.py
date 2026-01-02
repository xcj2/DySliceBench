#!/usr/bin/python3

def get_patten(B):
    return ''.join(map(str, B))

def change_left(index, B):
    C = B.copy()
    C[index], C[index - 1] = C[index - 1], C[index]
    return C

def change_right(index, B):
    C = B.copy()
    C[index], C[index + 1] = C[index + 1], C[index]
    return C

def change_top(index, B):
    C = B.copy()
    C[index], C[index - 3] = C[index - 3], C[index]
    return C

def change_bottom(index, B):
    C = B.copy()
    C[index], C[index + 3] = C[index + 3], C[index]
    return C

# main
boad = []
for i in range(3):
    boad.extend(map(int, input().split()))
exist_patten = set()

q = []
q.append((boad, None, 0))

while len(q) > 0:
    B, prev, count = q.pop(0)
    p = get_patten(B)
    if p in exist_patten:
        continue
    exist_patten.add(p)
    if p == '123456780':
        print(count)
        exit()

    index = B.index(0)

    if index % 3 != 0 and prev != 'right':
        C = change_left(index, B)
        q.append((C, 'left', count + 1))

    if index % 3 != 2 and prev != 'left':
        C = change_right(index, B)
        q.append((C, 'right', count + 1))

    if index >= 3 and prev != 'bottom':
        C = change_top(index, B)
        q.append((C, 'top', count + 1))

    if index <= 5 and prev != 'top':
        C = change_bottom(index, B)
        q.append((C, 'bottom', count + 1))