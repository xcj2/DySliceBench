#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(s: str, x: int, y: int):
    s_list = list(map(len,s.split("T")))
    x_s_list = s_list[0::2]
    y_s_list = s_list[1::2]

    x_dp = [set() for _ in range(len(x_s_list))]
    for index,count in enumerate(x_s_list):
        ## 最初は
        if index == 0:
            x_dp[index].add(count)
            continue
        
        for j in x_dp[index-1]:
            x_dp[index].add(j-count)
            x_dp[index].add(j+count)


    y_dp = [set() for _ in range(len(y_s_list))]
    for index,count in enumerate(y_s_list):
        ## 最初は
        if index == 0:
            y_dp[index].add(count)
            y_dp[index].add(-count)  
            continue
        
        for j in y_dp[index-1]:
            y_dp[index].add(j-count)
            y_dp[index].add(j+count)
    
    if not y_dp:
        if y != 0:
            print(NO)
        else:
            if x in x_dp[-1]:
                print(YES)
            else:
                print(NO)
        return

    if not x_dp:
        if x != 0:
            print(NO)
        else:
            if y in y_dp[-1]:
                print(YES)
            else:
                print(NO)
        return

    if x in x_dp[-1] and y in y_dp[-1]:
        print(YES)
    else:
        print(NO)

    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(s, x, y)

if __name__ == '__main__':
    main()
