class BIT:
    def __init__(self,n):
        self.size=n
        self.tree=[0]*-~n
    def sum(self,i):
        s=0
        while i:
            s+=self.tree[i]
            i-=i&-i
        return s
    def add(self,i,x):
        while i<=self.size:
            self.tree[i]+=x
            i+=i&-i
def main():
    n=int(input())
    bit=BIT(10**5)
    for a in map(int,input().split()):
        bit.add(a,a)
    for _ in range(int(input())):
        b,c=map(int,input().split())
        t=bit.sum(b)-bit.sum(b-1)
        bit.add(b,-t)
        bit.add(c,t//b*c)
        print(bit.sum(10**5))
main()