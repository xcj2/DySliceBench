#!/usr/bin/env python3
import sys
import bisect

def solve(s: str, t: str):
    LENS = len(s)
    dict_s = {} ##{'c': [0], 'o': [1], 'n': [2], 't': [3, 6], 'e': [4], 's': [5]}
    index = [] ##[[5], [4], [2], [3, 6], [4], [2], [0], [4]]

    ## create dict
    for i in range(LENS):
        if dict_s.get(s[i]) != None:
            dict_s[s[i]].append(i)
        else:
            dict_s[s[i]]= [i]
    
    ## そもそもtが作れるかの判定
    for tt in t:
        if dict_s.get(tt) == None:
            print(-1)
            return
        else:
            index.append(dict_s[tt])
    
    answer = 0
    for i in range(len(index)):
        cur = index[i]

        if i == 0:
            answer += cur[0]
            index[i]=[cur[0]]
            continue

        prev = index[i-1]

        if len(cur)==1:
            if cur[0]>prev[0]:
                answer += cur[0]-prev[0]
            else:
                answer += cur[0]+LENS-prev[0] ##一周追加
        else: ##複数
            next_index = bisect.bisect_left(cur,prev[0])

            if next_index<len(cur)-1: ## prevより大きいindexがある時
                next_index += 1 if cur[next_index] == prev[0] else 0
                
                answer += cur[next_index]-prev[0]
                index[i]= [cur[next_index]]
            elif next_index==len(cur)-1:
                if prev[0]<cur[next_index]:
                    answer += cur[next_index]-prev[0]
                    index[i] =[cur[next_index]]
                elif prev[0]==cur[next_index]:
                    answer += cur[0]+LENS-prev[0]
                    index[i] =[cur[0]]
            else: ##next_index==len(cur):
                answer += cur[0]+LENS-prev[0]
                index[i] = [cur[0]]
       

    print(answer+1)
    return


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)  # type: str
    t = next(tokens)  # type: str
    solve(s, t)

if __name__ == '__main__':
    main()
