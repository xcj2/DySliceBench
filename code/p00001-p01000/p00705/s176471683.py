def get_input():
    data_list = input().split()
    for i in range(len(data_list)):
        data_list[i] = int(data_list[i])
    return data_list

def make_dict(day_dict, data_list):
    candidate_num =data_list[0] + 1
    for i in range(1, candidate_num):
        data = data_list[i]
        if data in day_dict:
            day_dict[data] += 1
        else:
            day_dict[data] = 1
    return day_dict

def decide_open_day(day_dict, quorum):
    max_num = max(day_dict.values())
    if max_num < quorum:
        return 0
    max_k_list = [kv[0] for kv in day_dict.items() if kv[1] == max_num]
    open_day = min(max_k_list)
    return open_day


if __name__ == "__main__":
    while True:
        member_num, quorum = get_input()
        if member_num == 0:
            break
        day_dict = dict()
        for i in range(member_num):
            data_list = get_input()
            day_dict = make_dict(day_dict, data_list)
        if day_dict == {}: # remove candidate_day is None
            print(0)
        else:
            open_day = decide_open_day(day_dict, quorum)
            print(open_day)


