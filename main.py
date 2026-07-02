

from monster import Mushroom as BlueMushroom
from player import Player
from battle import BattleManager
from game import Game


def main() -> None:
    """Instantiate objects and launch the game loop."""
    player = Player()
    monster = BlueMushroom("파랑버섯", 100, 80, 50)
    battle_manager = BattleManager()
    game = Game(player, monster, battle_manager)
    game.start()


if __name__ == "__main__":
    main()
