# def Swap(A,B):
#     swp = A
#     A = B
#     B = swp
#     return A,B

def BubbleSort(A):
    count = 0
    for i in range(len(A)):
        for j in range(i+1,len(A))[::-1]:
            if(A[j-1] > A[j]):
                swp = A[j-1]
                A[j-1] = A[j]
                A[j] = swp
                count += 1
                # print(A)
                # print(f"count:{count}")
                # print(f"i:{i},j:{j}")
    
    return A,count

def test(a):
    return a

def outputList(A):
    if(len(A) == 1):
        print(A[0])
    else:
        for i in range(len(A)-1):
            print(f"{A[i]} ",end="")
        print(A[-1])
        

n = int(input())
numbers = list(map(int,input().split()))
ans,count = BubbleSort(numbers)
# ans = BubbleSort(numbers)
outputList(ans)
print(count)



