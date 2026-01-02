import sys
sys.setrecursionlimit(500000)

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    N = ii()
    S = [input() for i in range(N)]
    ac = 0
    wa = 0
    tle = 0
    re = 0
    for i in range(N):
        if S[i] == 'AC':
            ac += 1
        if S[i] == 'TLE':
            tle += 1
        if S[i] == 'WA':
            wa += 1
        if S[i] == 'RE':
            re += 1

    print('AC x', ac)
    print('WA x', wa)
    print('TLE x', tle)
    print('RE x', re)


if __name__ == '__main__':
    main()
