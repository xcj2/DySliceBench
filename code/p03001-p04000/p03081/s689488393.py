N,Q = map(int,input().split(" "))
s=list(input())
ju = []
for i in range(Q):
    ju.append(input().split(" "))

def isdeadleft(xp):
    oxp = xp
    for i in range(Q):
        com = ju[i]
        if s[xp] == com[0]:
            if com[1] == "L":
                xp -= 1
            else:
                xp += 1
        if xp < 0:
            return True
        if xp > N-1:
            xp = N-1
    return False

def isdeadright(xp):
    oxp = xp
    for i in range(Q):
        com = ju[i]
        if s[xp] == com[0]:
            if com[1] == "L":
                xp -= 1
            else:
                xp += 1
        if xp < 0:
            xp = 0
        if xp > N-1:
            return True
    return False

def mid(x1,x2):
    return int((x1+x2)/2)

if isdeadleft(N-1) or isdeadright(0):
    print(0)
    exit()

#left
p1 = 0
p3 = N-1
p2 = mid(p1,p3)
while p3 - p1 != 1:
    if isdeadleft(p2):
        p1,p2 = p2,mid(p2,p3)
    else:
        p2,p3 = mid(p1,p2),p2
if isdeadleft(p1):
    p = p3
else:
    p = p1
#right
p1 = 0
p3 = N-1
p2 = mid(p1,p3)
while p3 - p1 != 1:
    if isdeadright(p2):
        p2,p3 = mid(p1,p2),p2
    else:
        p1,p2 = p2,mid(p2,p3)
if isdeadright(p3):
    q = p1
else:
    q = p3

if p > q:
    print(0)
else:
    print(q-p+1)
