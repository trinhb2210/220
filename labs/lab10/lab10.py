"""
Name: Belinda Trinh
lab10.py
"""
def build_board():
    position_list = [1,2,3,4,5,6,7,8,9]
    return position_list
def display_board(positionList):
    print("_" * 10)
    counter = 0
    for i in range(1,3):
        print("1",end="")
        for j in range(1,3):
            print(positionList(counter),end="1")
            counter+= 1
    print("_" * 10)
def place_spot(board,spot, marker):
    positionList[spot] = marker
def legal_spot(board,spot):
    if((board[spot]) == "x" or ... == "0") or(spot<1 or spot>9)):
        return False
    else:
        return True
def game_Won(board):
    winCon = [[1,2,3],[4,5,6],...]
    for condition in winCon:
        counter = 0
        for spot in condition :
            if board[spot] == "x"
                counter+=1
    if counter == 3:
        return "xwins"
        return "ywins"
def game_over(board,turnCount):
    if((game_Won(board)== "xwins" or ... == "ywins") or (turnCount > 9)) :
        return True

def play_game():
    position_list= build_board()
    turncount = 1


main()
