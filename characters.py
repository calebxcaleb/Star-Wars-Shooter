import imgpath
from Trooper_Player import Trooper_Player
from Trooper_Enemy import Trooper_Enemy

troopers = []

add = 0
for path in imgpath.normal_p_troops1:
    troopers.append(Trooper_Player((230, 130 + 50*add, 40, 40), 16, False, path))
    add += 1

add = 0
for path in imgpath.normal_p_troops2:
    troopers.append(Trooper_Player((280, 130 + 50 * add, 40, 40), 16, False, path))
    add += 1

# Enemy Troopers
troopers_e = [Trooper_Enemy(troop.rect, troop.head_name, troop.weapon_name) for troop in troopers]
troopers_e[0].box_col = troopers_e[0].pick_col

add = 0
for path in imgpath.blast_p_troops:
    troopers.append(Trooper_Player((330, 130 + 50*add, 40, 40), 16, False, path))
    add += 1

add = 0
for path in imgpath.saber_p_troops:
    troopers.append(Trooper_Player((380, 130 + 50*add, 40, 40), 32, True, path))
    add += 1

troopers[0].box_col = troopers[0].pick_col
