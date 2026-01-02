def parse_formula(s, pointer):
    head = s[pointer]
    if head == "-":
        pointer += 1
        result, pointer = parse_formula(s, pointer)
        result = 2 - result
    elif head == "(":
        pointer += 1
        result_left, pointer = parse_formula(s, pointer)
        op, pointer = parse_op(s, pointer)
        result_right, pointer = parse_formula(s, pointer)
        result = calc(op, result_left, result_right)
        pointer += 1
    else:
        result = int(head)
        pointer += 1
    return result, pointer


def parse_op(s, pointer):
    return s[pointer], pointer + 1


calc_table1 = {(0, 0):0, (0, 1):0, (0, 2):0,
               (1, 0):0, (1, 1):1, (1, 2):1,
               (2, 0):0, (2, 1):1, (2, 2):2}
calc_table2 = {(0, 0):0, (0, 1):1, (0, 2):2,
               (1, 0):1, (1, 1):1, (1, 2):2,
               (2, 0):2, (2, 1):2, (2, 2):2}


def calc(op, left, right):
    if op == "*":return calc_table1[(left, right)]
    if op == "+":return calc_table2[(left, right)]


while True:
    formula = input()
    if formula == ".":
        break
    ans = 0
    for p in ("0", "1", "2"):
        sp = formula.replace("P", p)
        for q in ("0", "1", "2"):
            sq = sp.replace("Q", q)
            for r in ("0", "1", "2"):
                sr = sq.replace("R", r)
                if parse_formula(sr, 0)[0] == 2:
                    ans += 1
    print(ans)
