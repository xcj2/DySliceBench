
def create_groups(H):
    F = "{:0" + str(H) + "b}"
    ret = set()
    for n in range(2 ** H):
        g = create_group(F.format(n))
        ret.add(tuple(g))
    return list(sorted(ret))


def create_group(s):
    ret = []
    n = 0
    for i in range(len(s)):
        if i == 0:
            ret.append(0)
        else:
            if s[i-1] == s[i]:
                ret.append(n)
            else:
                n += 1
                ret.append(n)
    return ret

# assert(create_group("0000") == [0,0,0,0])
# assert(create_group("0011") == [0,0,1,1])
# assert(create_group("0010") == [0,0,1,2])

# print(len(create_groups(10)))

def solve(H, W, K, fields):
    ans = H * W + 1
    for g in create_groups(H):
        M = len(set(g))
        s = [0 for _ in range(M)]
        tans = M - 1
        for w in range(W):
            for h in range(H):
                if fields[h][w] == "1":
                    s[g[h]] += 1
            if any([a > K for a in s]):
                s = [0 for _ in range(M)]
                tans += 1
                for h in range(H):
                    if fields[h][w] == "1":
                        s[g[h]] += 1
            if any([a > K for a in s]):
                tans = H * W + 1
                break
        ans = min(ans, tans)
    return ans
#
# assert(solve(3, 3, 1, ["111", "111", "111"]) == 4)
# assert(solve(1, 1, 1, ["1"]) == 0)
# assert(solve(2, 1, 1, ["1", "1"]) == 1)
# assert(solve(1, 2, 1, ["11"]) == 1)
# assert(solve(1, 2, 1, ["11"]) == 1)
# assert(solve(3, 5, 4, ["11100", "10001", "00111"]) == 2)
# assert(solve(3, 5, 8, ["11100", "10001", "00111"]) == 0)
# assert(solve(4, 10, 4, ["1110010010", "1000101110", "0011101001", "1101000111"]) == 3)

# print(slowsolve(5, 11, "33883"))
# print(solve(5, 11, "33883"))

if __name__ == "__main__":
    H, W, K = tuple(map(int, input().split(" ")))
    fields = []
    for _ in range(H):
        fields.append(input())
    print(solve(H, W, K, fields))
