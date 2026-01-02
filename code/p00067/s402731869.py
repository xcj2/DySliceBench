def f1():
    t = 0
    for y, line in enumerate(M):
        for x, cell in enumerate(line):
            if M[y][x] == '1':
                f2(x, y)
                t += 1
    return t


def f2(x, y):
    if x < 0 or len(M[0]) == x or y < 0 or len(M) == y:
        return
    if M[y][x] == '1':
        M[y][x] = '0'
        for i in range(4):
            if i == 0:  # U
                f2(x, y-1)
            elif i == 1:  # D
                f2(x, y+1)
            elif i == 2:  # R
                f2(x+1, y)
            elif i == 3:  # L
                f2(x-1, y)


def get_input():
    while True:
        try:
            yield input()
        except EOFError:
            break
            

M = []
for line in list(get_input()):
    if line == '':
        print(f1())
        M = []
    else:
        M.append(list(line))
print(f1())