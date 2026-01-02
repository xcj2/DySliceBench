n = int(input())
s = input()


def arihon_SA(T):
    rank = [0] * (n + 1)
    SA = [0] * (n + 1)
    temp = [0] * (n + 1)

    def rank_calc(i):
        res1 = rank[i]
        res2 = -1
        if i + k <= n:
            res2 = rank[i + k]
        return (res1, res2)

    for i in range(n + 1):
        SA[i] = i
        if i < n:
            rank[i] = ord(T[i])
        else:
            rank[i] = -1
    k = 1

    while k <= n:
        SA.sort(key=rank_calc)
        temp[SA[0]] = 0
        for i in range(1, n + 1):
            temp[SA[i]] = temp[SA[i - 1]]
            if rank_calc(SA[i - 1]) < rank_calc(SA[i]):
                temp[SA[i]] += 1
        rank = temp[::]
        k *= 2

    return SA


# SAとsからSA[i+1],SA[i]の共通接頭辞LCP[i]を求めたい。
# len(s)=nならlen(SA)=n+1
# LCP[0]は必ず0
def arihon_LCP(s, SA):
    num = len(s)
    rank = [0] * (num + 1)
    LCP = [-1] * (num)
    for i in range(num + 1):
        rank[SA[i]] = i
    h = 0
    LCP[0] = 0
    for i in range(num):
        j = SA[rank[i] - 1]
        if h > 0:
            h -= 1
        while j + h < num and i + h < num:
            if s[j + h] != s[i + h]:
                break
            else:
                h += 1
        LCP[rank[i] - 1] = h
    return LCP


SA = arihon_SA(s)
LCP = arihon_LCP(s, SA)

# sparse table
num = n.bit_length()
ST = [[0] * (num + 1) for _ in range(n)]

for i in range(n):
    ST[i][0] = LCP[i]

for j in range(num):
    for i in range(n):
        ST[i][j + 1] = ST[i][j]
        delta = 1 << j
        if i + delta < n:
            ST[i][j + 1] = min(ST[i][j + 1], ST[i + delta][j])


def query(a, b):
    if a > b:
        a, b = b, a
    d = (b - a).bit_length() - 1
    delta = 1 << d
    res = min(ST[a][d], ST[b - delta][d])
    return res


ans = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        a = SA[i]
        b = SA[j]
        temp = query(i, j)
        if abs(b - a) >= temp:
            ans = max(ans, temp)
print(ans)
