import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))

INF=10**20
def main():
    N,K=mi()
    P=list(mi())
    C=list(mi())

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





if __name__ == "__main__":
    main()