def Next(): return input()
def NextInt(): return int(Next())
def NextInts(): return map(int,input().split())
def Nexts(): return map(str,input().split())
def NextIntList(): return list(map(int,input().split()))
def RowInts(n): return [input() for i in range(n)]

used = {}
used[0] = 0
gg = {}

def dfs(n, a, b, c, d):
    global used
    # print(n)
    if n in used: return used[n]
    ret = n*d
    for i in range(-4, 4):
        now = n + i
        if now%2==0 and now > 0 and abs(i) < 2: ret = min(ret, abs(i)*d + a + dfs(now//2, a, b, c, d))
        if now%3==0 and now > 0 and abs(i) < 3: ret = min(ret, abs(i)*d + b + dfs(now//3, a, b, c, d))
        if now%5==0 and now > 0: ret = min(ret, abs(i)*d + c + dfs(now//5, a, b, c, d))
    used[n] = ret
    return ret
        


def solve():
    n,a,b,c,d = NextInts()
    global used
    used = {}
    gg = {}
    used[0] = 0
    used[1] = d
    used[2] = min(d*2, d+a)
    return dfs(n, a, b, c,d)
    
def main():
    t = NextInt()
    ans = [solve() for i in range(t)]
    for i in range(t):
        print(ans[i])

if __name__ == "__main__":
    main()
