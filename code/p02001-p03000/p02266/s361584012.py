def cal_puddle(puddle):
    depth = 0
    score = 0
    for s in puddle:
        if s == "\\":
            score += depth + 0.5
            depth += 1
        elif s == "/":
            depth -= 1
            score += depth + 0.5
        elif s == "_":
            score += depth

        if depth == 0:
            return int(score)
    return int(score)

def get_puddles(diagram):
    hight = 0
    top_list = []
    in_puddle = True
    for index, s in enumerate(diagram + "\\"):
        if s == "/":
            in_puddle = True
            hight += 1
        if s == "\\":
            if in_puddle:
                in_puddle = False
                top_list.append([hight, index])
            hight -= 1

    puddles = []
    prev_hight = 0
    hight_list = [h for h, i in top_list]
    i = 0
    while i < len(top_list) - 1:
        cur_top = top_list[i]
        next_tops = list(filter(lambda top:cur_top[0] <= top[0], top_list[i + 1:]))
        #print(next_tops)
        if next_tops:
            next_top = next_tops[0]
            puddles.append((cur_top[1], next_top[1]))
            i = top_list.index(next_top)
        else:
            cur_top[0] -= 1
            cur_top[1] += diagram[cur_top[1] + 1:].index("\\") + 1
    #print(hight_list)
    #print(top_list)
    #print(puddles)
    return puddles

def main():
    diagram = input()
    result = []
    for s,e in get_puddles(diagram):
        result.append(cal_puddle(diagram[s:e]))
    print(sum(result))
    print(str(len(result)) + "".join([" " + str(i) for i in result]))
if __name__ == "__main__":
    main()