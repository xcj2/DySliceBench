def solve(N, XL):
    XL_re = [[xl[0] - xl[1], xl[0] + xl[1]] for xl in XL]
    XL_re = sorted(XL_re, key=lambda x: x[1])

    cnt = 0
    for i, xl in enumerate(XL_re):
        if i == 0:
            tmp = xl[1]
            cnt += 1
        else:
            if tmp <= xl[0]:
                tmp = xl[1]
                cnt += 1
    return cnt

def test():
    assert solve(4, [[2, 4], [4, 3], [9, 3], [100, 5]]) == 3

def main():
    N = int(input())
    XL = [list(map(int, input().split())) for _ in range(N)]
    ans = solve(N, XL)
    print(ans)

if __name__ == "__main__":
    # test()
    main()
