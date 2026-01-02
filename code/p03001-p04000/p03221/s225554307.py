import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    
    def readlines():
        for i in range(m):
            p, y = map(int, input().split())
            yield p, y, i

    cityies = sorted(readlines())

    def convert():
        prev = 0
        now = 1
        for p, y, i in cityies:
            if p == prev:
                now += 1
            else:
                now = 1
            yield i, "{:06}{:06}".format(p, now)

            prev = p

    print("\n".join(number for i, number in sorted(convert())))


main()
