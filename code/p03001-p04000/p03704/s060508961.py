import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


d = int(input())
def main(d):
    from collections import defaultdict
    vals = defaultdict(int)
    vals2 = defaultdict(int)
    for i in range(10):
        for j in range(10):
            vals[i-j] += 1
            if j>0:
                vals2[i-j] += 1
    def sub(n):
        vs = []
        for i in range(n):
            if i>=n-i:
                break
            vs.append(pow(10,n-i) - pow(10,i))
    #     if 9*sum(vs)<d:
    #         return 0
        def _sub(val, i):
            """vs[i:]以降でvalを作る通り数
            """
            if i==len(vs):
                if val==0:
                    return 1
                else:
                    return 0
            ans = 0
            for j in range(-9, 10):
                if (vs[i]*j)%pow(10,i+1)==val%(pow(10,i+1)):
                    ans += _sub(val-vs[i]*j, i+1) * vals[j]
            return ans

        ans = 0
        for i in range(-9,10):
            if (vs[0]*i)%10==d%10:
                ans += _sub(d-vs[0]*i, 1) * vals2[i]
        if n%2==0:
            ans *= 10
        return ans
    ans = 0
    i = 1
    while True:
        val = sub(i)
        ans += val
        if i>20:
            break
    #     if pow(10,i)-1>d:
    #         break
        i += 1
    return ans
print(main(d))