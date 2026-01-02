def get_input_data():
    input_data = int(input())
    return input_data

def make_calendar():
    calendar_dict = dict()
    duration = 0
    y, m, d = 1000, 1, 1
    while y > 1 or m > 1 or d > 1:
        duration += 1
        if d > 1:
            d -= 1
        elif m > 1:
            m -= 1
            d = calculate_month_having_date(y, m)
        else:
            y -= 1
            m = 10
            d = calculate_month_having_date(y, m)
        calendar_dict[(y, m, d)] = duration
    return calendar_dict

def calculate_month_having_date(y, m):
    if y % 3 == 0 or m % 2 == 1:
        d = 20
    else:
        d = 19
    return d

def show_the_duration(calendar_dict):
    birthday = input().split()
    for i, v in enumerate(birthday):
        birthday[i] = int(v)
    duration = calendar_dict[tuple(birthday)]
    return duration

if __name__ == "__main__":
    calendar_dict = make_calendar()
    # print("calendar_dict", calendar_dict) # debug
    people_num = get_input_data()
    for i in range(people_num):
        duration = show_the_duration(calendar_dict)
        print(duration)

