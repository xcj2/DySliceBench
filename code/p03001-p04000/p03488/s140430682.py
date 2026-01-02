import sys
import itertools
from itertools import accumulate
def main():
    import itertools
    def eratosthenes_sieve(n):
        table = [0] * (n + 1)
        prime_list = []
        for i in range(2, n + 1):
            if table[i] == 0:
                prime_list.append(i)
                for j in range(i + i, n + 1, i):
                    table[j] = 1
        return prime_list
        def inputs():return (int(x) for x in input().split())
    input = sys.stdin.readline
    def inputs():
        return [int(x) for x in input().split()]
    S = input()
    x,y=inputs()
    cnt=0
    s =[]
    if S[0]=="T":
        s.append(0)
        cnt+=1
    else:
        cnt+=1
    for i in range(len(S)-2):
        if S[i]==S[i+1]:
            cnt+=1
        else:
            s.append(cnt)
            cnt=1
    s.append(cnt)
    flag=1
    x1 = []
    y1 = []
    t= 0
    for i in range(len(s)):
        if i%2==0:
            if flag==1:
              if i!=0:
                x1.append(s[i])
            else:
                y1.append(s[i])
        else:
            flag=(flag+s[i])%2
            t+=s[i]
    x2 = sum(x1)+s[0]
    y2= sum(y1)
    if abs(x)>x2 or abs(y)>y2:
      print("No")
      exit()
    m = max(x2,y2,t)
    dpx=[[-1]*(m*2+5) for i in range(len(x1)+1)]
    dpx[0][m+s[0]]=1
    dpy =[[-1]*(m*2+5) for i in range(len(y1)+1)]
    dpy[0][m]=1
    for i in range(len(x1)):
        for j in range(m*2):
          if dpx[i][j]!=-1:
            if j+x1[i]<=(m)*2:
                dpx[i+1][j+x1[i]]=1
            if j-x1[i]>=0:
                dpx[i+1][j-x1[i]]=1      
    for i in range(len(y1)):
        for j in range(m*2):
          if dpy[i][j]!=-1:
            if j+y1[i]<=m*2:
                dpy[i+1][j+y1[i]]=1
                #print(j+y1[i])
            if j-y1[i]>=0:
                dpy[i+1][j-y1[i]]=1
                #print(j-y1[i])
    if dpx[len(x1)][m+x]==1 and dpy[len(y1)][m+y]==1:
        print("Yes")
    else:
        print("No")
main()
