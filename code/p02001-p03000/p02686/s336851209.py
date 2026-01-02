import sys
input=sys.stdin.readline

def count(s):
    m=0
    e=0
    for t in s:
        if t=='(':
            e+=1
        else:
            e-=1
            m=min(m,e)
    return (e,m)
def count_reverse(s):
    m=0
    e=0
    for t in s[::-1]:
        if t==')':
            e+=1
        else:
            e-=1
            m=min(m,e)
    return (e,m)

def main():
    n=int(input())
    S=[input().strip() for _ in range(n)]
    P,M=[],[]
    Z=[0]
    for s in S:
        e,m=count(s)
        if e>0:
            P.append((m,e))
        elif e<0:
            e,m=count_reverse(s)
            M.append((m,e))
        else:
            Z.append(m)
    P.sort(reverse=True); M.sort(reverse=True)
    s_p,s_m=0,0
    for m,e in P:
        if s_p+m<0:
            return 'No'
        s_p+=e
    for m,e in M:
        if s_m+m<0:
            return 'No'
        s_m+=e
    if s_p==s_m and s_p+min(Z)>=0:
        return 'Yes'
    return 'No'

if __name__=='__main__':
    print(main())