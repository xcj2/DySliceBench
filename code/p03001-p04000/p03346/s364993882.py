def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]

    idx = make_index(p)
    c = count_sequence(p, idx)
    ans = n - c
    print(ans)

def make_index(p):
    idx = dict()
    for i, v in enumerate(p):
        idx[v] = i
    return idx

def count_sequence(p, idx):
    cmax = 0
    c = 0
    i = -1

    x = 1
    while True:
        j = idx.get(x, None)
        if j is None:
            cmax = max(cmax, c)
            break
        elif j < i:
            cmax = max(cmax, c)
            c = 1
            i = j
        else:
            c += 1
            i = j
        x += 1

    return cmax

main()
