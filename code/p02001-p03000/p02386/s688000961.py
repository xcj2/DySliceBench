class Dice:
    """Dice class"""
    def __init__(self):                  # ?????????????????????
        self.eyeIndex = 1        #center
        self.eyeIndex_E = 3      #east
        self.eyeIndex_W = 4      #west
        self.eyeIndex_N = 5      #north
        self.eyeIndex_S = 2      #south
        self.eye = 0
        self.eye_S = 0
        self.eye_E = 0
        self.eye_W = 0
        self.eye_N = 0
        self.eye_B = 0
        self.eyes = []

    def convEyesIndexToEyes(self):
        self.eye = self.eyes[self.eyeIndex]
        self.eye_S = self.eyes[self.eyeIndex_S]
        self.eye_E = self.eyes[self.eyeIndex_E]
        self.eye_N = self.eyes[self.eyeIndex_N]
        self.eye_W = self.eyes[self.eyeIndex_W]
        self.eye_B = self.eyes[7-self.eyeIndex]

    def shakeDice(self, in_command):
        pre_eyeIndex = self.eyeIndex
        if in_command == "E":
            self.eyeIndex = self.eyeIndex_W 
            self.eyeIndex_E = pre_eyeIndex 
            self.eyeIndex_W = 7 - self.eyeIndex_E
            
        elif in_command == "W":
            self.eyeIndex = self.eyeIndex_E 
            self.eyeIndex_W = pre_eyeIndex
            self.eyeIndex_E = 7 - self.eyeIndex_W
            
        elif in_command == "N":
            self.eyeIndex = self.eyeIndex_S 
            self.eyeIndex_N = pre_eyeIndex 
            self.eyeIndex_S = 7 - self.eyeIndex_N

        elif in_command == "S":
            self.eyeIndex = self.eyeIndex_N         
            self.eyeIndex_S = pre_eyeIndex 
            self.eyeIndex_N = 7 - self.eyeIndex_S 
        
        self.convEyesIndexToEyes()


    def rotateDice(self):
        #rotate clockwise
        pre_E = self.eyeIndex_E
        pre_S = self.eyeIndex_S
        pre_W = self.eyeIndex_W
        pre_N = self.eyeIndex_N
        
        self.eyeIndex_E = pre_N
        self.eyeIndex_S = pre_E
        self.eyeIndex_W = pre_S
        self.eyeIndex_N = pre_W

        self.convEyesIndexToEyes()
        
    def getEye(self):
        return self.eye
        
    def getEye_S(self):
        return self.eye_S
    
    def getEye_E(self):
        return self.eye_E

    def getEye_N(self):
        return self.eye_N

    def getEye_W(self):
        return self.eye_W

    def getEye_B(self):
        return self.eye_B
        
    def setEyes(self, eyes):             # setEyes()???????????? ???????????????
        eyes = "0 " + eyes
        self.eyes = list(map(int, eyes.split(" ")))
        self.convEyesIndexToEyes()
        

def checkSameDice(dice_1, dice_2):
    shake_direction = "E"
    shake_cnt = 0

    while True:
        if dice_2.getEye() == dice_1.getEye() and dice_2.getEye_B() == dice_1.getEye_B():
            break
    
        dice_2.shakeDice(shake_direction)
        shake_cnt = shake_cnt + 1
        
        if shake_cnt >= 8:
            return False
            break
        if shake_cnt >= 4:
            shake_direction = "N"

    rotate_cnt = 0
    
    while True:
        if dice_1.getEye() == dice_2.getEye() and dice_1.getEye_E() == dice_2.getEye_E() and \
            dice_1.getEye_S() == dice_2.getEye_S() and dice_1.getEye_W() == dice_2.getEye_W() and \
            dice_1.getEye_N() == dice_2.getEye_N():
            break
        
        dice_2.rotateDice()
        rotate_cnt = rotate_cnt + 1
        
        if rotate_cnt >= 5:
            return False
            
    return True


dice_cnt = int(input().rstrip())

#dice_eyes = [" " for i in range(dice_cnt)]
dices = []

#set all dices
for i in range(dice_cnt):
    #dice_eyes[i] = input().rtstrip()
    tmpDice = Dice()
    tmpDice.setEyes(input().rstrip())
    dices.append(tmpDice)
    tmpDice = None


judge = "Yes"
for i in range(dice_cnt):
    for j in range(i+1, dice_cnt):
        if checkSameDice(dices[i],dices[j]):
            judge = "No"
            break
    
    if judge == "No":
        break
            
print(judge)