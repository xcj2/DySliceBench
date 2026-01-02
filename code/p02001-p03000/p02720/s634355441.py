from functools import lru_cache

(K,) = [int(x) for x in input().split()]


def solve(K):
    def getNext(x):
        if x == 0:
            return [0, 1]
        if x == 9:
            return [8, 9]
        return [x - 1, x, x + 1]

    @lru_cache(maxsize=None)
    def getNum(begin, digits):
        if digits == 0:
            assert False
            return 0
        if digits == 1:
            return 1
        ans = 0
        for x in getNext(begin):
            ans += getNum(x, digits - 1)
        return ans

    ans = []
    count = 0
    for digits in range(1, 30):
        for i in range(1, 10):
            delta = getNum(i, digits)
            if count < K <= count + delta:
                ans.append(i)
                while digits > 1:
                    for x in getNext(ans[-1]):
                        delta = getNum(x, digits - 1)
                        if count < K <= count + delta:
                            ans.append(x)
                            digits -= 1
                            break
                        count += delta
                return "".join(map(str, ans))

            count += delta


print(solve(K))
