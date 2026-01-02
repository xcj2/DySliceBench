import sys
from itertools import groupby, chain
def input(): return sys.stdin.readline().rstrip()


def trans(l_2d):
    return [list(x) for x in zip(*l_2d)]


def lamp(arr):
    count = [[] for i in range(len(arr))]
    for i in range(len(arr)):
        lamps = []
        for key, value in groupby(arr[i]):
            n = int(len(list(value)))
            if key == '.':
                lamps += [n]*n
            else:
                lamps += [0]*n
        count[i] = lamps
    return count


def main():
    h, w = map(int, input().split())
    s = [list(input()) for i in range(h)]
    tate = lamp(s)
    yoko = lamp(trans(s))
    ans=0
    for hh in range(h):
        for ww in range(w):
            ans=max(ans,tate[hh][ww]+yoko[ww][hh]-1)
    print(ans)
        


if __name__ == '__main__':
    main()
