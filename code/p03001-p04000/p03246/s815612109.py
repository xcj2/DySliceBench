import sys,collections,math;sys.setrecursionlimit(10**7)
def Is(): return [int(x) for x in sys.stdin.readline().split()]
def Ss(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

n = I()
t = Is()
od,ev = [t[i] for i in range(0,n,2)], [t[i] for i in range(1,n,2)]
odm = collections.Counter(od).most_common()[:2]
evm = collections.Counter(ev).most_common()[:2]
if odm[0][0] != evm[0][0]:
    ans = n - odm[0][1] - evm[0][1]
elif len(odm) == len(evm) == 1:
    ans = n//2
elif len(odm) == 1:
    ans = n - odm[0][1] - evm[1][1]
elif len(evm) == 1:
    ans = n - odm[1][1] - evm[0][1]
else:
    ans = n - max(odm[0][1]+evm[1][1], odm[1][1]+evm[0][1])
print(ans)
    