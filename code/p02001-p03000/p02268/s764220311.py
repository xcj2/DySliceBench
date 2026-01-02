def solve(s_list, t_list):
    ans = 0
    s_length = len(s_list)
    for t in t_list:
        left, right = 0, s_length
        if binary_search(s_list, left, right, t):
            ans += 1
    return ans


def binary_search(s_list, left, right, t):
    # [left, right)
    if right > left:
        mid = (left + right) // 2
        if s_list[mid] == t:
            return True
        elif s_list[mid] > t:
            right = mid
        else:
            left = mid + 1
        return binary_search(s_list, left, right, t)
    return False


def main():
    n = int(input())
    s_list = list(map(int, input().split()))
    q = int(input())
    t_list = list(map(int, input().split()))

    ans = solve(s_list, t_list)
    print(ans)


main()

