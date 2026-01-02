n=int(input())
nums=list(map(int,input().split()))
count=0
def merge(nums,left,mid,right):
    global count
    inf=10**9
    L=nums[left:mid]+[inf]
    R=nums[mid:right]+[inf]
    i=0
    j=0
    for k in range(left,right):
        count+=1
        if R[j]>=L[i]:
            nums[k]=L[i]
            i+=1

        else:
            nums[k]=R[j]
            j+=1

def merge_sort(nums,left,right):
    if left+1<right:
        mid=(right+left)//2
        merge_sort(nums,left,mid)
        merge_sort(nums,mid,right)
        merge(nums,left,mid,right)

merge_sort(nums,0,n)

def show(nums):
    l=len(nums)
    for i in range(l):
        if i!=l-1:
            print(nums[i],end=" ")
            
        else:
            print(nums[i])
            
show(nums)
print(count)
