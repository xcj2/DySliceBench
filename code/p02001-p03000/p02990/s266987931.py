# パスカルの三角形
def pascal_triangle(n):
    pascal =[[]]
    pascal[0].append(1)
    for i in range(1, n + 1):
        pascal[i - 1].append(0)
        pascal.append([])
        for j in range(i + 1):
            pascal[i].append((pascal[i - 1][j - 1] + pascal[i - 1][j]) % (10**9 + 7))
    return pascal

# n個からr個を選ぶ組合せ
def comb(n, r, pascal_triangle):
    r = min(r, n - r)
    if r == 0:
        return 1
    if r == 1:
        return n
    result = pascal_triangle[n][r]
    return result

# n種類からr個を選ぶ重複組合せ
def homo(n, r, pascal_triangle):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return comb(n + r - 1, r, pascal_triangle)

def main(n, k, i, pascal_triangle):
    # 青玉k個のうち、まずi箇所に1個ずつ配置
    # 残りの(k - i)個を、ゼロを許容してi箇所に配置 => i種類から(k - i)個を選ぶ重複組合せ
    result = homo(i, k - i, pascal_triangle)
    # 赤玉(n - k)個のうち、まず(i - 1)個は青玉を区切るために配置
    # 残りの(n - k - i + 1)個を、ゼロを許容して(i + 1)箇所に配置 => (i + 1)種類から(n - k - i + 1)個を選ぶ重複組合せ
    # ただし、そもそも赤玉が(i - 1)個未満の場合は、論外
    if (n - k) < (i - 1):
        return 0
    result *= homo(i + 1, n - k - i + 1, pascal_triangle)
    result = result % (10**9 + 7)
    return int(result)

N, K = [int(x) for x in input().split()]
pascal_triangle = pascal_triangle(N)
for i in range(K):
    print(main(N, K, i + 1, pascal_triangle))