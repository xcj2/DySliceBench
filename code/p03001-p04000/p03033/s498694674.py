import sys
input = sys.stdin.readline

n,q = map(int, input().split())
# stx = [tuple(map(int, input().split())) for _ in range(n)]
stx = [0]*n
for i in range(n):
    stx[i] = tuple(map(int, input().split()))
# d = [int(input()) for _ in range(q)]
d = [0]*q
for i in range(q):
    d[i] = int(input())

#これはセグ木 * bisect
import bisect
inf = 10**9 + 100

# 定数倍高速化
b_left = bisect.bisect_left
b_right = bisect.bisect_right

def init(n,init_num=0):
    num = len(str(bin(n-1))) + 1
    seg = [init_num] * (2**num)
    # seg[0] = 2**(num-1)
    seg0 = 2**(num-1)
    return(seg,seg0)

def update(head, tail, x):
    # print('{} {} {}'.format(head, tail, x))
    head += seg0
    tail += seg0
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

def execute_all():
    for i in range(2,len(seg)):
        seg[i] = min(seg[i], seg[i//2])


seg,seg0 = init(q, init_num = inf)

for i in range(n):
    left = b_left(d, stx[i][0] -stx[i][2])
    right = b_right(d, stx[i][1] - stx[i][2] -1) -1
    update(left, right, stx[i][2])
    # print('{} {} {}'.format(left, right, stx[i][2]))

execute_all()

for i in seg[seg0: seg0 + q]:
    if(i == inf):
        print(-1)
    else:
        print(i)