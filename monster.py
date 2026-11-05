 # 몬스터 2마리 만들기
 
import random

class Oak: # 오크 클래스 선언
    def __init__(self): # 오크 공격, 방어, 체력 속성
        self.attack = 8
        self.defence = 2
        self.hp = 80

    def attack_target(self, target): # 공격 method
        damage = self.attack - target.defence
        target.hp = target.hp - damage
        if target.hp <= 0:
            target.hp = 0


class Goblin: # 고블린 클래스 선언
    def __init__(self): # 고블린 공격, 방어, 체력 속성
        self.attack = 5
        self.defence = 6
        self.hp = 54

    def attack_target(self, target): # 공격 method
        damage = self.attack - target.defence
        target.hp = target.hp - damage
        if target.hp <= 0:
            target.hp = 0


oak_1 = Oak()
goblin_1 = Goblin()

initiaive_oak_1 = random.randint(1, 3)
initiaive_goblin_1 = random.randint(1, 3)

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
        print(f"{monster1} 죽음")
    elif monster2.hp <=0:
        print(f"{monster2} 죽음")
        
fight(goblin_1, oak_1)
print(goblin_1.hp, oak_1.hp)

        