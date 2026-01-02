#! /usr/bin/env python3
import sys
sys.setrecursionlimit(10**9)


INF=10**20
def solve(N: int, K: int, P: "List[int]", C: "List[int]"):
    ans = -INF
    for i in range(N):
        start = i + 1 
        stack = [start]
        score_his = [0]
        scores = 0
        depth = 1
        seen = {}
        while stack:
            if depth > K: break
            current = stack.pop()
            
            if current in seen:
                loop_start_depth = seen[current]
                loop_end_depth = depth - 1 
                loop_scores = score_his[-1] - score_his[loop_start_depth-1]
                loop_len = loop_end_depth - loop_start_depth + 1
                if loop_scores < 0: break
 
                # print(start,score_his)
                # print(loop_start_depth,loop_end_depth,loop_scores,loop_len)
                
                rest_count = K - depth + 1
                available_loop_count = rest_count // loop_len
                res1 = (available_loop_count-1) * loop_scores + scores
 
                # print("a",rest_count,available_loop_count,res1)
                
                res2 = res1
                rest_loop_len = rest_count % loop_len + loop_len
 
                # print("b",rest_loop_len)
                ress = [res1,res2]
                for j in range(rest_loop_len):
                    score = C[P[current-1]-1]
                    res2 += score
                    ress.append(res2)
                    current = P[current-1]
 
                # print("ress",ress)
                score_his.append(max(ress))
 
                break
 
            
            score = C[P[current-1]-1]
            scores += score
            score_his.append(scores)
 
            seen[current] = depth
            stack.append(P[current-1])
 
            depth += 1
        
        ans = max(ans,max(score_his[1:]))
    
    print(ans)
 
 
    return

def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, P, C)



if __name__ == "__main__":
    main()
