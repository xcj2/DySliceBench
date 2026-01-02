import sys
input = sys.stdin.readline


def readstr():
    return input().strip()


def readint():
    return int(input())


def readnums():
    return map(int, input().split())


def readstrs():
    return input().split()


def main():
    abcd = list(map(int, list(readstr())))
    l = [['+', '+', '+'], ['+', '+', '-'], ['+', '-', '+'], ['+', '-', '-'], ['-', '+', '+'], ['-', '+', '-'], ['-', '-', '+'], ['-', '-', '-']]
    for ll in l:
        ans = abcd[0]
        for i, x in enumerate(ll):
            if x == '+':
                ans += abcd[i + 1]
            else:
                ans -= abcd[i + 1]
        if ans == 7:
            s = ''
            for i in range(3):
                s += str(abcd[i]) + ll[i]
            s += str(abcd[3])
            print(s + '=7')
            break


if __name__ == "__main__":
    main()
