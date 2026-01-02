import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():


    n = I()
    time = [0 for _ in range(n)]
    start = [0 for _ in range(n)]
    freq = [0 for _ in range(n)]

    for i in range(n-1):
        time[i], start[i], freq[i] = LI()

    ans = [0 for _ in range(n)]

    for i in range(n):
        before = 0
        after = 0
        for j in range(i,n-1):
            if before < start[j]:
                after = start[j]
            else:
                after = before - before%freq[j] + freq[j]*(before%freq[j] != 0)

            before = after + time[j]

        ans[i] = before

    print(*ans, sep="\n")



main()
