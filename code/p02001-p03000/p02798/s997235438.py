#This function merges two sorted arrays and returns inversion count in the arrays.*/ 
def merge(arr, temp, left, mid, right): 
    inv_count = 0
  
    i = left #i is index for left subarray*/ 
    j = mid #i is index for right subarray*/ 
    k = left #i is index for resultant merged subarray*/ 
    while ((i <= mid - 1) and (j <= right)): 
        if (arr[i] <= arr[j]): 
            temp[k] = arr[i] 
            k += 1
            i += 1
        else: 
            temp[k] = arr[j] 
            k += 1
            j += 1
  
            #this is tricky -- see above explanation/ 
            # diagram for merge()*/ 
            inv_count = inv_count + (mid - i) 
  
    #Copy the remaining elements of left subarray 
    # (if there are any) to temp*/ 
    while (i <= mid - 1): 
        temp[k] = arr[i] 
        k += 1
        i += 1
  
    #Copy the remaining elements of right subarray 
    # (if there are any) to temp*/ 
    while (j <= right): 
        temp[k] = arr[j] 
        k += 1
        j += 1
  
    # Copy back the merged elements to original array*/ 
    for i in range(left,right+1,1): 
        arr[i] = temp[i] 
  
    return inv_count 
  
#An auxiliary recursive function that sorts the input 
# array and returns the number of inversions in the 
# array. */ 
def _mergeSort(arr, temp, left, right): 
    inv_count = 0
    if (right > left): 
        # Divide the array into two parts and call 
        #_mergeSortAndCountInv() 
        # for each of the parts */ 
        mid = int((right + left)/2) 
  
        #Inversion count will be sum of inversions in 
        # left-part, right-part and number of inversions 
        # in merging */ 
        inv_count = _mergeSort(arr, temp, left, mid) 
        inv_count += _mergeSort(arr, temp, mid+1, right) 
  
        # Merge the two parts*/ 
        inv_count += merge(arr, temp, left, mid+1, right) 
  
    return inv_count 
  
#This function sorts the input array and returns the 
#number of inversions in the array */ 
def countSwaps(arr, n): 
    temp = [0 for i in range(n)] 
    return _mergeSort(arr, temp, 0, n - 1) 


from itertools import combinations, zip_longest

N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

cards = [(a,b) if i % 2 == 0 else (b,a) for i,(a,b) in enumerate(zip(A,B))]

best = float('inf')

for odd_indices in combinations(range(N), N//2):
    odds = sorted((cards[i][1], i) for i in odd_indices)
    evens = sorted((card[0], i) for i,card in enumerate(cards) if i not in odd_indices)


    union = []
    for e,o in zip_longest(evens,odds):
        union.append(e)
        if o is not None:
            union.append(o)
    if all(a <= b for (a,_),(b,_) in zip(union,union[1:])):
        indices = [i for _,i in union]
        best = min(best, countSwaps(indices, N))

if best == float('inf'):
    print(-1)
else:
    print(best)