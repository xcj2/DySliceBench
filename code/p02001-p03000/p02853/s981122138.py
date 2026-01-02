
def read_tokens():
    return input().strip().split(' ')

def read_ints():
    return [int(token) for token in read_tokens()]

def solve(b, n):
    ret = []
    while len(b) > 0:
        # print(b)
        c = None
        for i in reversed(range(len(b))):
            if b[i] > i + 1:
                return [-1]
            if b[i] == i + 1:
                c = b[:i] + b[i+1:]
                ret.append(b[i])
                break
        if c is None:
            return [-1]
        b = c
    return list(reversed(ret))

x, y = read_ints()

def f(x):
    if x <= 3:
        return [300000, 200000, 100000][x-1]
    return 0

s = f(x) + f(y)
if x == 1 and y == 1:
    s += 400000

print(s)