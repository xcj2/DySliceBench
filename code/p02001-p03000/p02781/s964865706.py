def main():
    s = [int(char) for char in input()]
    l = len(s)
    k = int(input())

    tmp = 0
    nonzero = []
    for number in s:
        if number > 0:
            tmp += 1
        nonzero.append(tmp)
    nonzero.append(0)  # let nonzero[-1] be 0

    def binomial(n, k):
        if n < k or n < 0 or k < 0:
            return 0
        if k == 0:
            return 1
        if k == 1:
            return n
        if k == 2:
            return n * (n-1) // 2
        if k == 3:
            return n * (n-1) * (n-2) // 6
        raise ValueError

    def dp(i, _cache={-1: 0}):
        if i in _cache:
            return _cache[i]
        if nonzero[i-1] > k or s[i] == 0:
            result = dp(i-1)
            _cache[i] = result
            return result
        if nonzero[i-1] == k:
            result = dp(i-1) + 1
            _cache[i] = result
            return result
        result = (
            dp(i-1) +
            (s[i] - 1) * binomial(l - 1 - i, k - nonzero[i-1] - 1) *
            9 ** (k - nonzero[i-1] - 1) +
            binomial(l - 1 - i, k - nonzero[i-1]) *
            9 ** (k - nonzero[i-1])
        )
        _cache[i] = result
        return result
    
    print(dp(l-1) + (nonzero[l-1] == k))


main()
