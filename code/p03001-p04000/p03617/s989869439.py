# coding: utf-8
def II(): return int(input())
def ILI(): return list(map(int, input().split()))


def read():
    Q, H, S, D = ILI()
    N = II()
    return (Q, H, S, D, N)


def solve(Q, H, S, D, N):
    l_all = []
    l_all.append((Q * 8, "q"))
    l_all.append((H * 4, "h"))
    l_all.append((S * 2, "s"))
    l_all.append((D, "d"))
    l_all.sort(key= lambda x: x[0])
    if N % 2 == 0:
        ans = (N // 2) * l_all[0][0]
    else:
        ans = (N // 2) * l_all[0][0]
        if l_all[0][1] != "d":
            ans += l_all[0][0] // 2
        else:
            ans += l_all[1][0] // 2
    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()
