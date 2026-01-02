import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

def main():
    S_ = S()
    T = S()
    a = len(S_)
    b = len(T)
    cnt_list = []

    for i in range(a - b + 1):
        cnt = 0
        S_1 = S_[i:i + b]
        for j in range(b):
            if S_1[j] == T[j]:
                cnt += 1
        cnt_list.append(cnt)

    ans = b - max(cnt_list)
    print(ans)



if __name__ == "__main__":
    main()


