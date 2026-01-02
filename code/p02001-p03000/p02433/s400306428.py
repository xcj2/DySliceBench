readline = open(0).readline
writelines = open(1, 'w').writelines

Q = int(readline())
root = [None, None, None]
cursor = root[1] = [root, None, None]
def insert(x):
    global cursor
    cursor[0][1] = cursor[0] = cursor = [cursor[0], cursor, x]
def move(d):
    global cursor
    if d > 0:
        for _ in range(d):
            cursor = cursor[1]
    else:
        for _ in range(-d):
            cursor = cursor[0]
def erase():
    global cursor
    cursor[1][0] = cursor[0]
    cursor[0][1] = cursor = cursor[1]


C = [insert, move, erase].__getitem__
for q in range(Q):
    t, *a = map(int, readline().split())
    C(t)(*a)
root = root[1]
ans = []
while root[1]:
    ans.append("%d\n" % root[2])
    root = root[1]
writelines(ans)

