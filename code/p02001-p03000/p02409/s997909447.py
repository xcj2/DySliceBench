def initialize_buiding(building):
    for i in range(3):
        building.append([0 for j in range(10)])

def change_room(floor, row, v, building):
    building[floor-1][row-1] += v

def print_university_building(building):
    for floor in building:
        print(' ', end='')
        print(' '.join(map(str,floor)))

def print_hash():
    for i in range(1, 20):
        print('#',end="")
    print("#")

uni_building1 = []
uni_building2 = []
uni_building3 = []
uni_building4 = []

initialize_buiding(uni_building1)
initialize_buiding(uni_building2)
initialize_buiding(uni_building3)
initialize_buiding(uni_building4)

n = int(input())

for i in range(n):
    b,f,r,v = (int(x) for x in input().split())
    if b == 1:
        change_room(f,r,v,uni_building1)
    elif b == 2:
        change_room(f,r,v,uni_building2)
    elif b == 3:
        change_room(f,r,v,uni_building3)
    elif b == 4:
        change_room(f,r,v,uni_building4)
    else:
        None

print_university_building(uni_building1)
print_hash()
print_university_building(uni_building2)
print_hash()
print_university_building(uni_building3)
print_hash()
print_university_building(uni_building4)
