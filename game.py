from __future__ import annotations

import sys
from typing import Any

try:
    from player import Player  # type: ignore
except Exception:  # pragma: no cover
    Player = None  # noqa: N801

try:
    from monster import Mob, Mushroom, Slime  # type: ignore
except Exception:  # pragma: no cover
    Mob = None  # noqa: N801
    Mushroom = None
    Slime = None

try:
    from battle import BattleManager  # type: ignore
except Exception:  # pragma: no cover
    BattleManager = None  # noqa: N801


class Game:


    def __init__(self, player: Any, monster: Any, battle_manager: Any) -> None:
        self.player = player
        self.monster = monster
        self.battle_manager = battle_manager

    def show_menu(self) -> None:
        """Print the main menu.

        The menu follows the exact layout requested by the user:
        ``1. 공격하기`` – Attack the monster.
        ``2. 플레이어 정보 보기`` – Show player stats.
        ``3. 몬스터 정보 보기`` – Show monster stats.
        ``4. 종료`` – Exit the game.
        """
        print("\n=== 메뉴 ===")
        print("1. 공격하기")
        print("2. 플레이어 정보 보기")
        print("3. 몬스터 정보 보기")
        print("4. 종료")

    def start(self) -> None:
        """Run the interactive game loop.

        The loop continues until the monster's HP drops to ``0`` (or less) or
        the user selects the *exit* option.
        """
        while True:
            self.show_menu()
            choice = input("선택: ").strip()

            if choice == "1":
                # Delegate the actual combat to the battle manager.
                if self.battle_manager:
                    try:
                        self.battle_manager.player_attack(self.player, self.monster)
                    except Exception as exc:  # pragma: no cover
                        print(f"전투 중 오류 발생: {exc}")
                else:
                    # Fallback simple attack if no manager is provided.
                    try:
                        self.player.attack(self.monster)  # type: ignore[attr-defined]
                    except Exception as exc:  # pragma: no cover
                        print(f"공격 오류: {exc}")

                # Check monster health.
                if getattr(self.monster, "hp", 0) <= 0:
                    print("몬스터가 쓰러졌습니다! 게임 종료.")
                    break

            elif choice == "2":
                # Show player information.
                try:
                    self.player.show_info()  # type: ignore[attr-defined]
                except Exception as exc:  # pragma: no cover
                    print(f"플레이어 정보 조회 오류: {exc}")

            elif choice == "3":
                # Show monster information.
                try:
                    self.monster.show_info()  # type: ignore[attr-defined]
                except Exception as exc:  # pragma: no cover
                    print(f"몬스터 정보 조회 오류: {exc}")

            elif choice == "4":
                print("게임을 종료합니다.")
                break

            else:
                print("잘못된 입력입니다. 1~4 사이의 번호를 선택하세요.")


# ---------------------------------------------------------------------------
# When this file is executed directly, we provide a tiny demonstration that
# creates dummy objects if the dependent modules are not yet implemented.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Create minimal stand‑in objects when the real implementations are missing.
    if Player is None:
        class DummyPlayer:
            def __init__(self) -> None:
                self.name = "플레이어"
                self.hp = 100
                self.attack_power = 20

            def attack(self, target: Any) -> None:  # noqa: D401
                print(f"{self.name}이(가) {getattr(target, 'name', '몬스터')}에게 공격!")
                damage = self.attack_power
                target.hp = getattr(target, "hp", 0) - damage
                print(f"데미지 {damage}점, 남은 HP: {target.hp}")

            def show_info(self) -> None:
                print(f"플레이어: {self.name}, HP: {self.hp}, 공격력: {self.attack_power}")

        player_obj = DummyPlayer()
    else:
        player_obj = Player()

    if Slime is not None:
        monster_obj = Slime("슬라임", 50, 10, 5)
    elif Monster is not None:
        monster_obj = Monster("몬스터", 50, 10, 5)
    else:
        class DummyMonster:
            def __init__(self) -> None:
                self.name = "몬스터"
                self.hp = 50

            def show_info(self) -> None:
                print(f"몬스터: {self.name}, HP: {self.hp}")

        monster_obj = DummyMonster()

    if BattleManager is None:
        class DummyBattleManager:
            def player_attack(self, player: Any, monster: Any) -> None:
                player.attack(monster)
        battle_manager_obj = DummyBattleManager()
    else:
        battle_manager_obj = BattleManager()

    game = Game(player_obj, monster_obj, battle_manager_obj)
    game.start()
"