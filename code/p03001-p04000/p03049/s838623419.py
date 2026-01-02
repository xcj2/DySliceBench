from collections import deque
from heapq import heappush,heappop
import re
def int_raw():
    return int(input())

def ss_raw():
    return input().split()

def ints_raw():
    return list(map(int, ss_raw()))

INF = 1<<29

N = int_raw()
ss = []
cs = []
end_A = []
start_B = []
both_AB = []
for _ in range(N):
    s = input()
    end_A.append(s[-1]=="A")
    start_B.append(s[0]=="B")
    both_AB.append(end_A[-1] and start_B[-1])
    cs.append(s.count("AB"))
    ss.append(s)


def main():
    n_both_AB = sum(both_AB)
    n_endA = sum(end_A)-n_both_AB
    n_startB = sum(start_B)-n_both_AB
    #n_minAB = min(n_startB,n_endA)
    #n_maxAB = max(n_startB,n_endA)
    ans =0
    is_last_A = False
    while (n_both_AB+n_endA+n_startB)>0:
        if is_last_A:
            if n_both_AB>0:
                n_both_AB-=1
                ans+=1
                is_last_A=True
            elif n_startB>0:
                n_startB-=1
                ans+=1
                is_last_A=False
            else:
                 break
        else:
            if n_endA >0:
                n_endA-=1
                is_last_A=True
            elif n_both_AB>0:
                n_both_AB-=1
                is_last_A=True
            else:
                break
        
        
    return sum(cs)+ans
    """if n_minAB+n_both_AB <n_maxAB:
        return sum(cs)+n_minAB+n_both_AB
    else:
        return sum(cs)+(n_minAB+n_maxAB+n_both_AB)//2"""

print(main())
