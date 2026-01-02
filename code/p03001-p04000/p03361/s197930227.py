def main():
    h, w = map(int, input().split())
    m = []

    for _ in range(h):
        line = input()
        m.append(line)

    if judge_map(m):
        print('Yes')
    else:
        print('No')

def judge_map(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if not judge(m, i, j):
                return False
    return True

def judge(m, i, j):
    if m[i][j] == '.':
        return True
    
    if i - 1 >= 0 and m[i - 1][j] == '#':
        return True
    
    if i + 1 < len(m) and m[i + 1][j] == '#':
        return True
    
    if j - 1 >= 0 and m[i][j-1] == '#':
        return True
    
    if j + 1 < len(m[i]) and m[i][j + 1] == '#':
        return True
    
    return False


main()