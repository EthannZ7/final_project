'''
Five in a row!

Rule:
Two players and two types of stones, one is '#' and the other is '*'.
Take turns placing one stone on the board.
The first to make a line of 5 stones (straight line) wins.
The line can be horizontal, vertical, or diagonal.

Notice: When input coordinates, the number of row is first.
'''

'''Initialise a 5x5 board'''
def init_board():
    global board
    global player_1 
    global player_2

    board = [
        [' 1 2 3 4 5'],
        ['1','-','|','-','|','-','|','-','|','-'],
        ['2','-','|','-','|','-','|','-','|','-'],
        ['3','-','|','-','|','-','|','-','|','-'],
        ['4','-','|','-','|','-','|','-','|','-'],
        ['5','-','|','-','|','-','|','-','|','-']
    ]

    player_1 = input("Enter your name player_1('#'): ") # '#'
    player_2 = input('Enter your name player_2("*"): ') # '*'

'''Player 1 places the stone'''
def player1():
    player_1
    while True:
        crd_1 = list(input(f'{player_1}, enter the coordinates: '))
        if len(crd_1) != 3 or not crd_1[0].isdigit() or not crd_1[2].isdigit():
            print('Invalid coordinates!')
            continue
        else:
            x = int(crd_1[0])
            y = int(crd_1[2])
            if x not in range(6) or y not in range(6):
                print('Out of board!')
                continue
            else:
                if y == 2:
                    y += 1
                elif y == 3:
                    y += 2
                elif y == 4:
                    y += 3
                elif y == 5:
                    y += 4

                if board[x][y] != '-':
                    print('The coordinate is occupied!')
                    continue
                else:
                    board[x][y] = '#'
                    break
    
'''Player 2 places the stone'''
def player2():
    while True:
        crd_2 = list(input(f'{player_2}, enter the coordinates: '))
        if len(crd_2) != 3 or not crd_2[0].isdigit() or not crd_2[2].isdigit():
            print('Invalid coordinates!')
            continue
        else:
            x = int(crd_2[0])
        y = int(crd_2[2])
        if x not in range(6) or y not in range(6):
            print('Out of board!')
            continue
        else:
            if y == 2:
                y += 1
            elif y == 3:
                y += 2
            elif y == 4:
                y += 3
            elif y == 5:
                y += 4

            if board[x][y] != '-':
                print('The coordinate is occupied!')
                continue
            else:
                board[x][y] = '*'
                break
        
        
'''Check if there is a winner.'''
def judge():
    # horizantal
    i = 1
    count_player_1 = 0
    count_player_2 = 0
    outcome = ''
    while i <= len(board) - 1:
        count_player_1 = 0
        count_player_2 = 0
        for j in range(1, len(board[1]), 2):
            if board[i][j] == '#':
                count_player_1 += 1
            elif board[i][j] == '*':
                count_player_2 += 1
        if count_player_1 == 5:
            outcome = f'{player_1} wins!'
        elif count_player_2 == 5:
            outcome = f'{player_2} wins!'
        i += 1

    # diagonal
    i = 1
    j = 1
    count_player_1 = 0
    count_player_2 = 0
    while i <= len(board) - 1:
        if board[i][j] == '#':
            count_player_1 += 1
        elif board[i][j] == '*':
            count_player_2 += 1

        if count_player_1 == 5:
            outcome = f'{player_1} wins!'
            break
        elif count_player_2 == 5:
            outcome = f'{player_2} wins!'
            break
        i += 1
        j += 2

    i = 1
    j = 9
    count_player_1 = 0
    count_player_2 = 0
    while i <= len(board) - 1:
        if board[i][j] == '#':
            count_player_1 += 1
        elif board[i][j] == '*':
            count_player_2 += 1

        if count_player_1 == 5:
            outcome = f'{player_1} wins!'
            break
        elif count_player_2 == 5:
            outcome = f'{player_2} wins!'
            break
        i += 1
        j -= 2

    # vertical
    i = 1
    j = 1
    count_player_1 = 0
    count_player_2 = 0

    while j <= len(board[1]) - 1:
        i = 1
        count_player_1 = 0
        count_player_2 = 0
        while i <= 5:
            if board[i][j] == '#':
                count_player_1 += 1
            elif board[i][j] == '*':
                count_player_2 += 1
            i += 1
        if count_player_1 == 5:
            outcome = f'{player_1} wins!'
        elif count_player_2 == 5:
            outcome = f'{player_2} wins!'
        j += 2
    
    return outcome

    
'''check if it is a draw'''
def isdraw():
    count = 0
    for i in range(1, len(board)):
        for j in range(1, len(board[i]), 2):
            if board[i][j] == '-':
                count += 1
                # print(count)
    
    if count == 0:
        return True
    return False


'''Display the board'''
def display_board():
    
    i = 0
    
    while i < len(board):
         j =''.join(board[i])     
         print(j)
         i += 1    


def game():
    
    init_board()
    display_board()

    result = ''

    while True:
        
        player1()
        display_board()
        result = judge()
        is_draw = isdraw()
        if result == f'{player_1} wins!':
            break
        elif is_draw:
            result = 'The Gomoku game ended in a draw.'
            break

        player2()
        display_board()
        result = judge()
        is_draw = isdraw()
        if result == f'{player_2} wins!':
            break
        elif is_draw:
            result = 'The Gomoku game ended in a draw.'
            break

    print(result)
        
    
# Menu
print('-------------')
print('---1. Play---')
print('---2. Exit---')
print('-------------')


while True:
    try:
        choice = int(input('Enter your choice[1/2]:'))

        if choice == 1:
            game()
            break
        elif choice == 2:
            print('Goodbye!')
            break
        else:
            print('Invalid choice!')
    except ValueError:
        print("Invalid input.")



