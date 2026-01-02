import math
def trial_division(n):
    primeN = n
    #素因数を格納するリスト
    factor = []
    #2から√n以下の数字で割っていく
    tmp = int(math.sqrt(n)) + 1
    for num in range(2,tmp):
        while n % num == 0:
            n //= num
            factor.append(num)
    #リストが空ならそれは素数
    if not factor:
        return primeN
    else:
        factor.append(n)
        if factor[-1]==1:
            factor.remove(1)
        return factor
import sys
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
mod = 10**9 + 7
inf = float('inf')
#for i in range(100):
#N = i + 1

N = I()

#print(N)
if N >= 82:
    print("No")
    exit()
elif N == 70 or N == 80 or N == 60:
    print("No")
    exit()
ans = [1]

ans = trial_division(N)
if type(ans) is int:
    if ans >= 10:
        print("No")
    else:
        print("Yes")
elif max(ans) >= 10:
    print("No")
elif 5 in ans and ans.count(5) >= 2 and len(ans) >= 3:
    print("No")
elif 7 in ans:
    if ans.count(7) >= 2 and len(ans) >= 3:
        print("No")
    elif len(ans) >= 4:
        if 3 in ans:
            print("No")
        else:
            print("Yes")
    else:
        print("Yes")
elif len(ans) >= 6 and ans.count(3) >= 1:
    print("No")

else:
    print("Yes")