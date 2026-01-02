import numpy as np
import math
import sys
sys.setrecursionlimit(10000000)

def max(a, b):
    return a if a > b else b
 
def is_match(string, pattern):
    # print(string, pattern)
    # pat_len = len(pattern)
    # skip = [pat_len for _ in range(256)]
    # for i in range(pat_len):
    #     skip[ord(pattern[i])] = pat_len - i - 1
    # i = pat_len - 1
    # while i < len(string):
    #     j = pat_len - 1
    #     while string[i] == pattern[j]:
    #         if j == 0:
    #             return True
    #         i -= 1
    #         j -= 1
    #     i = i + max(skip[ord(string[i])], pat_len-j)
    # return None
    if pattern in string:
        return True
    else:
        return False


def main():
    N = int(input())
    S = input()

    dp = [0] * N

    for i in range(1, N):
        length = dp[i - 1] + 1
        match_string = S[i - length + 1: i + 1]
        matched_string = S[:i+1-length]
        # print(match_string, matched_string)
        if is_match(matched_string, match_string):
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]
        # print(dp[i])
    
    # print(dp)
    print(dp[-1])



if __name__ == '__main__':
    main()