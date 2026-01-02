
AIR_PORTS = ['A', 'B', 'C']


def get_input():
    PandQandR = input().split(" ")
    P = int(PandQandR[0])
    Q = int(PandQandR[1])
    R = int(PandQandR[2])
    return P, Q, R


def calc_flight_time(flight_time_list):
    min = 500
    for i, time_1 in enumerate(flight_time_list):
        for j, time_2 in enumerate(flight_time_list):
            if i == j:
                continue
            result_time = time_1 + time_2
            if min > result_time:
                min = result_time
    return min


def main():
    P, Q, R = get_input()
    flight_time_list = [P, Q, R]
    result_time = calc_flight_time(flight_time_list)
    print(result_time)


if __name__ == '__main__':
    main()
