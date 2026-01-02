def move_dice(d, dir):
    if(dir == 'N'):
        d[0], d[1], d[4], d[5] = d[1], d[5], d[0], d[4]
    if(dir == 'S'):
        d[0], d[1], d[4], d[5] = d[4], d[0], d[5], d[1]
    if(dir == 'E'):
        d[0], d[2], d[3], d[5] = d[3], d[0], d[5], d[2]
    if(dir == 'W'):
        d[0], d[2], d[3], d[5] = d[2], d[5], d[0], d[3]

def rotate_right_dice(d):
    d[1], d[2], d[3], d[4] = d[3], d[1], d[4], d[2]

def to_up_dice(d, num):
    num_index = d.index(num)
    if(num_index==2 or num_index==3):
        move_dice(d, 'E')
    while(d[0] != num):
        move_dice(d, 'N')

def to_front_dice(d, num):
    while(d[1] != num):
        rotate_right_dice(d)

dice = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    up, front = map(int, input().split())
    to_up_dice(dice, up)
    to_front_dice(dice, front)
    print(dice[2])