import sys

input=sys.stdin.readline

N,Q=map(int,input().split())
kouji=[]
for i in range(0,N):
    s,t,x=map(int,input().split())
    kouji.append([x,s,t])

d=[]
for i in range(0,Q):
    d.append(int(input()))

kouji.sort(reverse=True)

# N: 処理する区間の長さ

N0 = 2**(Q-1).bit_length()
data = [None]*(2*N0)
INF = (-1,-1)
# 区間[l, r+1)の値をvに書き換える
# vは(t, value)という値にする (新しい値ほどtは大きくなる)
def update(l, r, v):
    L = l + N0; R = r + N0
    while L < R:
        if R & 1:
            R -= 1
            data[R-1] = v

        if L & 1:
            data[L-1] = v
            L += 1
        L >>= 1; R >>= 1
# a_iの現在の値を取得
def _query(k):
    k += N0-1
    s = INF
    while k >= 0:
        if data[k]:
            s = max(s, data[k])
        k = (k - 1) // 2
    return s
# これを呼び出す
def query(k):
    return _query(k)[1]

time=0
for i in range(0,N):
    x,s,t=kouji[i]
    start=0
    end=Q-1
    while end-start>1:
        test=(end+start)//2
        if d[test]>=s-x:
            end=test
        else:
            start=test
    if d[start]>=s-x:
        l=start
    elif d[end]>=s-x:
        l=end
    else:
        l=Q

    start=0
    end=Q-1
    while end-start>1:
        test=(end+start)//2
        if t-x-1>=d[test]:
            start=test
        else:
            end=test
    if t-x-1>=d[end]:
        r=end
    elif t-x-1>=d[start]:
        r=start
    else:
        r=-1
    if r!=-1 and l!=Q and r>=l:
        update(l,r+1,(time,x))
    time+=1

for i in range(0,Q):
    print(query(i))
