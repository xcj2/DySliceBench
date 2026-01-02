# ABC161d


def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**6)
    # 再帰関数を使わない限りPypyで出すこと

    def dump(*args):
        sys.stderr.write(str(args))

    k = int(input())

    def isOk(n):
        n = str(n)
        for i in range(len(n)):
            if (i+1 < len(n) and abs(int(n[i]) - int(n[i + 1])) > 1 or i+2 < len(n) and abs(int(n[i + 1]) - int(n[i + 2])) > 1):
                return False
        return True

    def swap(n, i, f):
        ori = n
        ns = str(n)
        try:
            t = ns[-i-1]
            w = ns[-i - 2]
        except:
            s = int(f) + 1
            l = len(ns)
            if s == 10:
                l += 1
            a = ''
            for i in range(s, -1, -1):
                a += str(i)
            a += '0'*(l-len(a))
            return int(a[:l])
        if t == w:
            return swap(n, i+1, f)
        n -= int(t) * 10 ** i
        n -= int(w)*10**(i+1)
        n += int(t) * 10 ** (i + 1)
        n += int(w) * 10 ** (i)
        l = len(ns)
        a = str(n)[:-i-1]
        for i in range(int(a[-1])-1, -1, -1):
            a += str(i)
        a = a[:l]
        a += '0'*(l-len(a))
        n = int(a[:l])
        if not isOk(n):
            return swap(ori, i+1, f)
        return n

    def calc(n, I):
        if isOk(n):
            return n
        n -= 10**I
        n += 10 ** (I + 1)
        a = str(n)[: -I - 1]
        l = len(str(n))
        for i in range(int(a[-1])-1, -1, -1):
            a += str(i)
        a = a[:l]
        a += '0'*(l-len(a))
        n = int(a[:l])
        return calc(n, I+1)

    dp = [0] * (k+1)
    ind = 0
    for i in range(k):
        # if i == 43:
            # print('hi')
        dp[i + 1] = calc(dp[i] + 1, 0)
        # if dp[i] == 123:
        # print('hi')

        # if not isOk(dp[i + 1]):
        #    dp[i + 1] = swap(dp[i], 0, str(dp[i])[0])
        #print(i, dp[i + 1])
        # if i == 990:
        # print('hi')
    print(dp[k])


if __name__ == '__main__':
    main()
