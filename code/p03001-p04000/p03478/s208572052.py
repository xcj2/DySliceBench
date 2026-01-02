# coding: utf-8
"""this is python work script"""
def sum_num(i):
    sum_tmp = 0
    p = i
    for _ in range(5):
        p, mod = divmod(p, 10)
        sum_tmp += mod
        if p == 0:
           break
    return sum_tmp

def solve(N, num_min, num_max):
    """solve problem"""
    result = 0
    for i in range(1, N+1):
        sum_tmp = sum_num(i)
        if num_min <= sum_tmp and sum_tmp <= num_max:
            result += i
    return result

def main():
    N, A, B = list(map(int, input().rstrip().split(' ')))
    answer = solve(N, A, B)
    print(answer)

if __name__ == '__main__':
    main()
