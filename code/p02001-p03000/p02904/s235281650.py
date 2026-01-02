from collections import deque

def sliding_minima(a, k):
    dq = deque()
    l = r = 0
    ret = []
    for i, item in enumerate(a):
        while(dq and a[dq[-1]] >= a[i]):
            dq.pop()
        dq.append(i)
        if i < k - 1:
            continue
        if dq[0] == i - k:
            dq.popleft()
        ret.append(a[dq[0]])
    return ret

def sliding_maxima(a, k):
    dq = deque()
    l = r = 0
    ret = []
    for i, item in enumerate(a):
        while(dq and a[dq[-1]] <= a[i]):
            dq.pop()
        dq.append(i)
        if i < k - 1:
            continue
        if dq[0] == i - k:
            dq.popleft()
        ret.append(a[dq[0]])
    return ret

def is_increasing(a, k):
    increasing = [0] * len(a)
    for i, (a1, a2) in enumerate(zip(a, a[1:])):
        if a1 < a2:
            increasing[i+1] = 1
    ret = [0] * (len(a) - k + 1)
    val = sum(increasing[1:k])
    if val == k-1:
        ret[0] = 1
    for i in range(len(a) - k):
        val += increasing[i + k]
        val -= increasing[i + 1]
        if val == k-1:
            ret[i+1] = 1
        else:
            ret[i+1] = 0
    return ret

n, k = [int(item) for item in input().split()]
a = [int(item) for item in input().split()]

minima = sliding_minima(a, k)
maxima = sliding_maxima(a, k)
increasing = is_increasing(a, k)

ans = n - k + 1
if increasing[0]:
    ans -= 1
for l, r, minima, maxima, inc in zip(a, a[k:], minima[1:], maxima, increasing[1:]):
    if (l < minima and r > maxima) or inc:
        ans -= 1
if sum(increasing) > 0:
    ans += 1
print(ans)