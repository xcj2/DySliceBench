import sys
import itertools


input = sys.stdin.readline


def cannot_attack(Q):
    for i in range(7):
        sx, sy = Q[i]
        for j in range(i+1, 8):
            tx, ty = Q[j]
            if abs(tx-sx) == abs(ty-sy):
                return False
    return True


def include_fq(sq):
    for e in fq:
        if e not in sq:
            return False
    return True


def main():
    Q = []
    for p in itertools.permutations(range(8)):
        Q = [(i, p[i]) for i in range(8)]
        if cannot_attack(Q) and include_fq(set(Q)):
            break
    for y, x in Q:
        print("."*x+"Q"+"."*(7-x))


if __name__ == "__main__":
    K = int(input())
    fq = [tuple(map(int, input().split())) for _ in range(K)]
    main()
