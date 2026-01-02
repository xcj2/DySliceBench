import sys
def main():
    input = sys.stdin.readline
    N = int(input())
    xyh = [tuple(map(int, input().split())) for _ in range(N)]
    xyh.sort(reverse=True, key=lambda x:x[2])

    def check(cx, cy):
        def dist(x, y): return abs(x-cx) + abs(y-cy)
        tmp = 0
        for x, y, h in xyh:
            d = dist(x,y)
            if h == 0:
                if tmp > d: return -1
            else:
                if tmp != 0 and tmp != h+d: return -1
                tmp = h+d
        return tmp
    
    for x in range(101):
        for y in range(101):
            H = check(x,y)
            if H >= 0:
                print('{} {} {}'.format(x,y,H))
                return

if __name__ == '__main__':
    main()