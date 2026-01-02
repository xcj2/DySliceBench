#coding:utf-8
import copy
from collections import deque
import sys
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = lambda *something : print(*something) if DEBUG else 0
DEBUG = True

def index(a,b):
    return str(min(a,b)) + "," +  str(max(a, b))

def main(given = sys.stdin.readline):
    input = lambda : given().rstrip()
    LMIIS = lambda : list(map(int,input().split()))
    II = lambda : int(input())
    XLMIIS = lambda x : [LMIIS() for _ in range(x)]

    n = II()
    xy = []
    for i in range(n):
        a = II()
        xy.append(XLMIIS(a))


    def f(a):
        i = 0
        while n != i  and a[i] != -1:
            i += 1
        if i == n:
            return 0

        b = copy.copy(a)
        b[i] = 1
        b_ans = 1
        mujun = 0
        q = deque([i])
        while len(q) != 0:
            qq = q.pop()
            for j in xy[qq]:
                if b[j[0]-1] == -1 and j[1] == 1:
                    q.append(j[0]-1)
                    b[j[0]-1] = 1
                    b_ans += 1
                elif b[j[0]-1] == -1 and j[1] == 0:
                    b[j[0]-1] = 0
                elif b[j[0]-1] != j[1]:
                    mujun = 1
                    break
        if mujun == 0:
            b_ans += f(b)
        else:
            b_ans = 0

        c = copy.copy(a)
        c[i] = 0
        c_ans = f(c)

        return max(b_ans, c_ans)


    print(f([-1]*n))







if __name__ == '__main__':
    main()
