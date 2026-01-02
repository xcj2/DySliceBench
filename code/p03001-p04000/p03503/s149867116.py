from logging import getLogger, basicConfig, DEBUG
basicConfig(level=DEBUG)
LOG = getLogger(__name__)

N = int(input())

def get_count_logical_and(base_int, list):
    result = []
    for item in list:
        logical_and = format(base_int & item, 'b').zfill(10)
        count = logical_and.count("1")
        result.append(count)
        # LOG.debug("{0} and {1} -> {2}".format(
        #     format(base_int, 'b').zfill(10), 
        #     format(item, 'b').zfill(10), 
        #     count))
    return result

def get_profits(pattern_array, lists):
    profits = 0
    for i in range(N):
        index = pattern_array[i]
        profit_list = lists[i]
        profits += profit_list[index]
        # LOG.debug("{0} : profits -> {1}".format(index, profits))
    return profits

def main():
    business_list = [int(input().replace(' ', ''), 2) for _ in range(N)]
    profits = [list(map(int, input().split())) for _ in range(N)]
    result = -float('inf')
    for i in range(1, 2 ** 10):
        open_pattern = get_count_logical_and(i, business_list)
        result = max(result, get_profits(open_pattern, profits))
        # LOG.debug("result -> {0}".format(result))
    print(result)

if __name__ == '__main__':
    main()