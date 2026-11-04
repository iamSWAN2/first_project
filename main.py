# 가위 바위 보 게임 미니 프로젝트

print("=" * 30)
print()
print("     가위 / 바위 / 보 게임")
print()
print("=" * 30)
print()
print()

import random

choices = ("가위", "바위", "보")

com_win = 0
player_win = 0
player_total = 0
while True:
    print()
    print("1. 가위 2. 바위 3. 보")
    print()
    com_choice = random.randint(1, 3)
    def choose(a):
        return int(a) - 1
    while True:
        player_chioce = int(input("** 번호를 선택하세요 : "))
        if player_chioce < 4:
            break
        else:
            print("1 ~ 3을 입력해주세요")
            print()
    print()
    if player_chioce == 1:
        if com_choice == 1:
            print("비겼습니다")
            continue
        if com_choice == 2:
            com_win += 1
            print(f"player: {choices[choose(player_chioce)]} vs com: {choices[choose(com_choice)]}")
            print()
            print("패배")
        if com_choice == 3:
            player_win += 1
            print(f"player: {choices[choose(player_chioce)]} vs com: {choices[choose(com_choice)]}")
            print()
            print("승리")
    if player_chioce == 2:
        if com_choice == 2:
            print("비겼습니다")
            continue
        if com_choice == 3:
            com_win += 1
            print(f"player: {choices[choose(player_chioce)]} vs com: {choices[choose(com_choice)]}")
            print()
            print("패배")
        if com_choice == 1:
            player_win += 1
            print(f"player: {choices[choose(player_chioce)]} vs com: {choices[choose(com_choice)]}")
            print()
            print("승리")
    if player_chioce == 3:
        if com_choice == 3:
            print("비겼습니다")
            continue
        if com_choice == 1:
            com_win += 1
            print(f"player: {choices[choose(player_chioce)]} vs com: {choices[choose(com_choice)]}")
            print()
            print("패배")
        if com_choice == 2:
            player_win += 1
            print(f"player: {choices[choose(player_chioce)]} vs com: {choices[choose(com_choice)]}")
            print()
            print("승리")
    print()
    print(f"현재 스코어 player {player_win} : {com_win} com")
    if com_win == 3 or player_win == 3:
        if com_win == 3:
            player_total = 0
        else:
            player_total += 1
            print()
            print(f"{player_total} 연승중")
        print()
        while True:
            player_try = input("다시 도전 (yes / no) : ")
            print()
            if player_try != "yes" and player_try != "no":
                print("yes 또는 no를 입력해주세요")
                print()
            else:
                break
        if player_try == "yes":
            player_win = 0
            com_win = 0
        elif player_try == "no":
            break
    elif player_win < 3:
        continue