def solve():
    g, list_of_p_and_c = read()
    result = think(g, list_of_p_and_c)
    write(result)


def read():
    d, g = read_int(2)
    list_of_p_and_c = []
    for i in range(d):
        list_of_p_and_c.append(read_int(2))
    return g, list_of_p_and_c


def read_int(n):
    return list(map(int, read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(g, list_of_p_and_c):
    complete_bonus = []
    list_of_question_remained = []
    for p, c in list_of_p_and_c:
        list_of_question_remained.append(p)
        complete_bonus.append(c)

    return recursive_call(g, complete_bonus, list_of_question_remained, 0, 0, False, -1, {})


def recursive_call(g, complete_bonus, list_of_question_remained, questions_solved, subsum, in_halfway, what_of_halfway, cache):
    key = generate_key_for(list_of_question_remained)
    if key in cache:
        return cache[key]

    if subsum >= g:
        return questions_solved

    max_p = 100
    max_d = 10

    invalid = max_p * max_d + 1
    minimum_questions_to_be_solved = invalid

    local_list_of_question_remained = list(list_of_question_remained)

    if in_halfway:
        if list_of_question_remained[what_of_halfway] == 0:
            return invalid
        local_list_of_question_remained[what_of_halfway] -= 1
        return recursive_call(g, complete_bonus, local_list_of_question_remained, questions_solved + 1, subsum + 100 * (what_of_halfway + 1), True, what_of_halfway, cache)
    else:
        for i in range(len(list_of_question_remained)):
            if list_of_question_remained[i] == 0:
                continue  # already greedyed

            # case 1. greedy
            new_subsum = subsum + 100 * (i + 1) * list_of_question_remained[i] + complete_bonus[i]
            local_list_of_question_remained = list(list_of_question_remained)
            buf = local_list_of_question_remained[i]
            local_list_of_question_remained[i] = 0
            buf_2 = recursive_call(g, complete_bonus, local_list_of_question_remained, questions_solved + buf, new_subsum, False, -1, cache)

            minimum_questions_to_be_solved = min(minimum_questions_to_be_solved, buf_2)

            # case 2. not greedy, halfway
            new_subsum = subsum + 100 * (i + 1)
            local_list_of_question_remained = list(list_of_question_remained)
            local_list_of_question_remained[i] -= 1
            buf_2 = recursive_call(g, complete_bonus, local_list_of_question_remained, questions_solved + 1, new_subsum, True, i, cache)

            minimum_questions_to_be_solved = min(minimum_questions_to_be_solved, buf_2)

    cache[key] = minimum_questions_to_be_solved
    return minimum_questions_to_be_solved


def generate_key_for(list_of_question_remained):
    return ','.join(map(str, list_of_question_remained))


def write(result):
    print(result)


if __name__ == '__main__':
    solve()