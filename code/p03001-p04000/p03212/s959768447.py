import sys
def input(): return sys.stdin.readline().strip()

def func(S, char):
    l = len(char)
    if int(S[0]) in char:
        num = 0
        for c in char:
            if int(c) < int(S[0]): num += 1
        if len(S) == 1: return num + 1
        return num * l ** (len(S) - 1) + func(S[1:], char)
    else:
        num = 0
        for c in char:
            if int(c) < int(S[0]): num += 1
        return num * l ** (len(S) - 1)

def main():
    S = input()
    ans = func(S, [3, 5, 7]) - func(S, [3, 5]) - func(S, [5, 7]) - func(S, [3, 7]) + func(S, [3]) + func(S, [5]) + func(S, [7])
    for i in range(1, len(S)):
        n = len(S) - i
        ans += 3 ** n - 3 * 2 ** n + 3
    print(ans)


if __name__ == "__main__":
    main()
