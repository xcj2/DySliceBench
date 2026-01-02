pi = 3.1415926

############ ---- USER DEFINED INPUT FUNCTIONS ---- ############
def inp():
    return(int(input().rstrip()))
def inlt():
    return(list(map(int,input().rstrip().split())))
def insr():
    s = input().rstrip()
    return(s[:len(s) - 1])
def invr():
    return(map(int,input().rstrip().split()))
################################################################
n,m,x = invr()
nums = []
ans = [10**8]

for i in range(n):
    nums.append(inlt())
    
def cal(ins):
    aaa = [0 for i in range(m)]
    cost = 0
    for i in ins:
        cost += nums[i][0]
        
        for index,j in enumerate(nums[i][1:]):
            aaa[index] += j

    for i in range(m):
        if aaa[i] < x:
            return 10**8
    else:
        return cost
    
def printCombination(arr, n, r): 
      
    # A temporary array to  
    # store all combination 
    # one by one 
    data = [0]*r; 
  
    # Print all combination  
    # using temprary array 'data[]' 
    combinationUtil(arr, data, 0,  
                    n - 1, 0, r); 
  
# arr[] ---> Input Array 
# data[] ---> Temporary array to 
#         store current combination 
# start & end ---> Staring and Ending 
#             indexes in arr[] 
# index ---> Current index in data[] 
# r ---> Size of a combination  
# to be printed  
def combinationUtil(arr, data, start,  
                    end, index, r): 
                          
    # Current combination is ready  
    # to be printed, print it 
    if (index == r):
        ins = []
        for j in range(r): 
            ins.append(data[j])

        result = cal(ins)
        if result < ans[0]:
            ans[0] = result 
        return; 
  
    # replace index with all 
    # possible elements. The 
    # condition "end-i+1 >=  
    # r-index" makes sure that  
    # including one element at 
    # index will make a combination  
    # with remaining elements at  
    # remaining positions 
    i = start;  
    while(i <= end and end - i + 1 >= r - index): 
        data[index] = arr[i]; 
        combinationUtil(arr, data, i + 1,  
                        end, index + 1, r); 
        i += 1; 
    
arr = [i for i in range(n)]
for i in range(1,n + 1):
    printCombination(arr,n,i)

print(ans[0] if ans[0] < 10**8 else -1)
    
