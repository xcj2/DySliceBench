def reach(s, x, y):
    for i in range(x, y-1):
        if s[i] == "#" and s[i+1] == "#":
            return False
    return True
def search(s, x, y):
    for i in range(x-1, y):
        if s[i] == "." and s[i+1] == "." and s[i+2] == ".":
            return True
        if s[i] == "#" and s[i+1] == "#":
            break
    return False

def main():
    n, a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    s = input().rstrip()
    if reach(s, a, c) and reach(s, b, d):
        if c < d:
            print("Yes")
        else:
            if search(s, b, d):
                print("Yes")
            else:
                print("No")

    else:
        print("No")

if __name__ == "__main__":
    main()