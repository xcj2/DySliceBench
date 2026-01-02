
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

n, = read_ints()
b = read_ints()

ans = solve(b, n)
print('\n'.join(str(x) for x in ans))