def comp(i,j):
    # i < j <-> 1
    # i > j <-> -1
    # i == j <-> 0
    if len(i) < len(j):
        return 1
    elif len(i) > len(j):
        return -1
    for x in range(len(i)):
        if i[x] == j[x]:
            continue
        elif i[x] > j[x]:
            return -1
        else:
            return 1
    return 0



def bisect_left(array, i):
    __bisect_array = array
    def _bisect_left(i, left, right):
        n = right - left + 1
        mid = (left+right) // 2
        if n == 1:
            if comp(__bisect_array[mid],i) == 1:
                return 1
            else:
                return 0
        if comp(i, __bisect_array[mid]) >= 0:
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
            if comp(i, __bisect_array[mid]) == 1:
                return 0
            else:
                return 1
        if comp(__bisect_array[mid] ,i) >= 0:
            return  (mid-left+1) + _bisect_right(i,mid+1,right)
        else:
           return _bisect_right(i,left,mid)
    return _bisect_right(i, 0, len(array)-1)

N = int(input())
L = []
for _ in range(3):
    l = list(map(int,input().split()))
    l = list(map(str,sorted(l)))
    L.append(l)
ans = 0
for x in L[1]:
    n = bisect_left(L[0],x)
    m = bisect_right(L[2],x)
    m = N - m
    ans += n*m
print(ans)