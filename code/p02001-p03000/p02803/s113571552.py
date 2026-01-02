def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def f(S, start):
    H = len(S)
    W = len(S[0])
    stack = [start]
    closed = set()
    r = 0
    while stack:
        next_stack = []
        for s in stack:
            if s in closed:
                continue
            closed.add(s)
            for d in (-1, 1):
                for p in ((s[0] + d, s[1]), (s[0], s[1] + d)):
                    if p in closed:
                        continue
                    if p[0] < 0 or H <= p[0] or p[1] < 0 or W <= p[1]:
                        continue
                    if S[p[0]][p[1]] == "#":
                        continue
                    next_stack.append(p)
        stack = next_stack
        r += 1
    return r - 1


def main():
    H, W = read_values()
    S = [input() for _ in range(H)]

    res = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                continue
            res = max(res, f(S, (h, w)))
    print(res)

        
if __name__ == "__main__":
    main()
