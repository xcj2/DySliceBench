def is_odd(number):
    return number % 2 != 0
import sys

def draw_line(chk1, chk2, W):
    print((chk1 + chk2) * int(W / 2), end='')
    if is_odd(W):print(chk1, end='')
    print()
    
def draw_odd_line(W):
    draw_line('#', '.', W)
    
def draw_even_line(W):
    draw_line('.', '#', W)

def draw(H, W):
    for i in range(int(H / 2)):
        draw_odd_line(W)
        draw_even_line(W)
    if is_odd(H):draw_odd_line(W)
    print()
    
for line in sys.stdin:
    H, W = map(int, line.split())
    if H == W == 0:
        break
    draw(H, W)