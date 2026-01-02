def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))

N=one_int()

strs=[]
for i in range(N):
    strs.append(one_str())

count = 0
head_B=0
tail_A=0
dual_num=0
for s in strs:
    count +=s.count("AB")
    head_B += 0 if s[0]!="B" else 1
    tail_A += 0 if s[-1]!="A" else 1 
    
    if s[0]=="B" and s[-1]=="A":
        dual_num+=1
    

if N==1:
    print(count)
elif dual_num==head_B==tail_A and head_B>=1:
    print(min(head_B, tail_A) -1 +count)
else:
    print( min(head_B, tail_A)+count)