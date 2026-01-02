from sys import stdin

def getval():
    n,m = map(int,input().split())
    ab = []
    c = []
    def tobit(arr):
        idx = len(arr)-1
        s = ""
        for i in range(n-1,-1,-1):
            if arr[idx]-1==i and idx!=-1:
                s = "".join([s,"1"])
                idx -= 1
            else:
                s = "".join([s,"0"])
        return s
    for i in range(m):
        ab.append(list(map(int,stdin.readline().split())))
        c.append(tobit(list(map(int,stdin.readline().split()))))
    return n,m,ab,c 

def main(n,m,ab,c):
    dp = [-1 for i in range(2**n)]
    dp[0] = 0

    for i in range(m):
        curc = ab[i][0]
        curk = c[i]
        temp = [-1 for i in range(2**n)]
        for j in range(2**n):
            if dp[j]==-1:
                continue
            new = dp[j]
            
            update = int(curk,2)|j
            
            #print(i,j,update,new,curc,curk,s)
            target = temp[update]
            if target==-1:
                temp[update] = new+curc
            elif target>new+curc:
                temp[update] = new+curc                
            if new<temp[j] or temp[j]==-1:
                temp[j] = dp[j]
        dp = temp
        #print(dp)
    print(dp[-1])
        
                
if __name__=="__main__":
    n,m,ab,c = getval()
    main(n,m,ab,c)