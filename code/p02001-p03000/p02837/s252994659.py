n = int(input())
d = dict()
for i in range(n):
    a = int(input())
    for j in range(a):
        l = d.get(i, [])
        p, t = list(map(int, input().split(' ')))
        l.append((p-1, t))
        d[i] = l
# d[i] に i番の人の証言のlistがあるので 全パターン(=2^15)で矛盾しないか試す？
def get_bit_array(num):
    res = []
    while num > 0:
        res.append(num%2)
        num //= 2
    while len(res) < n:
        res = res + [0]
    return res[::-1]

def valid(tfs):
    for i in range(len(tfs)):
        honest = tfs[i]
        if not honest:  # 嘘つきは無視する
            continue
        for (person, tf) in d.get(i, []):  # 合ってる？
            if tfs[person] != tf:
                return False
    return True

ans = 0
def f(num):
    global ans
    if num >= 2**n:
        return
    tfs = get_bit_array(num)  # tfs = [1,0,1,0,...0] true or flase 
    total = sum(tfs)
    if valid(tfs):
        ans = max(ans, total)

for i in range(int(2**n)):
    f(i)

print(ans)
