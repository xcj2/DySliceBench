words = lambda t : list(map(t, input().split()))



n = int(input())
a = words(int)
b = words(int)

def getNext(i):
    if i == n-1:
        return 0
    else:
        return i+1

def getPrev(i):
    if i == 0:
        return n-1
    else:
        return i-1

from collections import deque
q = deque()

def verify(i):
    if b[i] != a[i] and b[i] - (b[getNext(i)] + b[getPrev(i)]) >= a[i]:
        return True
    else:
        return False

for i in range(len(b)):
    if b[i] >= a[i] and verify(i):
        q.append(i)

ans = 0
succeed = True
while not len(q) == 0:
    i = q.popleft()
    ni = getNext(i)
    pi = getPrev(i)
    #print(i, b)
    d = b[ni] + b[pi]
    if b[i] % d == a[i] % d:
        ans += b[i] // d - (a[i] // d)
        b[i] = a[i]
    else:
        ans += b[i] // d
        b[i] %= d
    if b[i] < a[i]:
        succeed = False
        break
    if verify(ni):
        q.append(ni)
    if verify(pi):
        q.append(pi)

for i in range(len(b)):
    if a[i] != b[i]:
        succeed = False
        break

if succeed:
    print(ans)
else:
    print(-1)
