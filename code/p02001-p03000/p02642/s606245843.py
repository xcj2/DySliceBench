import collections

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N = Z()
    A = sorted(ZZ())
    cA = collections.Counter(A)
    MAX_A = 10 ** 6
    is_ok = [True] * (MAX_A + 1)

    if 1 in cA.keys():
        if cA[1] == 1: print(1)
        elif cA[1] >= 2: print(0)
        return

    for a in cA.keys():
        if not is_ok[a]: continue
        if cA[a] >= 2: is_ok[a] = False
        for i in range(2, MAX_A + 1):
            if a * i > MAX_A: break
            is_ok[a * i] = False

    ans = 0
    for a in cA.keys():
        if is_ok[a]: ans += 1

    print(ans)

    return

if __name__ == '__main__':
    main()
