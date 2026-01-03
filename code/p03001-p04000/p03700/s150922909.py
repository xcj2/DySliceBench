import sys
import math

# 再帰
def solve_rec(n, a, b, h_lst, ans_min, ans_max):
    if ans_min == ans_max:
        return ans_min

    if ans_min > ans_max:
        return -1

    pivot = (ans_min + ans_max) // 2
    # print("try: {}".format(pivot))
    is_beatable = beatable(a, b, h_lst, pivot)

    if is_beatable:
        # print("beatable: {} {}".format(ans_min, ans_max))
        return solve_rec(n, a, b, h_lst, ans_min, pivot)
    else:
        # print("not beatable: {} {}".format(ans_min, ans_max))
        return solve_rec(n, a, b, h_lst, pivot+1, ans_max)

def beatable(a, b, h_lst, pivot):
    # まずBずつ削る
    living = [ h - b * pivot for h in h_lst if h > b * pivot ]
    # print(living)

    # 生き残ったものを1回ずつ(A-B)ダメージずつ与えていくときに、必要な回数
    c = sum([ math.ceil(1.0 * h / (a-b)) for h in living ])
    
    return c <= pivot

def solve(n, a, b, h_lst):
    h_max = max(h_lst)
    ans_min = 0
    ans_max = h_max // b + 1

    return solve_rec(n, a, b, h_lst, ans_min, ans_max)

def main():
    line = sys.stdin.readline()
    lst = line.split()
    n = int(lst[0])
    a = int(lst[1])
    b = int(lst[2])

    h_lst = []
    for i in range(n):
        line = sys.stdin.readline()
        h = int(line)
        h_lst.append(h)
        

    ans = solve(n, a, b, h_lst)
    print(ans)

if __name__ == '__main__':
    main()
