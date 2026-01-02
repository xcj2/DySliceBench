def bisect_left(array, i):
    __bisect_array = array
    def _bisect_left(i, left, right):
        n = right - left + 1
        mid = (left+right) // 2
        if n == 1:
            if __bisect_array[mid] < i:
                return 1
            else:
                return 0
        if i <= __bisect_array[mid]:
            return _bisect_left(i,left,mid)
        else:
            return (mid-left+1) + _bisect_left(i,mid+1,right)
    return _bisect_left(i, 0, len(array)-1)

def bisect_right(array, i):
    __bisect_array = array
    def _bisect_right(i, left, right):
        n = right - left + 1
        mid = (right+left) // 2
        if n == 1:
            if i < __bisect_array[mid] :
                return 0
            else:
                return 1
        if __bisect_array[mid] <= i:
            return  (mid-left+1) + _bisect_right(i,mid+1,right)
        else:
           return _bisect_right(i,left,mid)
    return _bisect_right(i, 0, len(array)-1)

N = int(input())
L = []
for _ in range(3):
    l = list(map(int,input().split()))
    L.append(sorted(l))
ans = 0
for x in L[1]:
    n = bisect_left(L[0],x)
    m = bisect_right(L[2],x)
    m = N - m
    ans += n*m
print(ans)