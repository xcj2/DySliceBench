import sys


def input(): return sys.stdin.readline().strip()


def resolve():
    def main():
        s = input()
        k = int(input())
        if int(s[0]) != 1:
            return s[0]
        else:
            cnt = 0
            for i in s:
                if int(i) == 1:
                    cnt += 1
                    if cnt >= k:
                        return 1
                else:
                    if cnt >= k:
                        return 1
                    else:
                        return i

    print(main())
resolve()