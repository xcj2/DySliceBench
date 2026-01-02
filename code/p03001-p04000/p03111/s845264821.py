
now_ans = 100000


def kotae(A, a_tree, a_tree_sum):
    ans = (a_tree - 1) * 10 + abs(a_tree_sum - A)
    if a_tree == 0:
        ans = 100000
    return ans

def calc_final(A, B, C, a_tree, b_tree, c_tree, a_tree_sum, b_tree_sum, c_tree_sum):
    global now_ans

    ans = 0
    ans += kotae(A, a_tree, a_tree_sum)
    ans += kotae(B, b_tree, b_tree_sum)
    ans += kotae(C, c_tree, c_tree_sum)
    if ans < now_ans:
        now_ans = ans



def calc_data(tree_data, A, B, C, a_tree, b_tree, c_tree, index, a_tree_sum, b_tree_sum, c_tree_sum ):
    if a_tree_sum >= A and b_tree_sum >= B and c_tree_sum >= C:
        calc_final(A, B, C, a_tree, b_tree, c_tree, a_tree_sum, b_tree_sum, c_tree_sum)
        return
    if index == len(tree_data) - 1:
        calc_final(A, B, C, a_tree, b_tree, c_tree, a_tree_sum, b_tree_sum, c_tree_sum)
        return
    if a_tree_sum < A:
        calc_data(tree_data, A, B, C, a_tree + 1, b_tree, c_tree, index + 1, a_tree_sum + tree_data[index + 1], b_tree_sum, c_tree_sum)
    if b_tree_sum < B:
        calc_data(tree_data, A, B, C, a_tree, b_tree + 1, c_tree, index + 1, a_tree_sum, b_tree_sum + tree_data[index + 1], c_tree_sum)

    if c_tree_sum < C:
        calc_data(tree_data, A, B, C, a_tree, b_tree, c_tree + 1, index + 1, a_tree_sum, b_tree_sum, c_tree_sum + tree_data[index + 1])

    calc_data(tree_data, A, B, C, a_tree, b_tree, c_tree, index + 1, a_tree_sum, b_tree_sum, c_tree_sum)


def main():
    global now_ans
    num, A, B, C = list(map(int, input().split()))
    tree_data = [int(input()) for i in range(num)]
    tree_data.sort(reverse=True)


    calc_data(tree_data, A, B, C, 1, 0, 0, 0, tree_data[0], 0, 0)
    calc_data(tree_data, A, B, C, 0, 1, 0, 0, 0, tree_data[0], 0)
    calc_data(tree_data, A, B, C, 0, 0, 1, 0, 0, 0, tree_data[0])
    calc_data(tree_data, A, B, C, 0, 0, 0, 0, 0, 0, 0)



    print(now_ans)

if __name__ == '__main__':
    main()