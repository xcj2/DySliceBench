import math


def find_argmax(num_list):
    argmax = sorted(enumerate(num_list), key=lambda x:x[1])[-1][0]
    return argmax


def find_all_more_than(threshold, num_list):
    indices = [
        idx
        for idx, num in enumerate(num_list) 
        if num > threshold
    ]
    return indices


def read_input():
    initial_inputs = input().split(" ")
    N = int(initial_inputs[0])
    H = int(initial_inputs[1])
    a_list = []
    b_list = []
    for _ in range(N):
        inputs = input().split(" ")
        a = int(inputs[0])
        b = int(inputs[1])
        a_list.append(a)
        b_list.append(b)
    return N, H, a_list, b_list


# TLE
def searchA(N, H, a_list, b_list):
    # initialize used_indices
    used_indices = [ False for b in b_list]

    # initialize search_area
    search_area = [ b for b in b_list ]

    # count how many times
    times_count = 0
    
    while H > 0:
        # search
        idx = find_argmax(search_area)

        # check
        if used_indices[idx]:
            # calculate rest and finish
            rest_count = math.ceil(H / search_area[idx])
            return times_count + rest_count

        # attack
        H -= search_area[idx]

        # change
        search_area[idx] = a_list[idx]
        used_indices[idx] = True
        
        # count
        times_count += 1

    return times_count

# still TLE
def searchB(N, H, a_list, b_list):
    # initialize used_indices
    used_indices = [ False ] * N

    # initialize search_area
    search_area = [ b for b in b_list ]

    # count how many times
    times_count = 0

    # pick up b indices higher than max(a_list)
    higher_b_indices = find_all_more_than(max(a_list), b_list)
    higher_b_list = [ b_list[idx] for idx in higher_b_indices ]

    for b in reversed(sorted(higher_b_list)):
        if not H > 0:
            return times_count

        # attack
        H -= b
        times_count += 1

    # fix search_area used_indices
    for idx in higher_b_indices:
        # change
        search_area[idx] = a_list[idx]
        used_indices[idx] = True

    while H > 0:
        # search
        idx = find_argmax(search_area)

        # check
        if used_indices[idx]:
            # calculate rest and finish
            rest_count = math.ceil(H / search_area[idx])
            return times_count + rest_count

        # attack
        H -= search_area[idx]
        times_count += 1

        # change
        search_area[idx] = a_list[idx]
        used_indices[idx] = True
        
    return times_count


# still TLE
def searchC(N, H, a_list, b_list):
    # count how many times
    times_count = 0

    # pick up b indices higher than max(a_list)
    max_a = max(a_list)
    higher_b_indices = find_all_more_than(max_a, b_list)
    higher_b_list = [ b_list[idx] for idx in higher_b_indices ]

    for b in reversed(sorted(higher_b_list)):
        if not H > 0:
            return times_count

        # attack
        H -= b
        times_count += 1

    # use max(a_list)
    rest_count = math.ceil(H / max_a)
    return times_count + rest_count


def main():
    # read input
    N, H, a_list, b_list = read_input()

    # search
    times_count = searchC(N, H, a_list, b_list)

    # output
    print(times_count)
    

if __name__ == '__main__':
    main()
