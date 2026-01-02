# Enter your code here. Read input from STDIN. Print output to STDOUT

def find(x):
    dic={}
    
    def fact(t):
        T=int(t**0.5)+1
        for i in range(2,T):
            if t%i==0:
                if i in dic:
                    dic[i]+=1
                else:
                    dic[i]=1
                return i
        if t in dic:
            dic[t]+=1
        else:
            dic[t]=1            
        return t

    while x>1:
        #print(x)
        x=int(x/fact(x))
        #print(x)
    return dic

def find_ans(N,P):
    dic=find(P)
    ans=1
    for x in dic:
        ans*=pow(x,dic[x]//N)
    return ans    

N,P=list(map(int,input().split(" ")))
print(find_ans(N,P))