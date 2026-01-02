import copy


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


longitude = [0, 1, 5, 4]
latitude = [0, 3, 5, 2]

values = list(input().split())
u, f = values[longitude[0] - 1], values[longitude[1] - 1]
values2 = list(input().split())
longitude2, latitude2 = copy.copy(longitude), copy.copy(latitude)
result = "No"
for i in range(6):
    set_upper(longitude2, latitude2, i)
    for j in range(4):
        rotate(longitude2, latitude2, "R")
        if values[0] != values2[longitude2[0]]:
            continue
        elif values[1] != values2[longitude2[1]]:
            continue
        elif values[2] != values2[latitude2[3]]:
            continue
        elif values[3] != values2[latitude2[1]]:
            continue
        elif values[4] != values2[longitude2[3]]:
            continue
        elif values[5] != values2[longitude2[2]]:
            continue
        else:
            result = "Yes"
            break
    if result == "Yes":
        break
print(result)

