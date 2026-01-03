class BIT():
    def __init__(self,n):
        self.BIT=[0]*(n+1)
        self.num=n

    def query(self,idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx&(-idx)
        return res_sum

    #Ai += x O(logN)
    def update(self,idx,x):
        while idx <= self.num:
            self.BIT[idx] += x
            idx += idx&(-idx)
        return

N=int(input())
a=[list(map(int,input().split())) for i in range(3)]
odd=[]
even=[]
for i in range(N):
    x,y,z=a[0][i],a[1][i],a[2][i]
    if x<z:
        if y!=x+1 or z!=y+1:
            print("No")
            exit()
        else:
            if i%2==0:
                if x%6==1:
                    even.append(x//6+1)
                else:
                    print("No")
                    exit()
            else:
                if x%6==4:
                    odd.append(x//6+1)
                else:
                    print("No")
                    exit()
    else:
        if y!=x-1 or z!=y-1:
            print("No")
            exit()
        else:
            if i%2==0:
                if z%6==1:
                    even.append(-(z//6)-1)
                else:
                    print("No")
                    exit()
            else:
                if z%6==4:
                    odd.append(-(z//6)-1)
                else:
                    print("No")
                    exit()

oddsign=0
ODD=[(abs(odd[i]),i) for i in range(len(odd))]
ODD.sort()
for i in range(len(odd)):
    val,id=ODD[i]
    check=(id-i)%2
    if check==1:
        oddsign+=(odd[id]>0)
    else:
        oddsign+=(odd[id]<0)

evensign=0
EVEN=[(abs(even[i]),i) for i in range(len(even))]
EVEN.sort()
for i in range(len(even)):
    val,id=EVEN[i]
    check=(id-i)%2
    if check==1:
        evensign+=(even[id]>0)
    else:
        evensign+=(even[id]<0)

oddbit=BIT(len(odd))
check=0
for i in range(len(odd)):
    v=abs(odd[i])
    check+=i-oddbit.query(v)
    oddbit.update(v,1)

if check%2!=evensign%2:
    print("No")
    exit()

evenbit=BIT(len(even))
check=0
for i in range(len(even)):
    v=abs(even[i])
    check+=i-evenbit.query(v)
    evenbit.update(v,1)

if check%2!=oddsign%2:
    print("No")
    exit()

print("Yes")
