ans_list = []

def solve():
    a, L = map(int,input().split())
    if (a, L) == (0,0):
        return "end"

    def Add(n: int) -> list:
        n = str(n)
        n = list(n)
        n = [int(s) for s in n]
        n = [0]*(L - len(n)) + n
        return n

    def Max(n: list) -> int:
        n = sorted(n, reverse=True)
        n = "".join([str(i) for i in n])
        n = int(n)
        return n
    
    def Min(n: list) -> int:
        n = sorted(n)
        n = "".join([str(i) for i in n])
        n = int(n)
        return n
    
    d = dict()

    d[a] = 0

    for i in range(1,21):
        a = Add(a)
        na = Max(a) - Min(a)
        j = d.get(na)
        if j is None:
            d[na] = i
        else:
            break
        a = na
    
    ans = "{} {} {}".format(j, na, i - j)
    return ans
        
while True:
    ans = solve()
    if ans == "end":
        break
    ans_list.append(ans)

for ans in ans_list:
    print(ans)
