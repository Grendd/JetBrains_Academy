inp = '         '
board = [list(inp[6:9]), list(inp[3:6]), list(inp[0:3])]
# Rows
top = ' '.join(board[2])
mid = ' '.join(board[1])
bot = ' '.join(board[0])
# Columns
left = ' '.join([top[0], mid[0], bot[0]])
mid_vertical = ' '.join([top[2], mid[2], bot[2]])
right = ' '.join([top[4], mid[4], bot[4]])

# Diagonals
diagonal_one = ' '.join([top[0], mid[2], bot[4]])
diagonal_two = ' '.join([top[4], mid[2], bot[0]])
last_cross = True
count = 0


def print_board():
    print('---------')
    print('| ' + top + ' |')
    print('| ' + mid + ' |')
    print('| ' + bot + ' |')
    print('---------')


def moving():
    global top, mid, bot, left, mid_vertical, right, diagonal_one, diagonal_two, last_cross, count
    coord = input('Enter coordinates:').split()
    if isinstance(int(coord[0]), str) or isinstance(int(coord[1]), str):
        print('You should enter numbers!')
        moving()
    elif int(coord[1]) > 3 or int(coord[0]) > 3:
        print('Coordinates should be from 1 to 3!')
        moving()
    elif board[int(coord[1]) - 1][int(coord[0]) - 1] == 'X' or board[int(coord[1]) - 1][int(coord[0]) - 1] == 'O':
        print('This cell is occupied! Choose another one!')
        moving()
    else:
        count = count + 1
        if last_cross is True:
            board[int(coord[1]) - 1][int(coord[0]) - 1] = 'X'
            last_cross = False
        elif last_cross is False:
            board[int(coord[1]) - 1][int(coord[0]) - 1] = 'O'
            last_cross = True
        top = ' '.join(board[2])
        mid = ' '.join(board[1])
        bot = ' '.join(board[0])
        left = ' '.join([top[0], mid[0], bot[0]])
        mid_vertical = ' '.join([top[2], mid[2], bot[2]])
        right = ' '.join([top[4], mid[4], bot[4]])
        diagonal_one = ' '.join([top[0], mid[2], bot[4]])
        diagonal_two = ' '.join([top[4], mid[2], bot[0]])
        if 'X X X' in (top, mid, bot) or 'X X X' in (left, mid_vertical, right) or 'X X X' in (diagonal_one, diagonal_two):
            print_board()
            print('X wins')
            return
        elif 'O O O' in (top, mid, bot) or 'O O O' in (left, mid_vertical, right) or 'O O O' in (diagonal_one, diagonal_two):
            print_board()
            print('O wins')
            return
        elif count == 9:
            print_board()
            print('Draw')
            return
        print_board()
        moving()


print_board()
moving()

