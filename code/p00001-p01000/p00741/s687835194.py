import sys
sys.setrecursionlimit(10000)

def get_two_int():
    two_int = input().split()
    for i in range(2):
        two_int[i] = int(two_int[i])
    return two_int

def get_data_list():
    data_list = input().split()
    for i, v in enumerate(data_list):
        data_list[i] = int(v)
    # print("data_list", data_list) # debug
    return data_list


def make_map(width, height):
    map_list = [[0] * (width + 2) for x in range(height + 2)] # まわりを0で囲む
    # print("map_list", map_list) # debug pprint?
    for h in range(1, height + 1):
        line_list = get_data_list()
        for w in range(1, width + 1):
            map_list[h][w] = line_list[w-1] # 汚い
    #print("map_list", map_list) # debug
    return map_list

def count_island(width, height, map_list):
    count = 0
    checked_set = set()
    for h in range(1, height + 1):
        for w in range(1, width + 1):
            if map_list[h][w] == 1 and ((h, w) not in checked_set):
                map_list, checked_set = check_around(h, w, map_list, checked_set)
                count += 1
    # print("checked_set", checked_set) # debug
    return count

def check_around(h, w, map_list, checked_set):
    # print((h, w)) #debug
    checked_set.add((h, w))
    # print("map_list", map_list) # debug
    for i in range(h - 1, h + 2): # まわりを全てチェック、大枠のまわりを0で余分に囲っているので無問題
        for j in range(w - 1, w + 2):
            if map_list[i][j] == 1 and (i, j) not in checked_set:
                    map_list, checked_set = check_around(i, j, map_list, checked_set)
    return map_list, checked_set


if __name__ == "__main__":
    while True:
        width, height = get_two_int()
        if width == 0:
            break
        # print("width", width) # debug
        # print("height", height) # debug
        map_list = make_map(width, height)
        # print("map_list", map_list) # debug 
        count = count_island(width, height, map_list)
        print(count)

