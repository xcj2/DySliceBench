# coding=utf-8

class Tree():
    def __init__(self, init_field):
        self.root = init_field

    def search(self, field_id, field):
        global final_queen_pos
        #print("field_id:", field_id)
        #field.print_field()
        q_r = rest_row[field_id - n]
        if final_queen_pos:
            return None
        else:
            for q_c, cell in enumerate(field.state[q_r]):
                if cell == 0:
                    if final_queen_pos:
                        break
                    if field_id == 7:
                        field.queen_pos.append([q_r, q_c])
                        final_queen_pos = field.queen_pos
                        break
                    else:
                        next_field = Field(field_id + 1, field)
                        field.children.append(next_field)
                        next_field.update(q_r, q_c)
                        self.search(field_id + 1, next_field)
                else:
                    continue

class Field():
    def __init__(self, field_id, parent=None):
        self.id = field_id
        self.parent = parent
        self.children = []

        if field_id == 0:
            self.state = [[0 for _ in range(W)] for H in range(H)]
            self.queen_pos = []
        else:
            self.state = []
            self.queen_pos = []
            for row in self.parent.state:
                x = row.copy()
                self.state.append(x)
            for parent_queen_pos in self.parent.queen_pos:
                self.queen_pos.append(parent_queen_pos)

    def update(self, q_r, q_c):
        self.queen_pos.append([q_r, q_c])
        for i in range(8):
            self.state[q_r][i] = 1
            self.state[i][q_c] = 1
        summ = q_c + q_r
        diff = q_c - q_r
        for i in range(8):
            if (0 <= i + diff < 8):
                self.state[i][i + diff] = 1
            if (0 <= summ - i < 8):
                self.state[i][summ - i] = 1

    def print_field(self): #for debug
        print("queen_pos:", self.queen_pos)
        for row in self.state:
            print(*row)


H, W = 8, 8
n = int(input())
init_field = Field(0)
tree = Tree(init_field)
field_list = [init_field]
rest_row = [i for i in range(8)]
queen_pos = []
final_queen_pos = None
final_result = [["." for _ in range(8)] for _ in range(8)]

for _ in range(n):
    r, c = map(int, input().split())
    queen_pos.append([r, c])
    rest_row.remove(r)

if n < 8:
    i = 0
    prev_field = init_field
    for q_r, q_c in queen_pos:
        i += 1
        field = Field(i, prev_field)
        field.update(q_r, q_c)
        field_list.append(field)
        prev_field.children = [field]
        prev_field = field

    tree.search(i, field)

    for q_r, q_c in final_queen_pos:
        final_result[q_r][q_c] = "Q"

    for row in final_result:
        print("".join(row), end = "\n")

else:
    for q_r, q_c in queen_pos:
        final_result[q_r][q_c] = "Q"

    for row in final_result:
        print("".join(row), end = "\n")