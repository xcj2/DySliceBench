p = list(map(int, list(input())))
def add(x,y,s):
    if s == 0: return x+y
    else: return x-y
def bittolist(x):
    ret = []
    for _ in range(3):
        ret.append(x%2)
        x //= 2
    return ret
def pm(s):
    if s == 0:
        return '+'
    else: return '-'
for i in range(8):
    s = bittolist(i)
    res = p[0]
    for j in range(3):
        res = add(res, p[j+1], s[j])
    if res == 7:
        print(p[0], end = '')
        print(pm(s[0]), end = '')
        print(p[1], end = '')
        print(pm(s[1]), end = '')
        print(p[2], end = '')
        print(pm(s[2]), end = '')
        print(p[3], end = '')
        print('=7')
        exit()