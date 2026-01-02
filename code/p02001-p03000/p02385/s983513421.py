class Dice:
    
    keys = [ 
        "top", 
        "front", 
        "right", 
        "left", 
        "back", 
        "bottom"
        ]
    keys_for_top = [
            ["front", "right", "back", "left", "bottom"],
            ["bottom", "right", "top", "left", "back"],
            ["bottom", "back", "top", "front", "left"],
            ["bottom", "front", "top", "back", "right"],
            ["bottom", "left", "top", "right", "front"],
            ["front", "left", "back", "right", "top"]
        ]

    def __init__(self, eye1, eye2, eye3, eye4, eye5, eye6):
        self.__eyes = {
            "top": eye1,
            "front": eye2,
            "right": eye3,
            "left": eye4,
            "back": eye5,
            "bottom": eye6
        }

    def set_eyes(self, eye1, eye2, eye3, eye4, eye5, eye6):
        self.__eyes["top"] = eye1
        self.__eyes["front"] = eye2
        self.__eyes["right"] = eye3
        self.__eyes["left"] = eye4
        self.__eyes["back"] = eye5
        self.__eyes["bottom"] = eye6
    
    def get_eyes(self, key):
        return self.__eyes[key]

    def N(self):
        self.set_eyes(
            self.get_eyes("front"),
            self.get_eyes("bottom"),
            self.get_eyes("right"),
            self.get_eyes("left"),
            self.get_eyes("top"),
            self.get_eyes("back")
            )
    def S(self):
        self.set_eyes(
            self.get_eyes("back"),
            self.get_eyes("top"),
            self.get_eyes("right"),
            self.get_eyes("left"),
            self.get_eyes("bottom"),
            self.get_eyes("front")
            )
        
    def E(self):
        self.set_eyes(
            self.get_eyes("left"),
            self.get_eyes("front"),
            self.get_eyes("top"),
            self.get_eyes("bottom"),
            self.get_eyes("back"),
            self.get_eyes("right")
            )
        
    def W(self):
        self.set_eyes(
            self.get_eyes("right"),
            self.get_eyes("front"),
            self.get_eyes("bottom"),
            self.get_eyes("top"),
            self.get_eyes("back"),
            self.get_eyes("left")
            )
    
    def print_top(self):
        print(self.get_eyes("top"))

    def guess_right_from_top_front(self, top, front):
        key_top = None
        key_front = None
        
        for key in Dice.keys:
            if top == self.get_eyes(key):
                key_top = key
            if front == self.get_eyes(key):
                key_front = key
        

        for i in range(6):
            if key_top == Dice.keys[i]:
                for j in range(4):
                    if key_front == Dice.keys_for_top[i][j]:
                        return Dice.keys_for_top[i][(j + 1) % 4]
        return False

    @classmethod
    def generate_all_states(cls, dice):
        dices = []
        for i in range(6):
            for j in range(4):
                dices.append(cls(
                    dice.get_eyes(Dice.keys[i]),
                    dice.get_eyes(Dice.keys_for_top[i][j]),
                    dice.get_eyes(Dice.keys_for_top[i][(j + 1) % 4]),
                    dice.get_eyes(Dice.keys_for_top[i][(j + 3) % 4]),
                    dice.get_eyes(Dice.keys_for_top[i][(j + 2) % 4]),
                    dice.get_eyes(Dice.keys_for_top[i][4])
                    ))
        return dices
    
    @classmethod
    def is_same_states(cls, dice1, dice2):
        for i in range(6):
            if dice1.get_eyes(Dice.keys[i]) != dice2.get_eyes(Dice.keys[i]):
                return False
        return True
    
    @classmethod
    def is_same_dices(cls, dice1, dice2):
        all_states_dice2 = Dice.generate_all_states(dice2)
        for i in range(24):
            if Dice.is_same_states(dice1, all_states_dice2[i]):
                return True
        return False   

eyes1 = list(map(int, input().split()))
eyes2 = list(map(int, input().split()))

dice1 = Dice(eyes1[0], eyes1[1], eyes1[2], eyes1[3], eyes1[4], eyes1[5])
dice2 = Dice(eyes2[0], eyes2[1], eyes2[2], eyes2[3], eyes2[4], eyes2[5])
if Dice.is_same_dices(dice1, dice2):
    print("Yes")
else:
    print("No")
