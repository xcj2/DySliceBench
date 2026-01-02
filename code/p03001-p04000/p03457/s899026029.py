import math
import sys

sys.setrecursionlimit(100000)

def solve():
    n = int(input())
    success_trip = True
    now_t, now_x, now_y = 0, 0, 0
    for i in range(n):
        next_t, next_x, next_y = map(int, input().split(' '))
        if success_trip:
            if not find_path(now_t, now_x, now_y, next_t, next_x, next_y):
                success_trip = False
            now_t, now_x, now_y = next_t, next_x, next_y
    
    if success_trip:
        print("Yes")
    else:
        print("No")

def find_path(now_t, now_x, now_y, next_t, next_x, next_y):
    time = next_t - now_t
    return recursion_find(time, now_x, now_y, next_x, next_y)
    
def recursion_find(time, now_x, now_y, target_x, target_y):
    # print("-----------")
    # print("time:", time)
    # print("now_x:", now_x)
    # print("now_y:", now_y)
    # print("target_x:", target_x)
    # print("target_y:", target_y)
    # print("-----------")

    if (abs(target_x - now_x) + abs(target_y - now_y) - time) % 2 == 1:
        # cant
        return False

    if time == 0:
        if now_x == target_x or now_y == target_y:
            return True
        else:
            return False
    else:
        # distant
        if time < abs(target_x - now_x) + abs(target_y - now_y):
            # cant
            return False
            
        if recursion_find(time-1, now_x-1, now_y, target_x, target_y):
            return True
        elif recursion_find(time-1, now_x, now_y-1, target_x, target_y):
            return True
        elif recursion_find(time-1, now_x+1, now_y, target_x, target_y):
            return True
        elif recursion_find(time-1, now_x, now_y+1, target_x, target_y):
            return True
        else: 
            return False

if __name__ == "__main__":
    solve()