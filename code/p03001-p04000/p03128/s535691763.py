
def get_match_list(num_list, num_num):
    match_num_list = set()
    match_dic = [2,5,5,4,5,6,3,7,6]
    for num in num_list:
        match_num_list.add(match_dic[num-1])
    match_num_list = list(match_num_list)
    match_num_list.sort()
    return match_num_list

def get_dp(use_match_list, match_nun):
    dp = [-1 for i in range(match_nun + 1)]
    dp[0] = 0
    for i in range(2, match_nun + 1):
        for macth_bar in use_match_list:
            if dp[i-macth_bar] >= 0:
                dp[i] = dp[i-macth_bar] + 1
                break
    return dp

def print_ans(dp, match_nun, num_list):
    match_dic = [2, 5, 5, 4, 5, 6, 3, 7, 6]
    max_ketasuu = dp[match_nun]
    ans = ''
    while match_nun > 0:
        for num in num_list:
            use_match_num = match_dic[num - 1]
            if match_nun - use_match_num < 0:
                continue
            if dp[match_nun - use_match_num] == max_ketasuu - 1:
                ans += str(num)
                match_nun -= use_match_num
                max_ketasuu -= 1
                break
    print(ans)



def main():
    match_nun, num_num = map(int, input().split())
    num_list = list(map(int, input().split()))
    num_list.sort(reverse=True)
    use_match_list = get_match_list(num_list, num_num)
    dp = get_dp(use_match_list, match_nun)
    print_ans(dp, match_nun, num_list)


if __name__ == '__main__':
    main()