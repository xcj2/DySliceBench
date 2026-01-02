from sys import stdin
import math
import itertools


def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

# これだと、O(n*n)
"""
temp_ans = []


def problem_a(input_string):
    S = int(input_string[0].rstrip())
    N = input_string[1].rstrip()
    N_l = len(N)
    global temp_ans
    for i in range(N_l)[::-1]:
        temp_ans += N[i]
        #print(temp_ans)
        for s in temp_ans:
            #print(s)
            if N[i] not in s:
                temp_ans.append(N[i]+s)
    #print(temp_ans)
    return len(temp_ans) % (10**9 + 7)
"""


def problem_a(input_string):
    S = int(input_string[0].rstrip())
    N = input_string[1].rstrip()
    #print(S)
    dic = {}
    c = 0
    for i in range(S)[::-1]:
        if N[i] not in dic:
            dic[N[i]] = 1
            #c += i+1
        else:
            dic[N[i]] += 1

    c = 1
    for key, value in dic.items():
        c *= (value+1)
    c -= 1
    """
    c += 2**len(dic.keys())-1
    #print(c)
    #c += S
    for key, value in dic.items():
        if value > 1:
            #c -= (value-1)
            c += 2**(len(dic.keys()))-1
            #print(c)
    #for key, value in dic.items():
    for key, value in dic.items():
        if value > 1:
            if len(dic.keys()) != S:
                c -= 2**(S-len(dic.keys())-1)
    """
            #print(c)
        #else:
    #c += (S-len(dic.keys()))
    """
    s_N = sorted(N)
    for i in range(S-1):
        if s_N[i] != s_N[i+1]:
            c += 2**(i+2)
    """
    """
    for key, value in dic.items():
        if value > 1:
            c += 2**(len(dic.items())-value)
        else:
            c += 2**(len(dic.items())-value)
    """
    #combinations_count(len(, r)

    return c % (10**9 + 7)


def main():
    input_line = stdin.readlines()
    answer = problem_a(input_line)
    print(answer)


if __name__ == '__main__':
    main()
