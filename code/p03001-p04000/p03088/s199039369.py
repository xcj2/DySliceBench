
dp = []
mod = 10 ** 9 + 7

def check(pre_3, pre_2, pre_1, now_num):
    if pre_2 == 0 and pre_1 == 2 and now_num == 1:
        return 1
    if pre_2 == 2 and pre_1 == 0 and now_num == 1:
        return 1
    if pre_2 == 0 and pre_1 == 1 and now_num == 2:
        return 1
    if pre_3 == 0 and pre_2 == 2 and now_num == 1:
        return 1
    if pre_3 == 0 and pre_1 == 2 and now_num == 1:
        return 1
    return 0

def print_ans(num):
    global dp, mod
    count = 0
    for pre_3 in range(4):
        for pre_2 in range(4):
            for pre_1 in range(4):
                count += dp[num][pre_3][pre_2][pre_1]
    print(count % mod)

# 0:'A', 1:'C', 2:'G', 3:'T'
def start_process(num):
    global dp, mod
    dp = [[[[0, 0, 0, 0] for k in range(4)] for j in range(4)] for i in range(num + 1)]
    dp[0][3][3][3] = 1
    for char_num in range(num):
        for pre_3 in range(4):
            for pre_2 in range(4):
                for pre_1 in range(4):
                    for now_num in range(4):
                        if check(pre_3, pre_2, pre_1, now_num):
                            continue
                        dp[char_num + 1][pre_2][pre_1][now_num] += dp[char_num][pre_3][pre_2][pre_1]
                        dp[char_num + 1][pre_2][pre_1][now_num] %= mod
    print_ans(num)

def main():
    num = int(input())
    start_process(num)

if __name__ == '__main__':
    main()
