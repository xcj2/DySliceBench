def insertion_sort(nums,n,g):
    global count
    
    for i in range(g,n):
        v=nums[i]
        j=i-g
        
        while (j>=0 and nums[j]>v):
            nums[j+g]=nums[j]
            j=j-g
            count+=1
        nums[j+g]=v


def shell_sort(nums,n):
    global count
    count=0
    m=-1
    test=0
    while test<=n:
        test=test*3+1
        m+=1
    G=[]
    h=0
    for i in range(m):
        h=h*3+1
        G.append(h)
    G.reverse()
    for i in range(m):
        insertion_sort(nums,n,G[i])
    return m,G,count,nums

def show(num):
    for i in range(len(num)):
        if i!=len(num):
            print(num[i],end=' ')
            
        else:
            print(num[i])

n=int(input())
nums=[int(input()) for j in range(n)]
answer_m,answer_G,answer_count,answer_nums=shell_sort(nums,n)
print(answer_m)
show(answer_G)
print()
print(answer_count)
for j in range(len(answer_nums)):
    print(answer_nums[j])

