def cross1(arr,s):
    for i in range(3):
        if arr[i][i] not in s:
            return False
    return True
def cross2(arr,s):
    for i in range(3):
        if arr[i][2-i] not in s:
            return False
    return True
def calc(arr, s):
    for r in range(3):
        pos = True
        for c in range(3):
            if arr[r][c] not in s:
                pos = False
                break
        if pos:
            return True
    
    for c in range(3):
        pos = True
        for r in range(3):
            if arr[r][c] not in s:
                pos = False
                break
        if pos:
            return True
    if cross1(arr,s) or cross2(arr,s):
        return True
    return False
        


if __name__ == "__main__":
    arr = []
    for i in range(3):
        arr.append(list(map(int,input().split())))
    # print(arr)
    s = set()
    n = int(input())
    for _ in range(n):
        s.add(int(input()))

    print("Yes" if calc(arr, s) else "No")
    
