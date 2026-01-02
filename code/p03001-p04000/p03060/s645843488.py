
num = int(input())
data_value = list(map(int, input().split()))
data_cost = list(map(int, input().split()))
ans = 0

def ans_check(all_cost):
    global ans
    if ans < all_cost:
        ans = all_cost


def calc_ans(ind, all_cost, in_out_flg):
    if ind == num:
        ans_check(all_cost)
        return
    if in_out_flg:
        all_cost = all_cost + data_value[ind] - data_cost[ind]

    calc_ans(ind + 1, all_cost, 0)
    calc_ans(ind + 1, all_cost, 1)



def main():
    calc_ans(0, 0, 0)
    calc_ans(0, 0, 1)

    print(ans)

if __name__ == '__main__':
    main()