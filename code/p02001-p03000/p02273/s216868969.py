import math
cos60 = math.cos(math.pi*60/180)
sin60 = math.sin(math.pi*60/180)
#add_triangle
# input: start(x, y) end(x, y)
def add_triangle(start, end):
    x1 = (2*start[0] + end[0]) / 3
    x3 = (start[0] + 2*end[0]) / 3
    y1 = (2*start[1] + end[1]) / 3
    y3 = (start[1] + 2*end[1]) / 3
    x2 = x1 + (x3-x1)*cos60 - (y3-y1)*sin60
    y2 = y1 + (x3-x1)*sin60 + (y3-y1)*cos60
    return [(x1,y1), (x2,y2), (x3,y3)]

#koch_recursion
#input list [(x1,y1),(x2,y2),(x3,y3)...]
def koch_recursion(list1):
    output = []
    for i in range(len(list1)-1):
        output.append(list1[i])
        output += add_triangle(list1[i], list1[i+1])
    output.append(list1[len(list1)-1])
    return output

#Koch  call koch_recursion(0, 100)
def Koch(start, end, n):
    output = [start, end]
    for i in range(n):
        output = koch_recursion(output)
    for x, y in output:
        print("{:.8f} {:.8f}".format(x, y))

n = int(input())
Koch((0,0), (100,0), n)
