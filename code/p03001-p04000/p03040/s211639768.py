import heapq

def calc(keisuu_lower_max, keisuu_lower_sum,  keisuu_lower_count,
         keisuu_upper_sum, keisuu_upper_count, teisuu):
    print(keisuu_lower_max,
          - keisuu_lower_sum + keisuu_lower_count * keisuu_lower_max
          + keisuu_upper_sum - keisuu_upper_count * keisuu_lower_max + teisuu)


def lowerpush(keisuu_lower, a, keisuu_lower_max,  keisuu_lower_sum, keisuu_lower_count):
    heapq.heappush(keisuu_lower, -a)
    keisuu_lower_count += 1
    keisuu_lower_max = -keisuu_lower[0]
    keisuu_lower_sum += a
    return keisuu_lower, a, keisuu_lower_max,  keisuu_lower_sum, keisuu_lower_count


def upperpush(keisuu_upper, a, keisuu_upper_min, keisuu_upper_sum, keisuu_upper_count):
    heapq.heappush(keisuu_upper, a)
    keisuu_upper_count += 1
    keisuu_upper_min = keisuu_upper[0]
    keisuu_upper_sum += a
    return keisuu_upper, a, keisuu_upper_min,  keisuu_upper_sum, keisuu_upper_count


def from_lower_to_upper(keisuu_lower, keisuu_lower_max, keisuu_lower_sum, keisuu_lower_count,
                        keisuu_upper, keisuu_upper_min, keisuu_upper_sum, keisuu_upper_count):

    e = -heapq.heappop(keisuu_lower)
    heapq.heappush(keisuu_upper, e)
    keisuu_lower_sum -= e
    keisuu_upper_sum += e
    keisuu_lower_max = -keisuu_lower[0]
    keisuu_upper_min = e
    keisuu_lower_count -= 1
    keisuu_upper_count += 1

    return keisuu_lower, keisuu_lower_max, keisuu_lower_sum, keisuu_lower_count, keisuu_upper, keisuu_upper_min, keisuu_upper_sum, keisuu_upper_count


def from_upper_to_lower(keisuu_lower, keisuu_lower_max, keisuu_lower_sum, keisuu_lower_count,
                        keisuu_upper, keisuu_upper_min, keisuu_upper_sum, keisuu_upper_count):

    d = heapq.heappop(keisuu_upper)
    heapq.heappush(keisuu_lower, -d)
    keisuu_lower_sum += d
    keisuu_upper_sum -= d
    keisuu_lower_max = d
    keisuu_upper_min = keisuu_upper[0]
    keisuu_lower_count += 1
    keisuu_upper_count -= 1

    return keisuu_lower, keisuu_lower_max, keisuu_lower_sum, keisuu_lower_count, keisuu_upper, keisuu_upper_min, keisuu_upper_sum, keisuu_upper_count


def main():
    q = int(input())
    keisuu_lower = []
    keisuu_upper = []
    keisuu_lower_max = 0
    keisuu_upper_min = float("inf")
    keisuu_lower_count = 0
    keisuu_upper_count = 0
    keisuu_lower_sum = 0
    keisuu_upper_sum = 0
    teisuu = 0

    for i in range(q):
        query = input()
        if query == "2":
            calc(keisuu_lower_max, keisuu_lower_sum, keisuu_lower_count,
                 keisuu_upper_sum, keisuu_upper_count, teisuu)

        else:
            _, a, b = [int(i) for i in query.split()]
            teisuu += b

            if a < keisuu_lower_max:
                keisuu_lower, a, keisuu_lower_max, keisuu_lower_sum, keisuu_lower_count \
                    = lowerpush(keisuu_lower, a, keisuu_lower_max, keisuu_lower_sum, keisuu_lower_count)

            elif a > keisuu_upper_min:
                keisuu_upper, a, keisuu_upper_min, keisuu_upper_sum, keisuu_upper_count \
                    = upperpush(keisuu_upper, a, keisuu_upper_min, keisuu_upper_sum, keisuu_upper_count)

            elif keisuu_lower_count == keisuu_upper_count:
                keisuu_lower, a, keisuu_lower_max, keisuu_lower_sum, keisuu_lower_count \
                    = lowerpush(keisuu_lower, a, keisuu_lower_max, keisuu_lower_sum, keisuu_lower_count)

            else:
                keisuu_upper, a, keisuu_upper_min, keisuu_upper_sum, keisuu_upper_count \
                    = upperpush(keisuu_upper, a, keisuu_upper_min, keisuu_upper_sum, keisuu_upper_count)

            if keisuu_lower_count > keisuu_upper_count + 1:
                keisuu_lower, keisuu_lower_max, keisuu_lower_sum, keisuu_lower_count, keisuu_upper, keisuu_upper_min, keisuu_upper_sum, keisuu_upper_count \
                    = from_lower_to_upper(keisuu_lower, keisuu_lower_max, keisuu_lower_sum, keisuu_lower_count,
                                          keisuu_upper, keisuu_upper_min, keisuu_upper_sum, keisuu_upper_count)

            elif keisuu_lower_count < keisuu_upper_count:
                keisuu_lower, keisuu_lower_max, keisuu_lower_sum, keisuu_lower_count, keisuu_upper, keisuu_upper_min, keisuu_upper_sum, keisuu_upper_count \
                    = from_upper_to_lower(keisuu_lower, keisuu_lower_max, keisuu_lower_sum, keisuu_lower_count,
                                          keisuu_upper, keisuu_upper_min, keisuu_upper_sum, keisuu_upper_count)


main()