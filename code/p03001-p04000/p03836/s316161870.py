sx, sy, tx, ty = map(int, input().split())
answer = ''

# x軸とy軸の値を揃える関数
def plus_x_arrange(first_x, second_x):
    add_x = ''
    while first_x < second_x:
        add_x += 'R'
        first_x += 1
    return add_x

def plus_y_arrange(first_y, second_y):
    add_y = ''
    while first_y < second_y:
        add_y += 'U'
        first_y += 1
    return add_y

def minus_x_arrange(first_x, second_x):
    add_x = ''
    while first_x < second_x:
        add_x += 'L'
        first_x += 1
    return add_x

def minus_y_arrange(first_y, second_y):
    add_y = ''
    while first_y < second_y:
        add_y += 'D'
        first_y += 1
    return add_y

# 鬼の条件分岐！！
if sx < tx and sy < ty:
    answer += plus_y_arrange(sy, ty)
    answer += plus_x_arrange(sx, tx)
    answer += minus_y_arrange(sy, ty)
    answer += minus_x_arrange(sx, tx)
    answer += 'L'
    answer += plus_y_arrange(sy, ty)
    answer += 'U'
    answer += 'R'
    answer += plus_x_arrange(sx, tx)
    answer += 'D'
    answer += 'R'
    answer += minus_y_arrange(sy, ty)
    answer += 'D'
    answer += 'L'
    answer += minus_x_arrange(sx, tx)
    answer += 'U'

elif sx < tx and sy == ty:
    answer += plus_x_arrange(sx, tx)
    answer += 'D'
    answer += minus_x_arrange(sx, tx)
    answer += 'U'
    answer += 'U'
    answer += plus_x_arrange(sx, tx)
    answer += 'D'
    answer += 'R'
    answer += 'D'
    answer += 'D'
    answer += 'L'
    answer += minus_x_arrange(sx, tx)
    answer += 'L'
    answer += 'U'
    answer += 'U'
    answer += 'R'

elif sx < tx and sy > ty:
    answer += plus_x_arrange(sx, tx)
    answer += minus_y_arrange(sy, ty)
    answer += minus_x_arrange(sx, tx)
    answer += plus_y_arrange(sy, ty)
    answer += 'U'
    answer += plus_x_arrange(sx, tx)
    answer += 'R'
    answer += 'D'
    answer += minus_y_arrange(sy, ty)
    answer += 'L'
    answer += 'D'
    answer += minus_x_arrange(sx, tx)
    answer += 'L'
    answer += 'U'
    answer += plus_y_arrange(sy, ty)
    answer += 'R'

elif sx == tx and sy > ty:
    answer += minus_y_arrange(sx, tx)
    answer += 'R'
    answer += plus_y_arrange(sx, tx)
    answer += 'L'
    answer += 'L'
    answer += minus_y_arrange(sx, tx)
    answer += 'R'
    answer += 'D'
    answer += 'R'
    answer += 'R'
    answer += 'U'
    answer += plus_y_arrange(sx, tx)
    answer += 'U'
    answer += 'L'
    answer += 'L'
    answer += 'D'

elif sx > tx and sy > ty:
    answer += minus_x_arrange(sx, tx)
    answer += minus_y_arrange(sy, ty)
    answer += plus_x_arrange(sx, tx)
    answer += plus_y_arrange(sy, ty)
    answer += 'U'
    answer += minus_x_arrange(sx, tx)
    answer += 'L'
    answer += 'D'
    answer += minus_y_arrange(sy, ty)
    answer += 'R'
    answer += 'D'
    answer += plus_x_arrange(sx, tx)
    answer += 'R'
    answer += 'U'
    answer += plus_y_arrange(sy, ty)
    answer += 'L'

elif sx > tx and sy == ty:
    answer += minus_x_arrange(sx, tx)
    answer += 'U'
    answer += plus_x_arrange(sx, tx)
    answer += 'D'
    answer += 'D'
    answer += minus_x_arrange(sx, tx)
    answer += 'U'
    answer += 'L'
    answer += 'U'
    answer += 'U'
    answer += 'R'
    answer += plus_x_arrange(sx, tx)
    answer += 'R'
    answer += 'D'
    answer += 'D'
    answer += 'L'
    
elif sx > tx and sy < ty:
    answer += minus_x_arrange(sx, tx)
    answer += plus_y_arrange(sy, ty)
    answer += plus_x_arrange(sx, tx)
    answer += minus_y_arrange(sy, ty)
    answer += 'D'
    answer += minus_x_arrange(sx, tx)
    answer += 'L'
    answer += 'U'
    answer += plus_y_arrange(sy, ty)
    answer += 'R'
    answer += 'U'
    answer += plus_x_arrange(sx, tx)
    answer += 'R'
    answer += 'D'
    answer += minus_y_arrange(sy, ty)
    answer += 'L'

else:
    answer += plus_y_arrange(sx, tx)
    answer += 'R'
    answer += minus_y_arrange(sx, tx)
    answer += 'L'
    answer += 'L'
    answer += plus_y_arrange(sx, tx)
    answer += 'R'
    answer += 'U'
    answer += 'R'
    answer += 'R'
    answer += 'D'
    answer += minus_y_arrange(sx, tx)
    answer += 'D'
    answer += 'L'
    answer += 'L'
    answer += 'U'

print(answer)