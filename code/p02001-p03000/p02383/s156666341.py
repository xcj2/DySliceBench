import sys

input = sys.stdin.readline

def south(dice):
    f, u, d, b = [dice["front"], dice["up"], dice["down"], dice["back"]]
    dice["front"] = u
    dice["up"] = b
    dice["down"] = f
    dice["back"] = d
    return dice

def north(dice):
    f, u, d, b = [dice["front"], dice["up"], dice["down"], dice["back"]]
    dice["front"] = d
    dice["up"] = f
    dice["down"] = b
    dice["back"] = u
    return dice

def west(dice):
    d, l, r, u = [dice["down"], dice["left"], dice["right"], dice["up"]]
    dice["down"] = l
    dice["left"] = u
    dice["right"] = d
    dice["up"] = r
    return dice

def east(dice):
    d, l, r, u = [dice["down"], dice["left"], dice["right"], dice["up"]]
    dice["down"] = r
    dice["left"] = d
    dice["right"] = u
    dice["up"] = l
    return dice

def show(dice):
    print(" ", dice["up"], " ")
    print(dice["left"], dice["front"], dice["right"], dice["back"])
    print(" ", dice["down"], " ")
    print()

def init_dice(dice_data):
    return {
        "front": dice_data[1], "back": dice_data[4],
        "up": dice_data[0], "right": dice_data[2], "down": dice_data[5], "left": dice_data[3]
    }

def main():
    pos = list(map(int, input().split()))
    move = input().rstrip()
    dice = init_dice(pos)
    for i in move:
        if i == "W":
            dice = west(dice)
        elif i == "S":
            dice = south(dice)
        elif i == "N":
            dice = north(dice)
        elif i == "E":
            dice = east(dice)

    print(dice["up"])
    
if __name__ == "__main__":
    main()
