def InputData():
    
    # [weight_len, track_num] = map(int, input().split())
    # weight_data_str = [input() for i in range(weight_len)]
    # weight_data = list(map(int, weight_data_str))

    weight_len, track_num = [int(s) for s in input().split(" ")]
    weight_data = [int(input()) for _ in range(weight_len)]

    return weight_len, track_num, weight_data

def check(track_num, weight_len, weight_data, key):
    i = 0
    for j in range(track_num):
        s = 0
        while (s + weight_data[i]) <= key:
            s += weight_data[i]
            i += 1
            if i == weight_len:
                return weight_len

    return i

def binarySearch(right, weight_len, track_num, weight_data):

    left = 0

    while((right - left) > 1):
        mid = (left + right) // 2
        v = check(track_num, weight_len, weight_data, mid)
        if v >= weight_len:
            right = mid
        else:
            left = mid

    return right

def PrintOut(right):
    print(right)

def main():
    
    [weight_len, track_num, weight_data] = InputData()
    right = 100000 * 10000
    right = binarySearch(right, weight_len, track_num, weight_data)
    PrintOut(right)

if __name__ == '__main__':
    main()
    
