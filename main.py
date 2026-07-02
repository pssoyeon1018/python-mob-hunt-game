#!/usr/bin/env python
"""Entry point for the simple mob‑hunting game.

Creates a Player, a blue mushroom (BlueMushroom), a BattleManager, and starts the Game.
"""

# Ensure stdout can handle Unicode characters printed by monster module during import
import sys, io
if sys.stdout.encoding.lower() != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

from monster import Mushroom as BlueMushroom
from player import Player
from battle import BattleManager
from game import Game


def main() -> None:
    """Instantiate objects and launch the game loop."""
    # 이름을 반드시 넘겨 주어야 합니다.
    player = Player("플레이어")
    monster = BlueMushroom("파랑버섯", 100, 80, 50)
    battle_manager = BattleManager()
    game = Game(player, monster, battle_manager)
    game.start()


if __name__ == "__main__":
    main()
    