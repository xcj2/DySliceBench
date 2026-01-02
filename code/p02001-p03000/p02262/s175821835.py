import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

def ShellSort(bb):
    aa = bb[:]

    def InsertionSort(d):
        shift = 0
        for i in range(n):
            a = aa[i]
            j = i
            while j - d >= 0 and aa[j - d] > a:
                aa[j] = aa[j - d]
                shift += 1
                j -= d
            aa[j] = a
        return shift

    cnt = 0
    n = len(aa)
    dd = [1]
    while dd[-1] * 3 + 1 < n:
        dd.append(dd[-1] * 3 + 1)
    dd.reverse()
    print(len(dd))
    print(*dd)
    for d in dd:
        cnt += InsertionSort(d)
    print(cnt)
    return aa

def main():
    n = int(input())
    # aa = list(map(int, input().split()))
    aa = [int(input()) for _ in range(n)]
    aa = ShellSort(aa)
    for a in aa:
        print(a)

main()

