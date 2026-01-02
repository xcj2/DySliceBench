def hightMapGenerator(text):
    height_map = []
    current_height = 0
    for letter in text:
        if letter == '\\':
            current_height -= 1
        elif letter == '/':
            current_height += 1
        else :
            pass
        height_map.append(current_height)
    return height_map

def pondChecker(text, height_map):
    # 判定
    all_ponds = []
    pond = []
    for n, letter in enumerate(text):
        if pond == []: # 池オブジェクトが空の場合
            if letter == '\\': # かつ、文字列がa の場合
                max_height = max(height_map[n:])
                if height_map[n] + 1 <= max_height: # 現在地よりも、高度の高い位置があるならば
                    start_index = n
                    pond.append(start_index) # スタート位置としてインデックスする
                else :
                    pass
        else : # 池オブジェクとにスタートが入っている場合
            if height_map[start_index] + 1 == height_map[n]: # スタートインデックスと同じ高さに来たら終わりをインデックスして、初期化
                end_index = n
                pond.append(end_index)
                all_ponds.append(pond)
                pond = []
    return all_ponds
    
def squareCalc(text, pond_height_map):
    square = 0
    current_height = max(pond_height_map)
    for n, letter in enumerate(text):
        if letter == '\\':
            square += current_height - pond_height_map[n] - 0.5
        elif letter == '/':
            square += current_height - pond_height_map[n] + 0.5
        else :
            square += current_height - pond_height_map[n]
    return int(square)

def slicedPondsGenerator(text, height_map, all_ponds):
    sliced_ponds_str = []
    sliced_height_map = []
    for pond in all_ponds:
        start = pond[0]
        end = pond[1] + 1
        sliced_pond_str = text[start:end]
        sliced_height = height_map[start:end]
        sliced_ponds_str.append(sliced_pond_str)
        sliced_height_map.append(sliced_height)
    return sliced_ponds_str, sliced_height_map

text = input()

if '/' not in text:
    print(0)
    print(0)
elif '\\' not in text:
    print(0)
    print(0)
else :
    height_map = hightMapGenerator(text)
    # print(height_map)
    all_ponds = pondChecker(text, height_map)
    if all_ponds == []:
        print(0)
        print(0)
    else :
        # print(all_ponds)
        sliced_ponds_str, sliced_height_map = slicedPondsGenerator(text, height_map, all_ponds)
        # print(ponds_str)
        # print(sliced_height_map)
        squares = []
        for n, pond_str in enumerate(sliced_ponds_str):
            square = squareCalc(pond_str, sliced_height_map[n])
            squares.append(square)

        size_of_ponds = sum(squares)
        num_of_ponds = len(squares)
        output = ' '.join([str(n) for n in squares])
        print(size_of_ponds)
        print(num_of_ponds,output)
