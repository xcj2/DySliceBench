a1x = [int(x) for x in input().split(' ')]
a2x = [int(x) for x in input().split(' ')]
a3x = [int(x) for x in input().split(' ')]

sheet = [a1x, a2x, a3x]

n = int(input())
numbers = []

for i in range(n):
    num = int(input())
    numbers.append(num)

def solve(n, sheet, numbers):
    for number in numbers:
        for row in range(3):
            for column in range(3):
                if sheet[row][column] == number:
                    sheet[row][column] = "X"

    if checkRow(sheet) or checkColumn(sheet) or checkDiagonals(sheet):
        print("Yes")
    else:
        print("No")

def checkRow(sheet):
    for row in range(3):
        marked = 0
        for column in range(3):
            if sheet[row][column] == "X":
                marked += 1
        if marked == 3:
            return True
    
    return False
            
def checkColumn(sheet):
    for row in range(3):
        marked = 0
        for column in range(3):
            if sheet[column][row] == "X":
                marked += 1
        if marked == 3:
            return True
    
    return False

def checkDiagonals(sheet):
    marked = 0
    for i in range(3):
        if sheet[i][i] == "X":
            marked += 1

    if marked != 3:
        marked = 0
        for j in range(3):
            if sheet[j][2-j] == "X":
                marked += 1
    
    if marked == 3:
        return True
    else:
        return False

    

solve(n, sheet, numbers)