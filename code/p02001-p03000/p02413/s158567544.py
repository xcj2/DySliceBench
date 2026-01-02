r, c = map(int, input().split())

def num_get(r):
    nums = []
    for i in range(r):
        num = list(map(int, input().split()))
        nums.append(num)
    return nums

def hori_sum(num, r):
    nums = []
    for i in range(r):
        sum_i = sum(num[i])
        num[i].append(sum_i)
        print(" ".join([str(j) for j in num[i]]))
        nums.append(num[i])
    #print(nums)
    return nums

def verti_sum(nums, r, c):
    sums = []
    sum_v = 0
    c = c + 1
    for i in range(c):
        #print(i)
        for j in range(r):
            #print("{} {} {}" .format(i, j, num[j][i]))
            sum_v = sum_v + nums[j][i]
        sums.append(sum_v)
        sum_v = 0
    print(" ".join([str(i) for i in sums]))
    return sums

nums = num_get(r)
hori = hori_sum(nums, r)
#print(hori)
verti_sum(hori, r, c)




