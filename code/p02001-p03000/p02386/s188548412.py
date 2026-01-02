def dice_rotation(dice, command):

	tmp_dice = []
	
	for i in range(6):
		tmp_dice.append(dice[i])

	#S:1->2,2->6,6->5,5->1
	if command == 'S':
		dice[0] = tmp_dice[4]
		dice[4] = tmp_dice[5]
		dice[5] = tmp_dice[1]
		dice[1] = tmp_dice[0]
	#N:1->5,5->6,6->2,2->1
	elif command == 'N':
		dice[0] = tmp_dice[1]
		dice[1] = tmp_dice[5]
		dice[5] = tmp_dice[4]
		dice[4] = tmp_dice[0]
	#W:1->4,4->6,6->3,3->1
	elif command == 'W':
		dice[0] = tmp_dice[2]
		dice[2] = tmp_dice[5]
		dice[5] = tmp_dice[3]
		dice[3] = tmp_dice[0]
	#E:1->3,3->6,6->4,4->1
	elif command == 'E':
		dice[0] = tmp_dice[3]
		dice[3] = tmp_dice[5]
		dice[5] = tmp_dice[2]
		dice[2] = tmp_dice[0]

def dice_spinning(dice):

	tmp_dice = []
	
	for i in range(6):
		tmp_dice.append(dice[i])

	dice[1] = tmp_dice[2]
	dice[2] = tmp_dice[4]
	dice[4] = tmp_dice[3]
	dice[3] = tmp_dice[1]

def comparison_dices(Dice1,Dice2):

	yes_counter = 0
	for j in range(6):
		if Dice1[j] == Dice2[j]:
			yes_counter += 1
	if yes_counter == 6:
		return True

	return False

def full_validation_dices(Dice1,Dice2):

	judgement_result = False

	#1st direction
	for i in range(4):
		for j in range(4):
			if comparison_dices(Dice1,Dice2) == True:
				judgement_result = True
				break
			else:
				dice_spinning(Dice2)

		if judgement_result == True:
			break
		else:
			dice_rotation(Dice2,'S')

	#2nd direction
	for i in range(4):
		for j in range(4):
			if comparison_dices(Dice1,Dice2) == True:
				judgement_result = True
				break
			else:
				dice_spinning(Dice2)

		if judgement_result == True:
			break
		else:
			dice_rotation(Dice2,'W')

	if judgement_result == True:
		return True
	else:
		return False


def test():

	n = int(input())

	Dices = []

	result = True

	for i in range(n):

		tmp_dice = list(map(int,input().split()))
		Dices.append(tmp_dice)
	
	for i in range(n-1):
		for j in range(i+1,n):
			if full_validation_dices(Dices[i],Dices[j]) == True:
				result = False
				break
		if result == False:
			break

	if result == True:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	test()


