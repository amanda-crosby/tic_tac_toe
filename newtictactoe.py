def create_empty_board():

    board = [[None] * 3 for i in range(3)]
    return board
     #The inner list comprehension creates a list with 3 None elements, and the outer list comprehension creates 3 of those lists. 
     #This yields a 3x3 matrix where every element is initialized to None.

def draw(board):
    print
    print board[0][0] or "1", " | ", board[0][1] or "2", " | ", board[0][2] or "3"
    print "-------------"
    print board[1][0] or "4", " | ", board[1][1] or "5", " | ", board[1][2] or "6"
    print "-------------"
    print board[2][0] or "7", " | ", board[2][1] or "8", " | ", board[2][2] or "9"
    print

def make_move(action, board, player):

    num = action - 1
    #num = 6
    row = num / 3 #2
    col = num % 3 #0

    board[row][col] = player # X or O
    draw(board)

def full(board):
    for row in board:
        for element in row:
            if element == "X" or element == "O":
                pass
            else: 
                return False 
    return True

def winning(board):
        if board[0][0] == board[0][1] == board[0][2] != None:
                return board[0][0]
        elif board[1][0] == board[1][1] == board[1][2] != None:
                return board[1][0]
        elif board[2][0] == board[2][1] == board[2][2] != None:
                return board[2][0]
        elif board[0][0] == board[1][0] == board[2][0] != None:
                return board[0][0]
        elif board[0][1] == board[1][1] == board[2][1] != None:
                return board[0][1]
        elif board[0][2] == board[1][2] == board[2][2] != None:
                return board[0][2]
        elif board[0][0] == board[1][1] == board[2][2] != None:
                return board[0][0]
        elif board[0][2] == board[1][1] == board[2][0] != None:
                return board[0][2]
        else:
                return None

def main():
    
    board = create_empty_board()
    print
    print "Welcome to Tic Tac Toe! Player X will go first"
    draw(board)



    player_turn = 0

    while not full(board) and not winning(board):
        player_turn = player_turn + 1
        # 3
        player = "X" if player_turn % 2 else "O"  #will return X if player turn mod 2 is 1, and will return O if player turn mod 2 is 0 
        action = raw_input("Player {0}, which space would like to move? ".format(player))
        if action.isdigit():
            action = int(action)
            if action >0 and action <10:
                num = action - 1
                #num = 6
                row = num / 3 #2
                col = num % 3 #0

                if board[row][col] == "X" or board[row][col] == "O":
                    print
                    print "This position on the board is already taken. Please pick a different position."
                    print
                    player_turn = player_turn - 1
                else:
                    board[row][col] = player # X or O
                    draw(board)


            else:
                print
                print "This is an invalid move. Please pick a number 1-9."
                print
                player_turn = player_turn - 1
        else:
            print
            print "This is not a number. Please pick a number 1-9."
            print
            player_turn = player_turn - 1
        

    if winning(board):
        print "Congratulations, Player {0}! You won! Woohoo!".format(player)
        print
    else:
        print "The game is tied."
        print



main()





