H = int(input())
A = list(map(int, input().split()))

def per(p):
    global parentkey
    if p%2 == 0:
        pk = p/2-1
    else:
        pk = p//2
    if pk >= 0:
        parentkey = 'parent key = {}, '.format(A[int(pk)])
    else:
        parentkey = ''


def left(l):
    l += 1
    global leftkey
    if 2*l <= H:
        leftkey = 'left key = {}, '.format(A[2*l-1])
    else:
        leftkey = ''


def right(r):
    r += 1
    global rightkey
    if 2*r+1 <= H:
        rightkey = 'right key = {}, '.format(A[2*r])
    else:
        rightkey = ''


for i in range(H):
    per(i)
    left(i)
    right(i)
    print('node {}: key = {}, {}{}{}'.format(i+1, A[i], parentkey, leftkey, rightkey))
