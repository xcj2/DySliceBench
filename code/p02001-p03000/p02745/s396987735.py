a = input()
b = input()
c = input()

aa = len(a)
bb = len(b)
cc = len(c)

lensum = aa + bb + cc # 文字列の長さの最大値
ab = [0]*(lensum+cc+1) # 相対的位置に対して合わさるかどうかを記録
ac = [0]*(lensum+bb+1)
bc = [0]*(lensum+aa+1)

def match(v,w): # 2つの文字を合わせられるかどうかを調べる
    if(v != '?' and w != '?' and v != w):
        return 0
    else:
        return 1

def match2(A,B,k): # 2つの文字列とその相対的位置に対して合わさるかチェック
    AA = len(A)
    BB = len(B)
    if(k>=AA):
        return 1
    elif(k<-BB):
        return 1
    else:
        flg = 1
        st = max(0,k)
        la = min(AA,BB+k)
        for i in range(st,la):
            if(match(A[i],B[i-k])==0):
                flg = 0
                break
        return flg

#ab,ac,bcに対して計算する
for i in range(lensum+cc+1):
    ab[i] = match2(a,b,i-bb-cc)
for i in range(lensum+bb+1):
    ac[i] = match2(a,c,i-bb-cc)
for i in range(lensum+aa+1):
    bc[i] = match2(b,c,i-aa-cc)

def milen(a,b,c):
    minlen = lensum # 文字列の長さの最大値
    for i in range(-bb-cc,aa+cc+1): # iが文字列Bの開始位置
        for j in range(-bb-cc,aa+bb+1): # jが文字列Cの開始位置
            if(ab[i+bb+cc] == 0): 
                continue
            elif(ac[j+bb+cc] == 0):
                continue
            elif(j-i+aa+cc < 0 or j-i+aa+cc >= lensum+aa+1): #BとCが離れすぎている場合を除く
                continue  
            elif(bc[j-i+aa+cc] == 0):
                continue   
            else:
                sta = min(0,i,j) #文字列の中で一番左にある開始位置
                en = max(aa,i+bb,j+cc) #文字列の中で一番右にある終了位置
                minlen = min(minlen,en-sta) #更新
    return minlen

print(milen(a,b,c))