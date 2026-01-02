def listToStr(list):
    return ''.join(list)

def getChar(h, w):
    h_parity = h % 2
    w_parity = w % 2
    total_parity = (h_parity + w_parity) % 2
    
    if total_parity == 0:
        return "#"
    else:
        return "."

def getMatrix(h, w):
    result = []
    for i in range(h):
        result.append([])
        for j in range(w):
            result[i].append(getChar(i, j))
    return result

def input_parse():
    inputs = []
    while True:
        input_HW = input().split(" ")
        (h, w) = (int(input_HW[0]),int(input_HW[1]))
        if h == 0 and w == 0:
            break
        inputs.append((h, w))
    return inputs

def output_matrix(matrix):
    for line in matrix:
        print(listToStr(line))
    print()

inputs = input_parse()
for input in inputs:
    matrix = getMatrix(input[0], input[1])
    output_matrix(matrix),0