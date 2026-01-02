import sys
input=sys.stdin.readline
n=int(input())
S=input()
nagasa=len(list(S))
num=2**(nagasa-1).bit_length()
SEG=[0]*2*num
def word_num(a):
    return 1<<(ord(a)-96)
def init(S):
    for i in range(n):
        SEG[i+num-1]=word_num(S[i])
    for i in range(num-2,-1,-1) :
        SEG[i]=SEG[2*i+1]|SEG[2*i+2]
    
def update(k,x):
    k += num-1
    SEG[k] = word_num(x)
    while k:
        k-=1
        k//=2
        SEG[k] = SEG[k*2+1] | SEG[k*2+2]
    
def query(p,q):
    if q<=p:
        return 0
    p += num-1
    q += num-2
    ans=0
    while q-p>1:
        if p&1 == 0:
            ans|= SEG[p]
        if q&1 == 1:
            ans|= SEG[q]
            q -= 1
        p //=2
        q-=1
        q//=2
    if p == q:
        ans |=SEG[p]
    else:
        ans |= SEG[p]
        ans |= SEG[q]
    return ans
init(S)
q=int(input())
for i in range(q):
    a,s,t=input().split()
    if a=='1':
        s=int(s)
        update(s-1,t)
    if a=='2':
        s=int(s)
        t=int(t)
        print(bin(query(s-1,t)).count('1'))
