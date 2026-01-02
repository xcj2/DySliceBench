def solve(lis):
    # 全要素が0の場合
    if is_all_zero(lis):
        return 0

    # 0がある場合、0を境に分割
    zero_index = search_zero_index(lis)
    if zero_index != -1:
        return solve(lis[:zero_index]) + solve(lis[zero_index+1:])

    # 0が無い場合、最小値の数をリスト全体から引く
    min_num = min(lis)
    lis = list(map(lambda x: x - min_num, lis))
    return min_num + solve(lis)

def is_all_zero(lis):
    return len(list(filter(lambda x : x == 0, lis))) == len(lis)

def search_zero_index(lis):
    if 0 in lis:
        return lis.index(0)
    else:
        return -1

if __name__ == "__main__":
    N = int(input())
    h_list = list(map(int, input().split()))
    print(solve(h_list))
