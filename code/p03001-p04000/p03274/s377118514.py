import sys
def input(): return sys.stdin.readline().rstrip()

def solve(l, m):
    if l < m:
        return l * 2 + m
    else:
        return l + m * 2

def main():
    N, K = map(int, input().split())
    x = tuple(map(int, input().split()))
    right_x = [i for i in x if i >= 0][:K]
    left_x = [-i for i in x if i < 0][-K:]

    left_len = len(left_x)
    right_len = len(right_x)
    if right_len < K:
        right_x += [10 ** 9 + 1] * (K - right_len)
    if left_len < K:
        left_x = [10 ** 9 + 1] * (K - left_len) + left_x

    right_x = [0] + right_x
    left_x += [0]

    ans = 10 ** 9
    for i in range(K + 1):
        tmp_ans = solve(left_x[i], right_x[i])
        if tmp_ans < ans:
            ans = tmp_ans
    print(ans)

if __name__ == '__main__':
    main()
