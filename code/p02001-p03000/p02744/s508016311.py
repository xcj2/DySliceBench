
def get_normal_form(seq_type):
    curr_char = ord('a')
    return "".join([chr(curr_char + int(i)) for i in seq_type])


def submit():
    n = int(input())

    def rec(category, acc, result):
        if len(acc) == n:
            result.append(acc)
            return result

        for c in range(category):
            result = rec(category, acc + str(c), result)
        result = rec(category + 1, acc + str(category), result)

        return result

    result = rec(1, "0", [])
    result.sort()
    for r in result:
        print(get_normal_form(r))


if __name__ == "__main__":
    submit()
