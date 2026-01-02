def main():
    
    n = int(input())
    a = input().split()
    
    A = []
    for i in range(n):
        A.append(int(a[i]))
        
    display(A)
    insertSort(A)
        
def insertSort(A):
    
    for i in range(1,len(A)):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = v
        display(A)
            
def display(A):
    for i in range(len(A)):
        if i != len(A) - 1:
            endStr = ' '
        else:
            endStr = '\n'
        print(str(A[i]), end=endStr)
                
if __name__ == "__main__":
    main()

