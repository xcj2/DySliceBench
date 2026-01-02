first_line = input().split()
second_line = input().split()
third_line = input().split()
 
first_line = [int(i) for i in first_line]
second_line = [int(i) for i in second_line]
third_line = [int(i) for i in third_line]

N = input()
N = int(N)



B  = [] 
for i in range(N):
    inp  =input()
    inp = int(inp)
    B.append(inp)


# arr = [[0]*3]*3
# print(arr)
# for i in range(3):
#     arr[0][i]= first_line[i]
#     print(arr)
# print(arr)
# for i in range(3):
#     arr[1][i]= second_line[i]
# for i in range(3):
#     arr[2][i]= third_line[i]

arr = []
arr.append(first_line)
arr.append(second_line)
arr.append(third_line)
carr = [[False for i in range(3)] for j in range(3)]

for b in B:
    for i in range(3):
        for j  in range(3):
            if b == arr[i][j]:
                carr[i][j] = True

def yoko(carr):
    for i in range(3):
        flag = 0
        for j in range(3):
            if carr[i][j] != True:
                flag = 1
        if flag == 0 :
            return True    
    return False


def tate(carr):
    for i in range(3):
        flag = 0
        for j in range(3):
            if carr[j][i] != True:
                flag = 1
                break
        if flag == 0:

            return  True
    
    return False

def naname (carr):
    flag2 = 0
    flag1 = 0
    for i in range(3):
        if carr[i][i] != True:
            flag1 = 1

        if carr[i][3-i-1] != True:
            flag2 = 1;
    if flag1==0 or flag2 ==0:
        return True
    else:
        return False

def checker(carr):
    # print(tate(carr))
    # print(yoko(carr))
    # print(naname(carr))
    
    if not tate(carr)  and not yoko(carr) and not naname(carr):
        return 'No'
    else:
        return 'Yes' 
print(checker(carr))