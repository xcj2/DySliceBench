n = int(input())
s = list(input())
BITs = [[0]*(n+1) for _ in range(26)]

def c_idx(c):
    return ord(c) - 97

def query(pos):
    ret = [0]*26
    for i in range(26):
        tmp = 0
        p = pos
        while p > 0:
            tmp += BITs[i][p]
            p -= p & (-p)
        ret[i] = tmp
    return ret

def update(pos, a, x):
    while pos <= n:
        BITs[a][pos] += x
        pos += pos & (-pos)

for i in range(n):
    update(i+1, c_idx(s[i]), 1)
#print(BITs)

q = int(input())
for _ in range(q):
    a, b, c = input().split()
    b = int(b)
    if a == "1":
        if s[b-1] == c:
            continue
        update(b, c_idx(s[b-1]), -1)
        update(b, c_idx(c), 1)
        s[b-1] = c
    else:
        c = int(c)
        count1 = query(c)
        count2 = query(b-1)
        ans = 0
        for i in range(26):
            if count1[i] - count2[i] > 0:
                ans += 1
        print(ans)