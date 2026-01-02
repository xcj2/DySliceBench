import itertools
import collections
INF = 10 ** 9

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    p = collections.defaultdict(int)
    q = collections.defaultdict(list)
    for i, v in enumerate(itertools.permutations(range(8))):
        p[v] = i
        q[i] = list(v)

    dist = [INF] * (40325)
    dist[0] = 0
    que = collections.deque()
    que.append(0)

    def change(i, j, l):
        d = dist[p[tuple(l)]]
        l[i], l[j] = l[j], l[i]
        if dist[p[tuple(l)]] == INF:
            dist[p[tuple(l)]] = d + 1
            que.append(p[tuple(l)])
        l[i], l[j] = l[j], l[i]
        return

    while que:
        v = que.popleft()
        ll = q[v]
        i = ll.index(0)

        if i in {0, 4}: change(i, i+1, ll)
        elif i in {3, 7}: change(i-1, i, ll)
        else:
            change(i, i+1, ll)
            change(i-1, i, ll)
        change(i, (i+4)%8, ll)

    while True:
        try:
            A = ZZ()
            print(dist[p[tuple(A)]])
        except:
            break

    return

if __name__ == '__main__':
    main()

