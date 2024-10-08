from arithmetic import *
from chess import game

if __name__ == "__main__":
    print(math.add(5, 8))
    print(math.subtract(10, 5))
    print(math.division(2, 7))
    print(math.multiply(12, 6))

    print('squrares', generators.squares(10))
    print('rand', generators.rand(10))

    game.game_loop()