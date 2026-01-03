from heapq import heapify, heappop, heappush


class MaxHeap:
    def __init__(self, li):
        self.hp = []
        for e in li:
            heappush(self.hp, -e)

    def push(self, x):
        heappush(self.hp, -x)

    def pop(self):
        ret = heappop(self.hp)
        ret *= -1
        return ret

    def seak(self):
        return -self.hp[0]

    def sum(self):
        return -sum(self.hp)


n = int(input())
a = list(map(int, input().split()))

f = a[:n]
s = a[n:2*n]
t = a[2*n:]

heapify(f)
t = MaxHeap(t)

f_sm = sum(f)
f_sm_li = [f_sm]
for e in s:
    heappush(f, e)
    f_sm += e
    pp = heappop(f)
    f_sm -= pp
    f_sm_li.append(f_sm)

t_sm = t.sum()
t_sm_li = [t_sm]
for e in s[::-1]:
    t.push(e)
    t_sm += e
    pp = t.pop()
    t_sm -= pp
    t_sm_li.append(t_sm)

t_sm_li = t_sm_li[::-1]
ans = -float("inf")
for ef, et in zip(f_sm_li, t_sm_li):
    ans = max(ans, ef - et)

print(ans)
