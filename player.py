from monster import Mob

class Player:
    def __init__(self, name, hp=100, attack_power=10):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, monster):
        damage = self.attack_power - monster.defense
        if damage < 1:
            damage = 1
        
        monster.hp -= damage
        if monster.hp < 0:
            monster.hp = 0

        print(f"{self.name}이(가) {monster.name}을(를) 공격했습니다!")
        print(f"{monster.name}에게 {damage}의 피해를 입혔습니다.")

    def info(self):
        print(f"--- {self.name} 정보 ---")
        print(f"체력(HP): {self.hp} | 공격력: {self.attack_power}")

    def show_info(self):
        self.info()


# Mob 클래스에 show_info 메서드를 추가하여 Mob을 상속받는 Mushroom 및 Slime 모두 show_info() 호출 시
# 각자의 info() 메서드가 실행되도록 동적 주입합니다.
Mob.show_info = lambda self: self.info()