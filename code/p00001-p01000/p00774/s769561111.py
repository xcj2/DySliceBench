# https://onlinejudge.u-aizu.ac.jp/problems/1193
def delete(M):
    point = 0
    for row in M:
        for l in range(len(row)-1):
            for r in range(l + 1, len(row)):
                if row[l] != row[r]:
                    break
            if r - l >= 3:
                point += (r - l) * row[l]
                for i in range(l, r):
                    row[i] = 0
                break

    return point


def drop(M):
    for c in range(5):
        nums = []
        for i in range(len(M)-1, -1, -1):
            if M[i][c] != 0:
                nums.append(M[i][c])
            M[i][c] = 0

        for i in range(len(nums)):
            M[len(M)-1-i][c] = nums[i]


def solve(h, M):
    result = 0
    while True:
        point = delete(M)
        if point == 0:
            break
        result += point
        # print('-------')
        # for row in M:
        #     print(*row)
        # print('--drop-----')
        drop(M)
        # for row in M:
        # print(*row)
        # print('-------')
    print(result)


if __name__ == "__main__":
    while True:
        h = int(input())
        if h == 0:
            break
        M = [list(map(int, input().split())) + [0] for _ in range(h)]
        solve(h, M)

