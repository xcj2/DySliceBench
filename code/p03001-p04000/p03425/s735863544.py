import sys
import itertools

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def main():
    n = I()
    march = [0]*5
    for _ in range(n):
        s = input()[0]
        if s == 'M':
            march[0] += 1
        elif s == 'A':
            march[1] += 1
        elif s == 'R':
            march[2] += 1
        elif s == 'C':
            march[3] += 1
        elif s == 'H':
            march[4] += 1
    ans = 0
    for idx in itertools.combinations([0, 1, 2, 3, 4], 3):
        ans += march[idx[0]] * march[idx[1]] * march[idx[2]]
    print(ans)
if __name__ == '__main__':
    main()