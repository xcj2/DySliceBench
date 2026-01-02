inputs = list(map(int, list('1222')))
target = 7


def prepare():
    global inputs
    inputs = list(map(int, list(input())))


def dfs(depth, value, form):
    if depth == len(inputs):
        if value == target:
            return True, form + '=' + str(target)
        else:
            return False, form

    result1, form1 = dfs(depth + 1, value + inputs[depth],
                         (form + '+'
                          if depth > 0 else '') + str(inputs[depth]))
    if result1 is True:
        return result1, form1

    result2, form2 = dfs(depth + 1, value - inputs[depth],
                         (form + '-'
                          if depth > 0 else '') + str(inputs[depth]))
    if result2 is True:
        return result2, form2

    return False, ''


def solve():
    result, form = dfs(0, 0, '')
    if result is True:
        print(form)


prepare()
solve()
