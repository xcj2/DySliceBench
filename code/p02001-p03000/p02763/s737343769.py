import math
n = int(input())
s = input()
ss = [[(1 << ord(c) - ord('a')) for c in s]]
while len(ss[-1]) > 1:
    r = []
    for i in range(0, len(ss[-1]), 2):
        if i + 1 < len(ss[-1]):
            r.append(ss[-1][i] | ss[-1][i + 1])
        else:
            r.append(ss[-1][i])
    ss.append(r)
#print(ss)

def update(j, v):
    ss[0][j] = v
    for k in range(1, len(ss)):
        j = j // 2
        #print('k=', k, 'j=', j)
        if 2 * j + 1 < len(ss[k - 1]):
            ss[k][j] = ss[k - 1][2 * j] | ss[k - 1][2 * j + 1]
        else:
            ss[k][j] = ss[k - 1][2 * j]
    #print('j=', j, 'v=', v, 'ss=', ss)

def all_or(i, j, k):
    #print('all_or(', i, j, k, ')')
    if i == j:
        return 0
    while True:
        if k == 0:
            return ss[0][i]
        ik, jk = (i >> k), (j >> k)
        #print('i=', i, 'j=', j, 'k=', k, 'ik=', ik, 'jk=', jk)
        if ik != jk:
            break
        k -= 1
    r = 0
    if i == ik << k:
        r = ss[k][ik]
    else:
        r = all_or(i, (ik + 1) << k, k - 1)
    for l in range(ik + 1, jk):
        r |= ss[k][l]
    r |= all_or(jk << k, j, k - 1)
    return r

def popcount(v):
    r = 0
    while v != 0:
        v = (v & (v - 1))
        r += 1
    return r

q = int(input())

for i in range(q):
    cs = [x for x in input().split()]
    cs[0], cs[1] = int(cs[0]), int(cs[1]) - 1
    if cs[0] == 1:
        #print('cs[2]=', cs[2], 'mask=', 1 << (ord(cs[2]) - ord('a')))
        update(cs[1], (1 << (ord(cs[2]) - ord('a'))))
    else:
        #print('all_or(', cs[1], int(cs[2]), ')=',all_or(cs[1], int(cs[2]), len(ss) - 1))
        #r = 0
        #for j in range(cs[1], int(cs[2])):
        #    r |= ss[0][j]
        print(popcount(all_or(cs[1], int(cs[2]), len(ss) - 1)))
        #print(popcount(r))

