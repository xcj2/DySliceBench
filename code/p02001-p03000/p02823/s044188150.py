def even(d):
    return d // 2

def odd(A, B, N):
    if abs(A-1) > abs(B-N):
        dist2edge = abs(B-N)
        A += dist2edge
        B += dist2edge 

        return even(abs((A+1)- B)) + 1 + dist2edge

    else:
        dist2edge = abs(A - 1)
        A -= dist2edge
        B -= dist2edge
    
        return even(abs(A- (B-1))) + 1 + dist2edge


def main():
    N, A, B = map(int, input().split())
    diff = abs(A-B)

    if diff % 2 == 0:
        print(even(diff))
    else:
        print(odd(A, B, N))

if __name__ == "__main__":
    main()
