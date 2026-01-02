#n = int(input())
#s = input()
#n, k= map(int,input().split())
#da = list(map(int,input().split()))
class SegTree:
    def __init__(self,n):
        self.size=1
        while(n>self.size):
            self.size<<=1
        self.nod=[0 for i in range(self.size*2-1)]
    def update(self,k,a):
        k+=self.size-1
        self.nod[k]+=a
        while(k>0):
            k=(k-1)>>1
            self.nod[k]|=a
    def dedate(self, k, a):
        k += self.size-1
        self.nod[k] -= a
        while(k>0):
            k=(k-1)>>1
            self.nod[k] = self.nod[(k<<1)|1]|self.nod[(k+1)<<1]
    def query(self,a,b,k,l,r):
        if(r<=a or b<=l):
            return 0
        if(a<=l and r<=b):
            return self.nod[k]
        else:
            return self.query(a,b,(k<<1)|1,l,(l+r)>>1)|self.query(a,b,(k+1)<<1,(l+r)>>1,r)

def pop_c(x):
    ret = 0
    while x:
        ret += x&1
        x>>=1
    return ret

n = int(input())
t = input()
q = int(input())
EE = ord('a')
st = SegTree(n)
s = [t[i] for i in range(n)]

def adding(x, c):
    global st
    st.dedate(x, 1<<(ord(s[x])-EE))
    st.update(x, 1<<(ord(c)-EE))
    s[x] = c

def query(l, r):
    now = st.query(l, r+1, 0, 0, st.size)
    return pop_c(now)

for i in range(n):
    st.update(i, 1<<(ord(s[i])-EE))
ans = []
for i in range(q):
    x,l,r = map(str,input().split())
    if x=='1':
        adding(int(l)-1, r)
    else:
        ans.append(query(int(l)-1, int(r)-1))
for i in range(len(ans)):
    print(ans[i])