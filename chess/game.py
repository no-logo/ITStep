
player = {'x' : 0, 'y' : 0}
game_play = True

def game_loop():
    while game_play:
        draw_board()
        read_user_input(input('Your turn: '))

def pleyer_move(coord, step):
    if player[coord] + step >= 0 and player[coord] + step < 8:
        player[coord] += step



def read_user_input(key):
    match key:
        case "w":
            pleyer_move('y', -1)
        case "s":
            pleyer_move('y', 1)
        case "a":
            pleyer_move('x', -1)
        case "d":
            pleyer_move('x', 1)
        case "exit":
            global game_play 
            game_play = False

def draw_board():
    for y in range(8):
        for x in range(8):
            if player['x'] == x and player['y'] == y:
                print('[X]', sep = '', end = '')
            else:
                print('[ ]', sep = '', end = '')
        print('\n', end = '')