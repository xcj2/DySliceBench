import numpy as np

def input_numbers():
    temp = list(map(int, input().split()))
    return temp

def GCD(a, b):
    if(a < b):
        temp = a
        a = b
        b = temp
    a = a % b
    if(a == 0):
        return b
    else:
        return GCD(a, b)

class point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

n = int(input())

R_point = []
B_point = []

for i in range(n):
    temp = input_numbers()
    R_point += [point(temp[0], temp[1])]

for i in range(n):
    temp = input_numbers()
    B_point += [point(temp[0], temp[1])]

B_point.sort(key = lambda point:point.x)
R_point.sort(key = lambda point:point.y)
R_point.reverse()

count = 0

for i in range(len(B_point)):
    for j in range(len(R_point)):
        if(R_point[j].x < B_point[i].x and R_point[j].y < B_point[i].y):
            R_point.pop(j)
            count += 1
            break
print(count)