import heapq


class Reverse:
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __repr__(self):
        return repr(self.val)


class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            for i in range(len(arr)):
                arr[i] = Reverse(arr[i])
        self.desc = desc
        self.hq = arr
        heapq.heapify(self.hq)

    def pop(self):
        if len(self.hq) == 0:
            return None
        if self.desc:
            return heapq.heappop(self.hq).val
        else:
            return heapq.heappop(self.hq)

    def push(self, a):
        if self.desc:
            heapq.heappush(self.hq, Reverse(a))
        else:
            heapq.heappush(self.hq, a)

    def top(self):
        if self.desc:
            return self.hq[0].val
        else:
            return self.hq[0]

    def __len__(self):
        return len(self.hq)


n, m = map(int, input().split(' '))
ab = []
for _ in range(n):
    a, b = map(int, input().split(' '))
    if a > m:
        continue
    ab.append((a, b))
ab.sort(reverse=True)

ans = 0
h = Heapq([], desc=True)
for i in range(1, m+1):
    while ab and ab[-1][0] <= i:
        a, b = ab.pop()
        h.push(b)
    if h:
        ans += h.pop()
print(ans)
