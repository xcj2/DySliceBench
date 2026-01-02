# coding: utf-8
# Your code here!
# coding: utf-8
import sys
sys.setrecursionlimit(10000000)

#const
# my functions here!
def pin(type=int):
    return map(type,input().rstrip().split())
"""
def resolve():
    a,b,c=pin()
    from math import sqrt
    cond =(c-a-b)>sqrt(a*b)*2
    print(["No","Yes"][cond])
"""
def resolve():
    N,=pin()
    from collections import deque
    from collections import Counter
    ans=deque([["a",1]])
    L=1
    abc="abcdefghij"
    #("str",chars in str)のリスト？
    if N>1:
        for i in range(2,N+1):
            while(len(ans[0][0])<N):
                temp=ans.popleft() 
                string,types=temp
                for y in range(types+1):
                    temp2=string
                    temp2+=abc[y]
                    count=Counter(temp2)
                    
                    ans.append([temp2,len(count)])
                    
    for A in ans:
        print(A[0])
"""
#printデバッグ消した？
#前の問題の結果見てないのに次の問題に行くの？
"""
"""
お前カッコ閉じるの忘れてるだろ
"""
if __name__=="__main__":resolve()