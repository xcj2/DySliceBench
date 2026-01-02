import sys
input = sys.stdin.readline

n,q = map(int, input().split())
stx = [tuple(map(int, input().split())) for _ in range(n)]
d = [int(input()) for _ in range(q)]

#これはセグ木 * bisect
import bisect
inf = 10**9 + 100

def init(n,init_num=0):
    num = len(str(bin(n-1))) + 1
    seg = [init_num] * (2**num)
    seg[0] = 2**(num-1)
    return(seg)

def update(head, tail, x):
    # print('{} {} {}'.format(head, tail, x))
    head += seg[0]
    tail += seg[0]
    points = []
    while(head <= tail):
        if(head == tail):
            points.append(head)
            break

        if(head % 2 ==1):
            points.append(head)
            head += 1
        head = head//2

        if(tail % 2 == 0):
            points.append(tail)
            tail -= 1
        tail = (tail-1)//2

    for point in points:
        seg[point] = min(seg[point], x)

def execute(p):
    p += seg[0]
    tmp = seg[p]
    while(p > 0):
        p = p//2
        tmp = min(tmp, sep[p])
    return(tmp)

def execute_all():
    for i in range(2,len(seg)):
        seg[i] = min(seg[i], seg[i//2])


seg = init(q, init_num = inf)

for i in range(n):
    left = bisect.bisect_left(d, stx[i][0] -stx[i][2])
    right = bisect.bisect_right(d, stx[i][1] - stx[i][2] -1) -1
    update(left, right, stx[i][2])
    # print('{} {} {}'.format(left, right, stx[i][2]))

execute_all()

for i in seg[seg[0]: seg[0] + q]:
    if(i == inf):
        print(-1)
    else:
        print(i)