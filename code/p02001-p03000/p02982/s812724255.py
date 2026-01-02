from math import sqrt
N, D = map(int, input().split(' '))
 
coordinate_list = list()
 
# 一行ずつ分解してリストに入れる
for i in range(N):
    coordinate = list(input().split())
    coordinate = list(map(int, coordinate))
    coordinate_list.append(coordinate)
 
def make_dis_list(D, coordinate_list):
    distance_list = list()
    for i, coordinate in enumerate(coordinate_list):
        for j in range(i+1, N):
            distance_list.append(measure_distance(coordinate, coordinate_list[j], D))
    return distance_list
 
def measure_distance(a, b, D):
    square_dist = 0
    for i in range(D):
        square_dist += (a[i] - b[i])**2
    return sqrt(square_dist)
 
def int_counter(nums):
    counter = 0
    for num in nums:
        if int(num) == num: counter += 1
    return counter
 
distance_list = make_dis_list(D, coordinate_list)
print(int_counter(distance_list))