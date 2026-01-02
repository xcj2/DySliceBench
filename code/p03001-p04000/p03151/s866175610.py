import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    def main():

        N = int(input())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        pluslist = []
        minuscnt = 0
        cnt = 0

        for i in range(N):
            if A[i] < B[i]:
                minuscnt += B[i]-A[i]
                cnt += 1
            elif A[i] > B[i]:
                pluslist.append(A[i]-B[i])
        if minuscnt == 0:
            return 0
        pluslist.sort(reverse=True)
        val = 0
        i = 0
        while True:
            val += pluslist[i]
            i += 1
            if val >= minuscnt:
                return i+cnt
            elif i >= len(pluslist):
                return -1
        return i+1+cnt

    print(main())

resolve()