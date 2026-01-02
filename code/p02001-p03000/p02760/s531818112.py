import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    A = [[]for _ in range(3)]
    for i in range(3):
        A[i] = LI()
    A_ = [[]for _ in range(3)]
    for i in range(3):
        for j in range(3):
            A_[j].append(A[i][j])
    A__ = [[]for  _ in range(2)]
    for i in range(3):
        A__[0].append(A[i][i])
        A__[1].append(A[i][2 - i])

    N = I()
    B = []
    for i in range(N):
        b = I()
        B.append(b)
        for i in range(3):
            if b in A[i]:
                ind = A[i].index(b)
                A[i][ind] = 0
            if b in A_[i]:
                ind = A_[i].index(b)
                A_[i][ind] = 0
        for j in range(2):
            if b in A__[j]:
                ind = A__[j].index(b)
                A__[j][ind] = 0
    ans_list = []
    for i in range(3):
        ans_list.append(sum(A[i]))
        ans_list.append(sum(A_[i]))
    for j in range(2):
        ans_list.append(sum(A__[j]))

    if 0 in ans_list:
        print('Yes')
    else:
        print('No')






if __name__ == "__main__":
    main()