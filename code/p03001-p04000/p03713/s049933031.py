def main():
    h, w = map(int, input().split())
    print(min(solve(h, w), solve(w, h)))

def solve(h, w):
    m = float('inf')

    for i in range(1, h):
        a = i * w
        m = min(m, divide2(h - i, w, a))
    
    return m

def divide2(h, w, a):
    m = float('inf')
    
    if h >= 2:
        i = h // 2
        b = w * i
        c = w * (h - i)
        m = min(m, max(a, b, c) - min(a, b, c))
    
    if w >= 2:
        i = w // 2
        b = h * i
        c = h * (w - i)
        m = min(m, max(a, b, c) - min(a, b, c))
    
    return m

main()
