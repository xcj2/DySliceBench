# coding: utf-8
def get_ln_inputs():
    return input().split()


def get_ln_int_inputs():
    return list(map(int, get_ln_inputs()))


def can_construct_palindromic_matrix(char_counts, H, W):
    double_placeable_cells = (H >> 1 if W & 1 else 0) + (W >> 1 if H & 1 else 0)
    single_placeable_cell = (H & W) & 1

    counts_mod4 = list(map(lambda x : x % 4, char_counts))
    counts_div4 = list(map(lambda x : x // 4, char_counts))
    if counts_mod4.count(1) + counts_mod4.count(3) > single_placeable_cell:
        return False

    counts_mod4 = list(map(lambda x : 0 if x & 1 else x, counts_mod4))
    if counts_mod4.count(2) > double_placeable_cells or (double_placeable_cells - counts_mod4.count(2)) & 1:
        return False

    return True


def main():
    H, W = get_ln_int_inputs()
    matrix = list()
    for _ in range(H):
        matrix.append(get_ln_inputs()[0])
    
    counts = [0 for _ in range(26)]
    for i in range(H):
        for j in range(W):
            character = matrix[i][j]
            counts[ord(character) - 97] += 1
    
    print("Yes" if can_construct_palindromic_matrix(counts, H, W) else "No")
    return


main()