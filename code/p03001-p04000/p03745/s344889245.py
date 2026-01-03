n = int(input())
l = list(map(int, input().split()))

p = 0
count = 1

def start(L, A):
    global p
    if L[A+1] > L[A]:
        p=1
    elif L[A+1] < L[A]:
        p=2
    else:
        p=0

def upcount(L, A):
    global p, count
    if L[A+1] >= L[A]:
        p=1
    else:
        p=0
        count += 1

def downcount(L, A):
    global p, count
    if L[A+1] <= L[A]:
        p=2
    else:
        p=0
        count += 1

for i in range(n):
    if i == n-1:
        break
    elif p == 0:
        start(l, i)
    elif p == 1:
        upcount(l, i)
    else:
        downcount(l, i)

print(count)