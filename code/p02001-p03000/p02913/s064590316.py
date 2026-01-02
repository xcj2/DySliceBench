import sys

input = sys.stdin.readline

def main():
    def hash_ini(t):
        h = 0
        p = 1
        for i in range(1, len(t) + 1):
            h = hash_table[i] = (h * base + t[i - 1]) % hash_md
            p = pw[i] = p * base % hash_md

    # インデックスがi以上j未満の文字列のハッシュ
    def hash_ij(i, j):
        return (hash_table[j] - hash_table[i] * pw[j - i]) % hash_md

    n = int(input())
    s = input()[:-1]

    # 初期化
    base = 31
    hash_md = pow(3, 19)
    ord_a = ord('a')
    t = [ord(c) - ord_a for c in s]
    hash_table = [0] * (len(t) + 1)
    pw = [1] * (len(t) + 1)
    hash_ini(t)

    # 長さを二分探索
    ok = 0
    ng = n // 2 + 1
    while ok + 1 < ng:
        w = (ok + ng) // 2
        hashes = []
        for i in range(w):
            hashes.append(hash_ij(i, i + w))
        passed = set()
        for i in range(w, n - w + 1):
            passed.add(hashes[i - w])
            cur = hash_ij(i, i + w)
            if cur in passed:
                ok = w
                break
            hashes.append(cur)
        else:
            ng = w

    print(ok)

main()
