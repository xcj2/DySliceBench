import sys

class Rect():
    def __init__(self,w,h):
        self.w = w
        self.h = h

    def draw(self):
        for i in range(self.w):
            for j in range(self.h):
                checked = (i+j) % 2 == 0
                if checked:
                    sys.stdout.write("#")
                else:
                    sys.stdout.write(".")
            sys.stdout.write("\n")
        sys.stdout.write("\n")

def main():
    data = []
    while 1:
        n = input().split()
        w = int(n[0])
        h = int(n[1])

        if w == 0 and h == 0:
            break

        data.append(Rect(w,h))

    for num in data:
        num.draw()

if __name__ == "__main__":
    main()