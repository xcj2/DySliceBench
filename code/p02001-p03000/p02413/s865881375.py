def row_sum(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum

def column_sum(list, stop):
    sum = []
    for i in range(stop):
        temp_sum = 0
        for j in range(len(list)):
            temp_sum += list[j][i]
        sum.append(temp_sum)
    return(sum)

def answer(list, stop):
    list.append(column_sum(list, stop))
    for i in list:
        i.append(row_sum(i))
    return list

def print_list_list(list):
    for i in list:
        print(i[0],end="")
        for j in range(1, len(i)):
            print(" ", end="")
            print(i[j],end="")
        print()

r, c = map(int,input().split())
a = []
for i in range(r):
    a.append(list(map(int,input().split())))

ans = answer(a, c)
print_list_list(ans)
