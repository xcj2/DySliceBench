# O(n^2)解法 サンプルテスト用
def sample():
    cnt = 0
    for i in range(N):
        for j in range(i+1,N+1):
            part = A[i:j]
            if sum(part) % M == 0:
                cnt += 1
    return cnt 

def candidate():
    import itertools
    from collections import Counter
    acc = itertools.accumulate(A)
    acc = [e % M for e in acc]
    cnt_dict = {}
    res = 0
    for e in acc:
        if e == 0:
            res += 1
        if e in cnt_dict:
            cnt_dict[e] += 1
        else:
            cnt_dict[e] = 0
        res += cnt_dict[e]
    return res
    
def run():
    sample_ans = sample()
    candidate_ans = candidate()
    print("sample:",sample_ans,end = ", ")
    print("candidate:",candidate_ans)
    if sample_ans == candidate_ans:
        print("candidateの解法は正しいです")
    else:
        print("candidateの解法は誤りです") 

N,M = map(int,input().split())
A = list(map(int,input().split()))
print(candidate())