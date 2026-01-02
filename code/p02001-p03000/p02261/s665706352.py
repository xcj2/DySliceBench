def str_selection_sort(a,n):
    m=0
    for i in range(0,n):
        minj=i
        for j in range(i,n):
            if(int(a[minj][1:]) > int(a[j][1:])):
                minj=j
        if(minj!=i):
            m+=1
            a[minj],a[i] = a[i],a[minj]
        
    print(" ".join(a))
    return a

def str_bubble_sort(a,n):
    m=0
    flag=True
    while(flag):
        flag=False
        for i in range(n-1,0,-1):
            if(a[i-1][1:] > a[i][1:]):
                tmp=a[i-1]
                a[i-1]=a[i]
                m+=1
                a[i]=tmp
                flag=True
                
    print(" ".join(a))
    return a

def is_stable(a,b,n):
    for i in range(1,n):
        if(b[i-1][1:]!=b[i][1:]):
            continue
        flag=False
        for j in a:
            if(j[:1]==b[i-1][:1] and (not flag)):
                flag=True
                continue
            if(j[:1]==b[i][:1]):
                if(not flag):
                    return False
                else:
                    return True
        
        if(flag):
            return False
    return True

a=[]
n=int(input())
s=input()
a=s.split()
b=str_bubble_sort(list(a),n)
print("Stable")
c=str_selection_sort(list(a),n)
if(b==c):
    print("Stable")
else:
    print("Not stable")