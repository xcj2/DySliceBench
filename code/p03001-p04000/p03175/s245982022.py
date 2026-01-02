

def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    """
    OPT[node][BLACK] = product(OPT[child[i]][WHITE])
    OPT[node][WHITE] = product(OPT[child[i]][WHITE|BLACK])
    """
    N = read_int()
    G = [[] for _ in range(N)]
    modulo = 10**9+7
    for _ in range(N-1):
        x, y = read_ints()
        G[x-1].append(y-1)
        G[y-1].append(x-1)
    # type, node, parent
    VISIT, CALCULATE = 0, 1
    BLACK, WHITE = 0, 1
    OPT = [
        [1, 1] for _ in range(N)
    ]
    Q = [(VISIT, 0, None)]
    while len(Q) != 0:
        t, node, parent = Q.pop()
        if VISIT == t:
            Q.append((CALCULATE, node, parent))
            for child in G[node]:
                if child != parent:
                    Q.append((VISIT, child, node))
        else:
            for child in G[node]:
                if child != parent:
                    OPT[node][BLACK] = (OPT[node][BLACK]*OPT[child][WHITE])%modulo
                    OPT[node][WHITE] = (OPT[node][WHITE]*(OPT[child][WHITE]+OPT[child][BLACK]))%modulo
    return (OPT[0][BLACK]+OPT[0][WHITE])%modulo


if __name__ == '__main__':
    print(solve())
