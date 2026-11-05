import random


class Monster:
    def __init__(self, name, attack, defence, hp):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.hp = hp

    def attack_target(self, target): # 공격 method
        damage = self.attack - target.defence
        target.hp = target.hp - damage
        if target.hp <= 0:
            target.hp = 0
def fight(monster1, monster2):
    initiative_monster1 = random.randint(1, 3)
    initiative_monster2 = random.randint(1, 3)

    if initiative_monster1 == initiative_monster2:
        result = "draw"
    elif initiative_monster1 == 1 and initiative_monster2 == 3:
        result = "monster1_win"
    elif initiative_monster1 == 2 and initiative_monster2 == 1:
        result = "monster1_win"
    elif initiative_monster1 == 3 and initiative_monster2 == 2:
        result = "monster1_win"
    else:
        result = "monster2_win"
    if result != "draw":
        if result == "monster1_win":
            while monster1.hp > 0 and monster2.hp > 0:
                monster1.attack_target(monster2)
                if monster2.hp > 0:
                    monster2.attack_target(monster1)
        else:
            while monster1.hp > 0 and monster2.hp > 0:
                monster2.attack_target(monster1)
                if monster1.hp > 0:
                    monster1.attack_target(monster2)
    if monster1.hp <=0:
        print(f"{monster1.name} 죽음")
    elif monster2.hp <=0:
        print(f"{monster2.name} 죽음")

oak_1 = Monster("oak", 8, 2, 80)
goblin_1 = Monster("goblin", 5, 6, 54)

fight(oak_1, goblin_1)
