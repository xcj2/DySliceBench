def main():
    n = int(input().strip())
    s = list(input().strip())

    bit = [[0] * 26 for _ in range(n + 1)]

    def query(i):
        result = [0] * 26
        while i:
            for j, x in enumerate(bit[i]):
                result[j] += x
            i -= i & -i
        return result
    
    def update(i, c, val):
        j = ord(c) - ord("a")
        while i < len(bit):
            bit[i][j] += val
            i += i & -i

    for i, c in enumerate(s, 1):
        update(i, c, 1)

    q = int(input().strip())
    for _ in range(q):
        Q = input().strip().split()
        if Q[0] == "1":
            i, c = int(Q[1]), Q[2]
            update(i, s[i - 1], -1)
            update(i, c, 1)
            s[i - 1] = c
        else:
            l, r = int(Q[1]), int(Q[2])
            cnt = [x - y for x, y in zip(query(r), query(l - 1))]
            print(sum(x > 0 for x in cnt))


main()
