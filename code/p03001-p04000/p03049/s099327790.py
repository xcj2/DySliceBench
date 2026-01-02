import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = input_int()
    cnt = {"_A": 0, "B_": 0, "B_A": 0}
    ans = 0
    for _ in range(n):
        s = input()
        if s[0] == "B" and s[-1] == "A":
            cnt["B_A"] += 1
        elif s[0] == "B":
            cnt["B_"] += 1
        elif s[-1] == "A":
            cnt["_A"] += 1
        # 含まれるABを探す
        for i in range(len(s) - 1):
            if s[i:i + 2] == "AB":
                ans += 1

    # 接続することで作れるABを探す
    # B_Aで貪欲にABを作る
    if cnt["B_A"] > 1:
        ans += cnt["B_A"] - 1
        cnt["B_A"] = 1
    # B_A,_A,B_の組み合わせを作る
    if cnt["_A"] > 0 and cnt["B_"] > 0 and cnt["B_A"] > 0:
        ans += 2
        cnt["_A"] -= 1
        cnt["B_"] -= 1
        cnt["B_A"] -= 1
    # 残りで作る

    ans += min(sorted([cnt["_A"], cnt["B_"], cnt["B_A"]])[1:])

    print(ans)
    return


if __name__ == "__main__":
    main()
