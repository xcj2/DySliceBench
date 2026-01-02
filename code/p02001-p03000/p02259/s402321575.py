def bubbleSort(A, N):
    count = 0
    for i in reversed(range(N)):
        for j in range(i):
            if A[j] > A[j+1]:
                # print(f"交換:{A[j]},{A[j+1]}")
                A[j], A[j+1] = A[j+1], A[j]
                count += 1
    output(A, count)

def output(A, N):
    for a in range(len(A)):
        if a == len(A)-1:
            print(A[a])
            print(N)
        else:
            print(A[a], end=" ")

def main():
    N = int(input())
    list = input().split(" ")
    list = [int(s) for s in list]
    
    bubbleSort(list, N)

if __name__ == "__main__":
    main()
