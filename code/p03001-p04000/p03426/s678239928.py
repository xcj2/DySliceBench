from functools import lru_cache
h, w, d = map(int, input().split())
pos = [[] for j in range(h*w)]
for a in range(h):
    s = list(map(int, input().split()))
    for g in range(w):
        pos[s[g] -1] = [s[g], a+1, g+1]
q = int(input())

def soo(now, start):
    next = now + d
    prevy, prevx = pos[now - 1][1], pos[now - 1][2]
    nexty, nextx = pos[next - 1][1], pos[next - 1][2]
    return ((abs(nexty - prevy) + abs(nextx - prevx)))

def solve(start, end):
    now = 0
    ans = 0
    for i in range(int((end - start) / d)):
        now = start if not now else now + d
        ans += soo(now, start)
    return ans

time = [0 for h in range(h*w)]
for l in range(h*w - d):
    if not time[l + d]:
        time[l+d] = time[l] + (abs(pos[l+d][1] - pos[l][1]) + abs(pos[l+d][2] - pos[l][2]))


@lru_cache(maxsize=None)
def ask(st, en):
    return time[en-1] - time[st-1]


for rr in range(q):
    dd, ff = map(int, input().split())
    print(ask(dd, ff))