# coding: utf-8
def get_ln_inputs():
    return input().split()


def get_ln_int_inputs():
    return list(map(int, get_ln_inputs()))


def get_composable_numbers(a, b, lim):
    result = set()
    result.add(0)
    if a < lim:
        result.add(a)
    if b < lim:
        result.add(b)

    for c in range(max(result), lim + 1):
        if (c - a) in result or (c - b) in result:
            result.add(c)

    return list(result)

def get_concentration(water, suger):
    return suger / (water + suger)

def max_below(array, limit):
    max_res = array[0]
    for elem in array:
        if elem > max_res and elem <= limit:
            max_res = elem
        elif elem >= limit:
            break

    return max_res

def main():
    a, b, C, D, E, F = get_ln_int_inputs()
    A = 100 * a
    B = 100 * b
    water_composables = sorted(list(map(lambda x: x * 100, get_composable_numbers(a, b, F // 100))))
    suger_composables = sorted(get_composable_numbers(C, D, (E * F) // 100))

    res_tuple = (A, 0)
    max_concentration = 0
    for i in range(1, len(water_composables)):
        water = water_composables[i]
        suger_max = max_below(suger_composables, min((water * E) // 100, F - water))
        mass = water + suger_max

        concentration = get_concentration(water, suger_max)
        if concentration > max_concentration:
            max_concentration = concentration
            res_tuple = (water + suger_max, suger_max)
    
    print(str(res_tuple[0]) + " " + str(res_tuple[1]))
    return

main()