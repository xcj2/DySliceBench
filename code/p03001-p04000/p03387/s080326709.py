import sys
sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    def main():

        l = sorted(list(map(int, input().split())))
        even = 0
        for i in range(3):
            if l[i] % 2 == 0:
                even += 1
        cnt = 0
        if even == 0 or even == 3:
            for i in range(3):
                cnt += (l[2]-l[i])//2
            return cnt
        elif even == 1:
            cnt += 1
            for i in range(3):
                if l[i] % 2 == 1:
                    l[i] += 1
            for i in range(3):
                cnt += (max(l)-l[i])//2
            return cnt
        else:
            cnt += 1
            for i in range(3):
                if l[i] % 2 == 0:
                    l[i] += 1
            for i in range(3):
                cnt += (max(l)-l[i])//2
            return cnt
    print(int(main()))


#
resolve()