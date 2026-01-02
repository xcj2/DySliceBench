def seek(n, s):
    s = s.rstrip('#').lstrip('.')
    turn_to_black = s.count('.')
    current_min = turn_to_black
    turn_to_white = 0

    if current_min == 0 or current_min == len(s):
        return 0

    # seek minimum turns to create "^\.*#*$"
    for i in range(len(s)):
        if s[i] == '#':
            turn_to_white += 1
        else:
            turn_to_black -= 1
        current_min = min(current_min, turn_to_black + turn_to_white)
    return current_min


def input_from_console():
    n = int(input())
    s = input()
    return n, s


def main():
    n, s = input_from_console()
    print(seek(n, s))
    

if __name__ == "__main__":
    main()
