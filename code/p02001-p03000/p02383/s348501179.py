def north(list):
    List = []
    List.append(list[1])
    List.append(list[5])
    List.append(list[2])
    List.append(list[3])
    List.append(list[0])
    List.append(list[4])
    return List

def west(list):
    List = []
    List.append(list[2])
    List.append(list[1])
    List.append(list[5])
    List.append(list[0])
    List.append(list[4])
    List.append(list[3])
    return List
    
def south(list):
    List = []
    List.append(list[4])
    List.append(list[0])
    List.append(list[2])
    List.append(list[3])
    List.append(list[5])
    List.append(list[1])
    return List

def east(list):
    List = []
    List.append(list[3])
    List.append(list[1])
    List.append(list[0])
    List.append(list[5])
    List.append(list[4])
    List.append(list[2])
    return List

dice = list(map(int, input().split()))
x = str(input())
y = list(x)
for i in range(len(x)):
    if y[i] == 'N':
        dice[0:5] = north(dice)
    elif y[i] == 'W':
        dice[0:5] = west(dice)
    elif y[i] == 'S':
        dice[0:5] = south(dice)
    elif y[i] == 'E':
        dice[0:5] = east(dice)
print(dice[0])
