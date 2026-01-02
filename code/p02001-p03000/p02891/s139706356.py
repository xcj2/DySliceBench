s=input()
k=int(input())
code_list = 'abcdefghijklmnopqrstuvwxyz'

def c1(s):#len(s)>1
  count1=0
  S = list(s)
  l_s=len(S)
  for i in range(1,l_s):
    #print(S,count)
    if S[i]==S[i-1] and i<l_s-1:
      for j in code_list:
        if j != S[i+1] and j !=S[i-1]:
          S[i]=j
          count1+=1
          break
    elif S[i]==S[i-1]:
      for j in code_list:
        if j != S[i-1] and j !=S[0]:
          S[i]=j
          count1+=1
          break
  return count1,S[-1]

def c2(s,last):#k>2 and len(s)>1
  S=list(s)
  count2=0
  l_s=len(S)
  for i in range(0,l_s):
    #print(S,count)
    if i==0:
      if S[0]==last:
        for j in code_list:
          if j != S[i+1] and j !=last:
            S[i]=j
            count2+=1
            break
    elif S[i]==S[i-1] and i<l_s-1:
      for j in code_list:
        if j != S[i+1] and j !=S[i-1]:
          S[i]=j
          count2+=1
          break
    elif S[i]==S[i-1]:
      for j in code_list:
        if j != S[i-1] and j !=S[0]:
          S[i]=j
          count2+=1
          break
  return count2,S[-1]

def c3(s,last):#k>1 len(s)>1
  S=list(s)
  count3=0
  l_s=len(S)
  for i in range(0,l_s):
    #print(S,count)
    if i==0:
      if S[0]==last:
        for j in code_list:
          if j != S[i+1] and j !=last:
            S[i]=j
            count3+=1
            break
    elif S[i]==S[i-1] and i<l_s-1:
      for j in code_list:
        if j != S[i+1] and j !=S[i-1]:
          S[i]=j
          count3+=1
          break
    elif S[i]==S[i-1]:
      for j in code_list:
        if j != S[i-1]:
          S[i]=j
          count3+=1
          break
  return count3

if len(s)==1:
  print(k//2)
elif k==1:
  c,_=c1(s)
  print(c)
elif k==2:
  count1,last=c1(s)
  count3=c3(s,last)
  print(count1+count3)
else:
  if k%2==0:
    count1,last=c1(s)
    count21,last21=c2(s,last)
    count22,last22=c2(s,last21)
    count3=c3(s,last22)
    #print(count1,count2,count3)
    print(count1+count21*((k-2)//2)+count22*((k-2)//2)+count3)
  else:
    count1,last=c1(s)
    count21,last21=c2(s,last)
    if k>3:
      count22,last22=c2(s,last21)
    else:
      count22=0
    count3=c3(s,last21)
    #print(count1,count21,count22,count3)
    print(count1+count21*((k-2)//2+1)+count22*((k-2)//2)+count3)