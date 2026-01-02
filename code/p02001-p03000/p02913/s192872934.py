import math

def main():
    n = int(input())
    s = input()
    ans = solve(n, s)
    print(ans)


def solve(n, s):
    ans = 0
    for i in range(n - 1):
        tmp = Z(s[i:])
        t = [min(tmp[j], j)for j in range(n - i)]
        ans = max(ans, max(t))
        #print(tmp)
    return ans

def Z(s):
    l = len(s)
    ans = [l for _ in range(l)]

    i, j = 1, 0
    while i < l:
        while i + j < l and s[j] == s[i + j] :
            j += 1
        ans[i] = j

        if j == 0:
            i += 1
            continue

        k = 1
        while k < j and k + ans[k] < j:
            ans[i + k] = ans[k]
            k += 1
        i += k
        j -= k
    return ans

if __name__ == '__main__':
    main()