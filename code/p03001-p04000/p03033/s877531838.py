class BIT:
    def __init__(self, N):
        self.tree = [0] * (N + 1)  # 1-indexed
        self.N = N

    def add(self, i, x):
        """tree[i]と関連個所にxを加える"""
        tree = self.tree
        N = self.N
        while i <= N:
            tree[i] += x
            i += i & (-i)

    def sum(self, i):
        tree = self.tree
        s = 0
        while i:
            s += tree[i]
            i -= i & (-i)
        return s

    def binary_search(self, x):
        """区間和 >=x となる最小のindex"""
        tree = self.tree
        N = self.N
        i = 0
        step = 1 << (N.bit_length() - 1)
        while step:
            if i + step <= N and tree[i + step] < x:
                i += step
                x -= tree[i]
            step >>= 1
        return i + 1


def main():
    from collections import deque, namedtuple
    from operator import attrgetter
    import sys

    input = sys.stdin.readline
    Event = namedtuple('Event', 'time position')

    N, Q = map(int, input().split())

    go = []
    stop = []
    xs = set()
    for _ in range(N):
        s, t, x = map(int, input().split())
        stop.append(Event(time=s - x, position=x))
        go.append(Event(time=t - x, position=x))
        xs.add(x)

    xs = sorted(xs)

    stop.sort(key=attrgetter('time'))
    go.sort(key=attrgetter('time'))

    stop = deque(stop)
    go = deque(go)

    compress = {x: i for i, x in enumerate(xs, 1)}
    decompress = {i: x for i, x in enumerate(xs, 1)}

    ans = []
    b = BIT(N)
    for _ in range(Q):
        d = int(input())
        while go and go[0].time <= d:
            e = go.popleft()
            p = compress[e.position]
            b.add(p, -1)
        while stop and stop[0].time <= d:
            e = stop.popleft()
            p = compress[e.position]
            b.add(p, 1)

        compressed_ind = b.binary_search(1)
        ind = decompress.get(compressed_ind, -1)
        ans.append(ind)

    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
