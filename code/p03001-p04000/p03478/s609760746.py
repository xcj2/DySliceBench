# coding: utf-8
"""this is python work script"""

def sum_digits(i):
    """return sum input digits"""
    sum_tmp = 0
    quotient = i

    for _ in range(5):
        quotient, mod = divmod(quotient, 10)
        sum_tmp += mod
        if quotient == 0:
            break
    return sum_tmp

def solve(N, num_min, num_max):
    """solve problem"""
    result = 0
    for i in range(1, N+1):
        sum_d = sum_digits(i)
        if num_min <= sum_d <= num_max:
            result += i
    return result

def main():
    """main method"""
    N, A, B = list(map(int, input().split(' ')))
    answer = solve(N, A, B)
    print(answer)

if __name__ == '__main__':
    main()
