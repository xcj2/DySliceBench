
def reverse(s): 
    return s[::-1] 
  
def isPalindrome(s): 
    
    rev = reverse(s) 
  
    if (s == rev): 
        return True
    return False
def listToString(s):  

    str1 = ""  
    for ele in s:  
        str1 += ele   
   
    return str1   
    
s=input()
n = len(s)
p=int(round((n-1)/2))
q=int(round((n+3)/2))
ans = isPalindrome(s)


t1=[]
t2=[]

for i in range(0,p):
    t1.append(s[i])
for i in range(q-1,n):
    t2.append(s[i])    

ans1=isPalindrome(listToString(t1))
ans2=isPalindrome(listToString(t2))
if (ans==1 and ans1==1 and ans2==1):
    print ("Yes")
    
else:
    print("No")
   