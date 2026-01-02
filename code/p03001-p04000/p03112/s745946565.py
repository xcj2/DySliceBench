import bisect

inf = 10 ** 18

def get_near(tera_num, tera_data, start_point):
    index_right = bisect.bisect_right(tera_data, start_point)
    tera_pre, tera_after = tera_data[index_right], tera_data[index_right - 1]
    return tera_pre, tera_after

def calc_data(start_point, point_a, point_b, min_point):
    a = abs(start_point - point_a) + abs(point_a - point_b)
    b = abs(start_point - point_b) + abs(point_b - point_a)
    min_point = min(a, b, min_point)
    return min_point

def calc_ans(start_point, tera_pre, tera_after, jinja_pre, jinja_after):
    min_point = float('inf')
    min_point = calc_data(start_point, tera_pre, jinja_pre, min_point)
    min_point = calc_data(start_point, tera_pre, jinja_after, min_point)
    min_point = calc_data(start_point, tera_after, jinja_pre, min_point)
    min_point = calc_data(start_point, tera_after, jinja_after, min_point)
    return min_point


def start(tera_num, jinja_num, q_num, tera_data, jinja_data, q_data):
    for start_point in q_data:
        tera_pre, tera_after = get_near(tera_num, tera_data, start_point)
        jinja_pre, jinja_after = get_near(jinja_num, jinja_data, start_point)
        ans = calc_ans(start_point, tera_pre, tera_after, jinja_pre, jinja_after)
        print(ans)

def main():
    tera_num, jinja_num, q_num = list(map(int, input().split()))
    tera_data = [-inf] + [int(input()) for i in range(tera_num)] + [inf]
    jinja_data = [-inf] + [int(input()) for i in range(jinja_num)] + [inf]
    q_data = [int(input()) for i in range(q_num)]

    start(tera_num, jinja_num, q_num, tera_data, jinja_data, q_data)

if __name__ == '__main__':
    main()