def input_int():
    return(int(input()))

def input_int_list():
    return(list(map(int,input().split())))

def input_int_map():
    return(map(int,input().split()))

def run():
    num_count = input_int()
    nums = []
    for _ in range(num_count):
        nums.append(input_int())

    num_count = 1

    current_num = 1
    while True:
        current_num = nums[current_num - 1]

        if num_count >= len(nums):
            print(-1)
            return

        if current_num == 2:
            print(num_count)
            return
        num_count += 1

run()
