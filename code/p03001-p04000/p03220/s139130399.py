import bisect


def palace():
    def average_temperature(height):
        return t - (height * 0.006)
    
    def get_key_from_value(dict, value):
        for k, v in dict.items():
            if v == value:
                return k
    
    n = int(input())
    t, a = map(float, input().split())
    
    h = list(map(int, input().split()))
    h_dict = {}
    for i in range(n):
        h_dict[i + 1] = average_temperature(h[i])
    
    h_sorted = sorted(h, reverse=True)
    temperatures = [average_temperature(height) for height in h_sorted]
    
    index = bisect.bisect_left(temperatures, a)
    if index - 1 >= 0 and index <= n - 1:
        choices = [temperatures[index - 1], temperatures[index]]
        abses = [abs(a - choices[0]), abs(a - choices[1])]
        if abses[0] >= abses[1]:
            print(get_key_from_value(h_dict, choices[1]))
        else:
            print(get_key_from_value(h_dict, choices[0]))
    else:
        if index - 1 >= 0:
            choice = temperatures[index - 1]
            print(get_key_from_value(h_dict, choice))
        if index <= n - 1:
            choice = temperatures[index + 1]
            print(get_key_from_value(h_dict, choice))


if __name__ == '__main__':
    palace()
