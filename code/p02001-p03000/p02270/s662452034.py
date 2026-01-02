def sum_of_list(A):
    sum = 0
    for i in A:
        sum += int(i)
    return sum

def load_number(A, p, k):
    capacity = p
    num = 0
    for i in A:
        if capacity < int(i):
            break
        elif p >= int(i) and k > 0:
            num += 1
            p -= int(i)
        elif p < int(i) and k > 1:
            num += 1
            k -= 1
            p = capacity
            p -= int(i)
        elif k == 0:
            break
    return num

def search_load_capacity(A, n, k):
    total_weight = sum_of_list(A)
    left = 0
    right = total_weight + 1
    while left < right:
        mid = int((left + right) / 2)
        if load_number(A, mid, k) >= n:
            if load_number(A, mid-1, k) < n:
                return mid
            else:
                right = mid
        else:
            left = mid + 1

n, k = (map(int,input().split()))
A = [input() for x in range(n)]
print(search_load_capacity(A, n, k))
