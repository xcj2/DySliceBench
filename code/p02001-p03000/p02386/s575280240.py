n = int(input())
d = [input().split() for i in range(n)]
# print(d)
# dice1 = input().split()
# dice2 = input().split()
# dice3 = input().split()

def rotate(faces, move):
    for i in range(len(move)):
        m = move[i]
        
        if m == "N":
            # N
            tmp = faces[4]
            faces[4] = faces[0]
            faces[0] = faces[1]
            faces[1] = faces[5]
            faces[5] = tmp
            
        elif m == "S":
            # S
            tmp = faces[1]
            faces[1] = faces[0]
            faces[0] = faces[4]
            faces[4] = faces[5]
            faces[5] = tmp
            
        elif m == "E":
            # E
            tmp = faces[2]
            faces[2] = faces[0]
            faces[0] = faces[3]
            faces[3] = faces[5]
            faces[5] = tmp
            
        elif m == "W":
            # W
            tmp = faces[3]
            faces[3] = faces[0]
            faces[0] = faces[2]
            faces[2] = faces[5]
            faces[5] = tmp

# for k, v in enumerate(dice1):
#     print(k, v)
#     if v in dice2:
#         index1 = dice2.index(v)
#         print(index1)

# if dice1[2] in dice2:
#     index1 = dice2.index(dice1[2])
#     if index1 == 0:
#         rotate(dice1, "W")
#     elif index1 == 1:
#         rotate(dice1, "WS")
#     elif index1 == 2:
#         pass
#     elif index1 == 3:
#         rotate(dice1, "WW")
#     elif index1 == 4:
#         rotate(dice1, "WN")
#     elif index1 == 5:
#         rotate(dice1, "E")
        
def equals(a, b):
    for (a1, b1) in zip(a, b):
        if a1 != b1:
            return False
            
    return True


def check(a, b):
    # print(a, b)
    isMatch = equals(a, b)
    
    
    looping = True
    for j in range(4):
        #print(dice1)
        if isMatch:
            break
        for i in range(4):
            # print(a)
            rotate(a, "N")
            if equals(a, b):
                isMatch = True
                break
        #print('----')
        #print(dice1)
        rotate(a, "W")
        #print(dice1)
    
    # print('---- ---- ----')
    #print(copy_list)
    # print('---- ---- ----')
    
    rotate(a, "NW")
    
    for j in range(4):
        #print(dice1)
        if isMatch:
            break
        for i in range(4):
            #print(dice1)
            rotate(a, "N")
            if equals(a, b):
                isMatch = True
                break
        #print('----')
        #print(dice1)
        rotate(a, "W")
        #print(dice1)
    
    return isMatch
    

result = True
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        
        if (check(d[i], d[j])):
            result = False

if result:
    print('Yes')
else:
    print('No')

