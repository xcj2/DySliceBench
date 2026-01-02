import copy


def move(lon, lat, news):
    target, other, pop_index, insert_index = lon, lat, 0, 3
    if news == "E" or news == "W":
        target, other = lat, lon
    if news == "S" or news == "W":
        pop_index, insert_index = 3, 0
    target.insert(insert_index, target.pop(pop_index))
    other[0], other[2] = target[0], target[2]


def set_upper(lon, lat, upper):
    news = "N" if upper in lon else "E"
    while lon[0] != upper:
        move(lon, lat, news)


def rotate(lon, lat, com):
    if com == "R":
        lon[1], lat[1], lon[3], lat[3] = lat[3], lon[1], lat[1], lon[3]
    elif com == "L":
        lon[1], lat[1], lon[3], lat[3] = lat[1], lon[3], lat[3], lon[1]


def compare(val1, val2):
    lon2, lat2 = copy.copy(longitude), copy.copy(latitude)
    for u in range(6):
        set_upper(lon2, lat2, u)
        for f in range(4):
            rotate(lon2, lat2, "R")
            if False not in map(lambda x1, x2: val1[x1] == val2[x2], longitude + latitude, lon2 + lat2):
                return True
    return False


longitude = [0, 1, 5, 4]
latitude = [0, 3, 5, 2]
# values = input().split()
# newses = input()
# for c in newses:
#     move(longitude, latitude, c)
# print(values[longitude[0]])

# values = input().split()
# n = int(input())
# for i in range(n):
#     x, y = map(lambda z: values.index(z), input().split())
#     lon_work, lat_work = copy.copy(longitude), copy.copy(latitude)
#     set_upper(lon_work, lat_work, x)
#     while y != lon_work[1]:
#         rotate(lon_work, lat_work, "R")
#     print(values[lat_work[3]])

# values1 = input().split()
# values2 = input().split()
# print("Yes" if compare(values1, values2) else "No")

values = []
n = int(input())
for i in range(n):
    values.append(input().split())
value1, *tail = values
while tail:
    for value2 in tail:
        if compare(value1, value2):
            print("No")
            exit()
    head, *tail = tail
print("Yes")

