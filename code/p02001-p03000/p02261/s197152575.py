def bubble_sort(num_list):
    list_b = num_list[:]
    for i in range(len(list_b)-1):
        for j in range(len(list_b)-1,i,-1):
            if list_b[j][1] < list_b[j-1][1]:
                list_b[j],list_b[j-1] = list_b[j-1],list_b[j]
    return list_b

def selection_sort(num_list):
    list_s = num_list[:]
    for i in range(len(list_s)):
        minj = i
        for j in range(i,len(list_s)):
            if list_s[minj][1] > list_s[j][1]:
                minj = j
        list_s[i],list_s[minj] = list_s[minj],list_s[i]
    return list_s

def isStable(list_x, list_y):
    leng = int(len(list_x))
    for i in range(leng-1):
        for j in range(i+1, leng):
            for x in range(leng-1):
                for y in range(x+1, leng):
                    if list_x[i][1]==list_x[j][1] and list_x[i]==list_y[y] and list_x[j] == list_y[x]:
                        return "Not stable"
    return "Stable"


qnt = int(input())
num_list = input().split()

bs = bubble_sort(num_list)
ss = selection_sort(num_list)
print(" ".join(bs))
print(isStable(num_list,bs))
print(" ".join(ss))
print(isStable(num_list,ss))