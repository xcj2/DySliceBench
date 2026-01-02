def swap(arr,i,j):
    arr1 = arr[:]
    arr1[i],arr1[j] = arr1[j],arr1[i]

    return arr1

def increasing(arr):
    for i in range(len(arr)-1):
        if arr[i+1] <= arr[i]:
            return False

    return True

def main():
    n = int(input())
    arr = list(map(int,input().split()))
    if increasing(arr):
        print('YES')
        return

    for i in range(n):
        for j in range(n):
            arr1 = swap(arr,i,j)
            if increasing(arr1):
                print('YES')
                return

    print('NO')

main()
