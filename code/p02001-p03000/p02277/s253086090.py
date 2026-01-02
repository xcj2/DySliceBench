def partition(hoge, p, r):
    x = int(hoge[r][1])
    i = p-1
    for j in range(p, r):
        if int(hoge[j][1]) <= x:
            i += 1
            tmp = hoge[i]
            hoge[i] = hoge[j]
            hoge[j] = tmp
    tmp = hoge[i+1]
    hoge[i+1] = hoge[r]
    hoge[r] = tmp
    return i+1
    
def qSort(hoge, p, r):
    if p < r:
        q = partition(hoge, p, r)
        qSort(hoge, p, q-1)
        qSort(hoge, q+1, r)
    
def isStable(input_array, output_array):
    same_nums = list()
    now_num = 0
    for elem in output_array:
        if now_num != int(elem[1]):
            now_num = int(elem[1])
            same_nums = list()
        else:
            for c in same_nums:
                if input_array.index(c) > input_array.index(elem):
                    return 'Not stable'
        same_nums.append(elem)
    return 'Stable'
    
if __name__ == '__main__':
    num = int(input())
    hoge = list()
    for _ in range(num):
        c, s = input().split()
        hoge.append((c,s))
    origin = hoge[:]
    qSort(hoge, 0, len(hoge)-1)
    print(isStable(origin, hoge))
    print('\n'.join(['{0[0]} {0[1]}'.format(x) for x in hoge]))
