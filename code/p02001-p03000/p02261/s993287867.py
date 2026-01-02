import copy
def bubble_sort(nums,n):
    flag=1
    while flag:
        flag=0
        for i in range(n-1,0,-1):
            if int(nums[i][1])<int(nums[i-1][1]):
                flag=1
                nums[i],nums[i-1]=nums[i-1],nums[i]

    return nums

def selection_sort(nums,n):
    for i in range(n):
        minj=i
        for j in range(i+1,n):
            if nums[j][1]<nums[minj][1]:
                minj=j
        nums[minj],nums[i]=nums[i],nums[minj]

    return nums

n=int(input())
nums=list(input().split())
nums_2=copy.deepcopy(nums)
b_nums=bubble_sort(nums,n)
s_nums=selection_sort(nums_2,n)

def show(nums):
    for i in range(len(nums)):
        if i!=len(nums)-1:
            print(nums[i],end=' ')

        else:
            print(nums[i])

show(b_nums)
print("Stable")
show(s_nums)
if b_nums==s_nums:
    print("Stable")

else:
    print("Not stable")
