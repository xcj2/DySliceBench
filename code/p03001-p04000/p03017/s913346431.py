n,a,b,c,d = map(int,input().split())
S = input()
 
ans = 0
def aaa(s,g):
    global ans
    if S[s:g].count("##") == 0:
        ans += 1
    
def bbb(s,g):
    global ans
    if S[s:g].count("##") == 0:
        ans += 1
        return(1)
    else:
        return(0)

def ccc(s,g):
    global ans
    if S[s:g].count("##") == 0:
        return(1)
    else:
        return(0)
        
if c < d:
    aaa(b,d)
    aaa(a,c)
else:
    flag = bbb(b,d)
    flag2 = ccc(a,c)
 #   print(ans)
    if flag == 1 and flag2 == 1:
        for i in range(b,d+1):
      #      print(i)
            if S[i-1:i] != "#":
                k = S[i-2:i-1] + "#" + S[i:i+1]
      #          print(k,i)
                if k.count("##") == 0:
                    ans += 1
                    break
#    print(flag)
#    print(ans)
 
if ans == 2:
    print("Yes")
else:
    print("No")