def game_logic(game_board):
    if game_board == win_board:
        clear_s()
        print('Победа')
        return
    else:
        clear_s()
        print_board(game_board)
        for x in range(len(game_board)):
            for y in range(len(game_board[x])):
                if game_board[x][y] == empty_cell:
                    x_empty = x
                    y_empty = y
                    break
    move = input('Куда двигаемся? W A S D: \n').lower()
    if move in ('w', 'a', 's', 'd'):
        movement(move, x_empty, y_empty)
    else:
        text('Нет такого направления')
        game_logic(game_board)

def movement(move, x_empty, y_empty):
    match move:
        case 'w':
            if x_empty - 1 >= 0:
                game_board[x_empty - 1][y_empty], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty - 1][y_empty]
                game_logic(game_board)
            else:
                text("Туда незя!")
                game_logic(game_board)
        case 'a':
            if y_empty - 1 >= 0:
                game_board[x_empty][y_empty - 1], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty][y_empty - 1]
                game_logic(game_board)
            else:
                text("Туда незя!")
                game_logic(game_board)
        case 's':
            if x_empty + 1 <= 3:
                game_board[x_empty + 1][y_empty], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty + 1][y_empty]
                game_logic(game_board)
            else:
                text("Туда незя!")
                game_logic(game_board)
        case 'd':
            if y_empty + 1 <= 3:
                game_board[x_empty][y_empty + 1], game_board[x_empty][y_empty] = game_board[x_empty][y_empty], game_board[x_empty][y_empty + 1]
                game_logic(game_board)
            else:
                text("Туда незя!")
                game_logic(game_board)