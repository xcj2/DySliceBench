# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_5_C&lang=jp
#  Enumeration : python3
#  2018.12.01 yonezawa

import sys
input = sys.stdin.readline
from collections import deque

class enumeration:
    def __init__(self,n):
        self.n = n
        self.depth = 0
        self.wnum = 0
        self.nq = []
        self.bits = [ pow(2,i) for i in range(n+1) ]
        self.mk_permutation(0,0,0)

    def mk_permutation(self,depth,bflag,wnum):
        if self.n == depth:
            self.nq.append(wnum)
            return
        for i in range(1,self.n+1):
            if bflag & self.bits[i-1] != 0:
                continue
            self.mk_permutation(depth + 1,bflag + self.bits[i-1],wnum*10+i)  
            
    def printList(self):
        l = self.nq
        self.nq.sort()
        for i in l:
            self.printInttoStr(i)
            
    def printInttoStr(self,i):
        c = ""
        for j in str(i):
            c += j + " "
        print(c.strip())

    def solve(self,tc):
        pos = self.nq.index(tc)
        if (pos != 0 ):
            self.printInttoStr(self.nq[pos-1])
        self.printInttoStr(tc)
        if (pos + 1 != len(self.nq) ):
            self.printInttoStr(self.nq[pos+1])
            
def main():
    n = int(input())
    tc = 0
    for i in list(map(int,input().split())):
        tc = tc * 10 + i
    e = enumeration(n)
    e.solve(tc)

if __name__ == '__main__':
    main()
