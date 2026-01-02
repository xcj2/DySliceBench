#  http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_D&lang=jp
#  Allocatin : python3
#  2018.12.09 yonezawa


#from collections import deque
import sys
input = sys.stdin.readline
#import cProfile

def calc(l,k,m):
    n = len(l)
    kp = 1
    mp = 0
    for i in range(n):
        if (l[i] >  m ):
            return False
        if (mp + l[i] <= m ):
            mp += l[i]
            continue
        kp += 1
        mp = l[i]
    if (kp <= k):
        return True
    else:
        return False

def binSearch(l,k):
    left = 0
    right = 100000 * 100000
    mid = right // 2
    flg = False
    while right - left > 1:
        if calc(l,k,mid) == False:
            left = mid
            flg = True
        else:
            right = mid
            flg = False
        mid =  (right + left ) // 2 
    return right


def main():
    l = []
    (n,k) = map(int,input().split())
    for i in range(n):
        l.append(int(input()))
    t = binSearch(l,k)
    print (t)

if __name__ == '__main__':
   main()
#    pr = cProfile.Profile()
#    pr.runcall(main)
#    pr.print_stats()
