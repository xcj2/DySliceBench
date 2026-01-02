import copy
def main():
    n, k = map(int, input().rstrip().split(' '))
    s = [c == '1' for c in input().rstrip()]

    windows = []
    current_window = None
    for i, c in enumerate(s):
        if not c:
            if current_window  == None:
                current_window = Window(False)
            elif current_window.one:
                windows.append(current_window)
                current_window = Window(False)
            current_window.count += 1
        else:
            if current_window  == None:
                current_window = Window(True)
            elif not current_window.one:
                windows.append(current_window)
                current_window = Window(True)
            current_window.count += 1
    windows.append(current_window)
    
    counts = []
    count = 0
    zero_window_count = 0
    for i, w in enumerate(windows):
        if not w.one:
            zero_window_count += 1
            if zero_window_count > k:
                counts.append(count)
                leftmost = i - (2 * k) - 1
                if leftmost >= 0:
                    count -= windows[leftmost].count #1s, if exist
                count -= windows[leftmost + 1].count #0s

        count += w.count
    counts.append(count)
    print(max(counts))

class Window:
    def __init__(self, one_or_zero):
        self.one = one_or_zero
        self.count = 0
    
    def __repr__(self):
        return ("1" if self.one else "0") + " " + str(self.count)


if __name__ == '__main__':
    main()