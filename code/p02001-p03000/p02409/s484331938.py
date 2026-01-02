HOUSE_CNT = 4
FLOOR_CNT = 3
ROOM_CNT = 10

def init(houses):
    for h in range(0, HOUSE_CNT):
        floors = []
        for f in range(0, FLOOR_CNT):
            rooms = []
            for r in range(0, ROOM_CNT):
                rooms.append(0)
            floors.append(rooms)
        houses.append(floors)


def in_out(houses):
    n = int(input())
    for i in range(0, n):
        b, f, r, v = tuple(map(int, input().split(' ')))
        houses[b-1][f-1][r-1] += v;


def output(houses):
    line = False
    for house in houses:
        if line:
            print('####################')
        else:
            line = True
        for floor in house:
            for room in floor:
                print(' %d' % room, end='')
            print()


houses = []
init(houses)
in_out(houses)
output(houses)

