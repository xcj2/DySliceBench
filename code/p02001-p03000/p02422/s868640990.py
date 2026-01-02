def ss_reverse(ss,a,b):
    rev = ss[a:b+1]
    rev = rev[::-1]
    edited = ss[:a] + rev + ss[b+1:]
    return edited

def ss_replace(ss,a,b,word):
    edited = ss
    edited= ss[:a] + word + ss[b+1:]
    return edited

def print_result(ss,a,b):
    print(ss[a:b+1])

ss = input()
n = int(input())

for i in range(n):
    I = input().split()
    if len(I) == 4:
        ss = ss_replace(ss,int(I[1]),int(I[2]),I[3])
    
    if I[0] == "reverse" :
        ss = ss_reverse(ss,int(I[1]),int(I[2]))

    if I[0] == "print" :
        print_result(ss,int(I[1]),int(I[2]))
    

