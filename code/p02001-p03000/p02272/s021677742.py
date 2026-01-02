n = int(input())
s = list(map(int, input().split()))
count = 0

def main():
    mergeSort(s, 0, n)
    print(' '.join(map(str, s)))
    print(count)

def mergeSort(a, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        mergeSort(a, left, mid)
        mergeSort(a, mid, right)
        merge(a, left, mid, right)

def merge(a, left, mid, right):
    global count
    l = a[left:mid]
    r = a[mid:right]
    i = 0
    j = 0
    l.append(float('inf'))
    r.append(float('inf'))
    for k in range(left, right, 1):
        if l[i] < r[j]:
            a[k] = l[i]
            i += 1
        else :
            a[k] = r[j]
            j += 1
        count += 1


if __name__ == '__main__':
    main()

