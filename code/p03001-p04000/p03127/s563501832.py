num = int(input())

monsters_hp = [int(i) for i in input().split()]

attacker = 0

def attack(attacker, monsters_hp):
    for i in range(len(monsters_hp)):
        if i == attacker:
            continue
        else:
            monster_hp = monsters_hp[i]
            if monsters_hp[attacker] == 0:
                continue
            hp_mod = monster_hp % monsters_hp[attacker]
            monsters_hp[i] = hp_mod
    return monsters_hp

def calc_zero(monsters_hp):
    count = 0
    for monster_hp in monsters_hp:
        if monster_hp == 0:
            count += 1
    return count

def change_attacker(monsters_hp):
    minimum = calc_minimum(monsters_hp)
    for i in range(len(monsters_hp)):
        if monsters_hp[i] == minimum:
            return i
def calc_minimum(monsters_hp):
    minimum = monsters_hp[0]
    for i in range(len(monsters_hp)):
        if monsters_hp[i] == 0:
            continue
        elif minimum >= monsters_hp[i]:
            minimum = monsters_hp[i]
    if minimum == 0:
        minimum += 1
    return minimum

while True:
    attack(attacker, monsters_hp)
    attacker = change_attacker(monsters_hp)
    count = calc_zero(monsters_hp)
    if count == (len(monsters_hp) - 1):
        break

print(max(monsters_hp))