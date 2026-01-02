import sys
def main():
    input = sys.stdin.readline
    H,W,N = map(int, input().split())
    start = tuple(map(int, input().split()))
    S = input().rstrip()
    T = input().rstrip()
    D = {
        'R': (0,1),
        'L': (0,-1),
        'U': (-1,0),
        'D': (1,0)
    }
    Dc = ['R', 'L', 'U', 'D']

    def move(current, direction):
        d = D[direction]
        return (current[0]+d[0], current[1]+d[1])

    def is_dropped(a):
        return not (1<=a[0]<=H and 1<=a[1]<=W)

    ans = True
    for i in range(4):
        cur = start
        for j in range(N):
            if S[j] == Dc[i]:
                cur = move(cur, Dc[i])
                if is_dropped(cur): ans = False
            if T[j] == Dc[i^1]:
                cur = move(cur, Dc[i^1])
                if is_dropped(cur): cur = move(cur, Dc[i])
    print('YES' if ans else 'NO')

if __name__ == '__main__':
    main()