# Write your solution here

def who_won(game_board: list):
    play1 = 0
    play2 = 0
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1:
                play1 += 1
            elif game_board[i][j] == 2:
                play2 += 1
    if play1 > play2:
        return 1
    elif play1 < play2:
        return 2
    else:
        return 0

if __name__ == "__main__":
    
    print(whowon())




