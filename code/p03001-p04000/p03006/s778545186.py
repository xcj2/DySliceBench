import collections
import itertools

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N = Z()
    P = [ZZ() for _ in range(N)]
    vecs = set()
    d = collections.defaultdict(int)
    output = 1
    if N == 1:
        print(output)
        return

    for i, j in itertools.combinations(range(N), 2):
        dx, dy = P[i][0] - P[j][0], P[i][1] - P[j][1]
        if dx < 0: dx, dy = -dx, -dy
        vecs.add((dx, dy))

    c = 0
    for v in list(vecs):
        cc = 0
        for i, j in itertools.combinations(range(N), 2):
            if (P[i][0] - P[j][0] == v[0] and P[i][1] - P[j][1] == v[1]) or (P[i][0] - P[j][0] == -v[0] and P[i][1] - P[j][1] == -v[1]):
                cc += 1
        c = max(c, cc)
    output = (N - c)
    print(output)
    return

if __name__ == '__main__':
    main()
