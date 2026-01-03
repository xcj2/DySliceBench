def vertical_move(move):
    if move >= 0:
        return "U" * move
    return "D" * (-move)

def horizontal_move(move):
    if move >= 0:
        return "R" * move
    return "L" * (- move)

def opposite_horizontal_to_vertical(sx, sy, tx, ty):
    ans = ""
    first_opposite = ""
    vertical = ""
    horizontal = ""
    last_opposite = ""
    if sx <= tx:
        first_opposite = "L"
        horizontal = horizontal_move(tx - sx + 1)
    else:
        first_opposite = "R"
        horizontal = horizontal_move(tx - sx - 1)
        
    if sy <= ty:
        last_opposite = "D"
        vertical = vertical_move(ty + 1 - sy)
    else:
        last_opposite = "U"
        vertical = vertical_move(ty - 1 - sy)
        
    return first_opposite + vertical + horizontal + last_opposite

sx, sy, tx, ty = map(int, input().split())

ans = ""
ans += vertical_move(ty - sy)
ans += horizontal_move(tx - sx)
ans += vertical_move(sy - ty)
ans += horizontal_move(sx - tx)

ans += opposite_horizontal_to_vertical(sx, sy, tx, ty)
ans += opposite_horizontal_to_vertical(tx, ty, sx, sy)

print(ans)
