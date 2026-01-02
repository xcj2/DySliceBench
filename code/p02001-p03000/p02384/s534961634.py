def move(lon, lat, com):
    target, other, pop_index, insert_index = lon, lat, 0, 3
    if com == "E" or com == "W":
        target, other = lat, lon
    if com == "S" or com == "W":
        pop_index, insert_index = 3, 0
    target.insert(insert_index, target.pop(pop_index))
    other[0], other[2] = target[0], target[2]


def set_upper(lon, lat, upper):
    com = "N" if upper in lon else "E"
    for _i in range(4):
        move(lon, lat, com)
        if lon[0] == upper:
            break


def rotate(lon, lat, com):
    if com == "R":
        lon[1], lat[1], lon[3], lat[3] = lat[3], lon[1], lat[1], lon[3]
    elif com == "L":
        lon[1], lat[1], lon[3], lat[3] = lat[1], lon[3], lat[3], lon[1]


longitude = [1, 2, 6, 5]
latitude = [1, 4, 6, 3]
values = list(input().split())
n = int(input())
for i in range(n):
    U, F = input().split()
    set_upper(longitude, latitude, values.index(U) + 1)
    for j in range(3):
        if longitude[1] == values.index(F) + 1:
            break
        rotate(longitude, latitude, "R")
    print(values[latitude[3] - 1])

