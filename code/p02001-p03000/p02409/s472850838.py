def construct_floor(num_rooms):
    return [0] * num_rooms


def construct_building(num_floors, num_rooms):
    building = []

    for i in range(num_floors):
        building.append(construct_floor(num_rooms))

    return building


def construct_buildings(num_buildings, num_floors, num_rooms):
    buildings = []

    for i in range(num_buildings):
        buildings.append(construct_building(num_floors, num_rooms))

    return buildings


def floor_to_string(floor):
    room_strings = list(map(str, floor))

    return ' ' + ' '.join(room_strings)


def building_to_string(building):
    floor_strings = list(map(floor_to_string, building))

    return '\n'.join(floor_strings)


def show_buildings(buildings):
    building_strings = list(map(building_to_string, buildings))

    separator = ''.join(['#'] * 20)

    separator = '\n' + separator + '\n'

    buildings_string = separator.join(building_strings)

    print(buildings_string)


if __name__ == "__main__":
    num_inputs = int(input())

    inputs = []

    for i in range(num_inputs):
        inputs.append(input())

    tenant_leaver_notices = list(
        map(lambda input_value: list(map(int, input_value.split())), inputs)
    )

    official_house = construct_buildings(4, 3, 10)

    for tenant_leaver_notice in tenant_leaver_notices:
        building = tenant_leaver_notice[0] - 1
        floor = tenant_leaver_notice[1] - 1
        room = tenant_leaver_notice[2] - 1
        num_people = tenant_leaver_notice[3]

        official_house[building][floor][room] += num_people

    show_buildings(official_house)

