from sys import stdin
readline = stdin.readline
def i_input(): return int(readline().rstrip())
def i_map(): return map(int, readline().rstrip().split())
def i_list(): return list(i_map())

def main():
    X, N = i_map()
    if N == 0:
        print(X)
        exit()
    P = i_list()
    p = list(map(lambda x: abs(x - X), P))
    p.sort()
    for i, j in enumerate(p, 1):
        if i // 2 != j:
            ans = X - (i // 2)
            if ans in P:
                ans = X + (i // 2)
            break
    else:
        if N % 2 == 1:
            ans = X - ((N + 1) // 2)
        else:
            ans = X - (N // 2)
            if ans in P:
                ans = X + (N // 2)
    print(ans)

if __name__ == "__main__":
    main()
