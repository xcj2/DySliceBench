import copy

def BubbleSort(arr):
	n=len(arr)
	for i in range(n):
		for j in range(n-1,i,-1):
			if int(arr[j][1])<int(arr[j-1][1]):
				arr[j],arr[j-1]=arr[j-1],arr[j]
	return arr

def SelectionSort(arr):
	n=len(arr)
	for i in range(n):
		minp=i
		for j in range(i,n):
			if int(arr[j][1])<int(arr[minp][1]):
				minp=j
		arr[minp],arr[i]=arr[i],arr[minp]
	return arr
  
def IsStable(basearr,resultarr):
  checkarr1=[[] for _ in range(14)]
  checkarr2=[[] for _ in range(14)]
  for i in range(len(basearr)):
    checkarr1[int(basearr[i][1])].append(basearr[i][0])
    checkarr2[int(resultarr[i][1])].append(resultarr[i][0])
  if checkarr1==checkarr2:
    print('Stable')
  else:
    print('Not stable')
  

n=int(input())
arr=list(map(str,input().split()))
bubble=BubbleSort(copy.deepcopy(arr))
selection=SelectionSort(copy.deepcopy(arr))
print(' '.join(map(str,bubble)))
IsStable(arr,bubble)
print(' '.join(map(str,selection)))
IsStable(arr,selection)
