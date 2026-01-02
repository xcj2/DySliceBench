import sys
input = sys.stdin.readline


def solve(S):
    def split(sub):
        result = []
        s = sub.partition('LR')
        while s[1] != '':
            new_s = s[0] + s[1][0]
            rem = s[1][1] + s[2]
            result.append(new_s)
            s = rem.partition('LR')
        return result + [s[0]]

    def count(sub):
        c = [0] * len(sub)
        l = sub.index('L')

        # R
        i = 1
        while l - i >= 0:
            c[l - (i % 2)] += 1
            i += 1

        # L
        i = 0
        while l + i < len(sub):
            c[l - (i % 2)] += 1
            i += 1

        return c

    ans = []
    for s in split(S):
        ans += count(s)
    return ans


def main():
    S = input().strip()
    ans = solve(S)

    for x in ans:
        print(x, end=' ')


if __name__ == "__main__":
    main()
