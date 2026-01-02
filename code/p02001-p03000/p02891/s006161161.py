import copy

S = list(input())
K = int(input())

#両端が異なる
def listCount(S,K):
    box = "" #１つ前の文字を格納
    count=0 #f(0):重複ペアをカウント

    for mozi in S:
        if box != mozi:
            box = mozi
        else:
            count += 1
            box=""
            
    return count
  
#両端が同じ全部同じ文字じゃない
def listCount_dash(S,K):
    box =""
    S_origin = copy.deepcopy(S)
    
    #Sの後ろから前まで試行
    for k in range(0,len(S)-1):
        #もし先頭と最後尾が同じならque
        if S[0] == S[len(S)-1]:
            S.append(S[0])
            S.pop(0)
        else:
            break
        
    return listCount(S,K)*(K-1) + listCount(S_origin,K)
  
#両端が全部同じ
def listCount_dou(S,K):
    S_origin = copy.deepcopy(S)
    S.extend(S)
    return listCount(S,K)*int(K/2) + listCount(S_origin,K)*(K%2)
  
flag = 1
box=S[0]
for mozi in S:
    if box != mozi:
        flag = 0
        break
    box = mozi

if flag==0 and S[0] != S[len(S)-1]:
    #両端が異なる場合
    ans = listCount(S, K)*K
elif flag==0:
    #両端が同じ場合
    ans = listCount_dash(S, K)
else:
    #文字が全部同じ
    ans = listCount_dou(S,K)
    
print(ans)