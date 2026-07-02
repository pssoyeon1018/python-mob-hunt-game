class Mob:
    def __init__(self, name, hp, attack_power, defense):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.defense = defense

    def attack(self):
        print(f"[{self.name}]이(가) 공격스킬을 출력했습니다.")
        print(f"{self.attack_power}의 데미지로 공격했습니다.")

    def info(self):
        print(f'이름: {self.name}')
        print(f'hp: {self.hp}')
        print(f'공격력: {self.attack_power}')
        print(f'방어력: {self.defense}')

class Mushroom(Mob):
    def __init__(self, name, hp, attack_power, defense):
        super().__init__(name, hp, attack_power, defense)

    def run(self):
        print(f"{self.name}(이)가 달리기 시작했습니다.")

    def jump(self):
        print(f"{self.name}(이)가 점프합니다.")


class Slime(Mob):
    def __init__(self, name, hp, attack_power, defense):
        super().__init__(name, hp, attack_power, defense)
        self.count = 1

    def split(self):
        self.count *= 2
        print(f"{self.name}이 분열했습니다!")

    def info(self):
        super().info()
        print(f"현재 슬라임의 개수  {self.count}마리")

# ==========================================
# 🎮 시뮬레이션 플레이!
# ==========================================
# bluemushroom = Mushroom("파랑버섯", 100, 80, 50)
# slime1 = Slime('슬라임1번', 30, 40, 20)
# bluemushroom.attack()
# bluemushroom.mob_info()
# slime1.split()
# slime1.slime_info()

mob1 = Mushroom("빨간버섯",100,90,80)
mob1.run()
mob1.jump()
mob1.info()

mob3 = Mushroom("파랑버섯",100,80,90)
mob3.run()
mob3.jump()
mob3.info()


mob2 = Slime("빨간슬라임",100,70,50)
mob2.split()
mob2.split()
mob2.info()


mob4 = Slime("파랑슬라임",100,80,50)
mob4.split()
mob4.split()
mob4.info()