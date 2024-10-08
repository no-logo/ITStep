from arithmetic import *
from chess import game
from algo import sorting

if __name__ == "__main__":
    print(math.add(5, 8))
    print(math.subtract(10, 5))
    print(math.division(2, 7))
    print(math.multiply(12, 6))

    print('squrares', generators.squares(10))
    print('rand', generators.rand(10))

    #game.game_loop()
    rand_list = generators.rand(20)
    print(rand_list)
    sorting.bublle_sort(rand_list)
    print(rand_list)

    rand_list = generators.rand(20)
    print(rand_list)
    print(sorting.min(rand_list,0,len(rand_list)))

    rand_list = generators.rand(20)
    print(rand_list)
    sorting.selection_sort(rand_list)
    print(rand_list)

    rand_list = generators.rand(20)
    print(rand_list)
    sorting.insertion_sort(rand_list)
    print(rand_list)

    # obczaić algorytmy sortowania https://visualgo.net/en/sorting