#アルゴリズム関数-サイコロを回転させる
def dice_rotation(list1, str1):
    if str1 == "S":
        list1[0],list1[1],list1[4],list1[5] = list1[4],list1[0],list1[5],list1[1]
    elif str1 == "E":
        list1[0],list1[2],list1[3],list1[5] = list1[3],list1[0],list1[5],list1[2]
    elif str1 == "N":
        list1[0],list1[1],list1[4],list1[5] = list1[1],list1[5],list1[0],list1[4]
    elif str1 == "W":
        list1[0],list1[2],list1[3],list1[5] = list1[2],list1[5],list1[0],list1[3]
    return list1

#アルゴリズム関数-上面・前面の番号を指定番号へサイコロを回転させる
def dice_find(list1, int1, int2):
    try:
        position_numnber = list1.index(int2)
    except:
        position_numnber = -1
    if position_numnber == 0:
        list1 = dice_rotation(list1, "S")
    elif position_numnber == 2:
        list1 = dice_rotation(list1, "W")
        list1 = dice_rotation(list1, "S")
    elif position_numnber == 3:
        list1 = dice_rotation(list1, "E")
        list1 = dice_rotation(list1, "S")
    elif position_numnber == 4:
        list1 = dice_rotation(list1, "S")
        list1 = dice_rotation(list1, "S")
    elif position_numnber == 5:
        list1 = dice_rotation(list1, "N")
    try:
        position_numnber = list1.index(int1)
    except:
        position_numnber = -1
    if position_numnber == 2:
        list1 = dice_rotation(list1, "W")
    elif position_numnber == 3:
        list1 = dice_rotation(list1, "E")
    elif position_numnber == 5:
        list1 = dice_rotation(list1, "W")
        list1 = dice_rotation(list1, "W")
    return list1

#アルゴリズム関数-サイコロの内容が
def list_overlapping_check(list1):
    result = True
    for i in range(1, len(list1)):
        list1[i] = dice_find(list1[i], list1[0][0], list1[0][1])
        if list1[0] == list1[i]:
            result = False
            break
    if result == True and len(list1) > 2:
        result = list_overlapping_check(list1[1:])
    return result

#インプットdataの格納
input_count = int(input())
check_data = list()
for i in range(input_count):
    check_data.append(list(map(int, input().split())))

#結果表示
if list_overlapping_check(check_data) == True:
    print("Yes")
else:
    print("No")

