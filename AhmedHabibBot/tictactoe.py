import time

def printGrid(g):
    print(f"{g[0][0]}|{g[0][1]}|{g[0][2]}  3")
    print("________________________")
    print(f"{g[1][0]}|{g[1][1]}|{g[1][2]}  2")
    print("________________________")
    print(f"{g[2][0]}|{g[2][1]}|{g[2][2]}  1")
    print("a\tb\tc")

def twoPlayers():
    win = 0
    grid = [["\t","\t","\t"],
            ["\t","\t","\t"],
            ["\t","\t","\t"]]
    columns = ("a","b","c")
    columns_num = (0, 1, 2)
    p1p2 = lambda l: 1 if l =="X" else 2
    
    while win == 0:
        
        for i in ["X","O"]:
            printGrid(grid)
            
            #Checks if the inputted value is valid
            while True:
                user_input = input(f"Player {p1p2(i)} ({i}) turn. Enter the coordinates of {i} (ex: a1):\n")
                if len(user_input) != 2 or user_input[0] not in columns or int(user_input[1]) - 1 not in columns_num:
                    print(f"\'{user_input}\' is not valid!")
                    continue
                r = 3 - int(user_input[1])
                c = columns_num[columns.index(user_input[0])]
                if len(grid[r][c]) == 2:
                    print(f"{user_input} is already taken!")
                    continue
                else:
                    break
                
            grid[r][c] = f"{i}\t"
            
            #Checks if the player "i" won:

            #Checks rows
            for j in range(3):
                if grid[j][0] == grid[j][1] == grid[j][2] == f"{i}\t":
                    win = p1p2(i)
                    break
            else:
                #Checks columns
                for j in range(3):
                    if grid[0][j] == grid[1][j] == grid[2][j] == f"{i}\t":
                        win = p1p2(i)
                        break
                else:
                    #Checks diagonals
                    if grid[0][0] == grid[1][1] == grid[2][2] == f"{i}\t":
                        win = p1p2(i)
                    elif grid[0][2] == grid[1][1] == grid[2][0] == f"{i}\t":
                        win = p1p2(i)
            #Checks for draw
            flat_grid = [num for sublist in grid for num in sublist]
            if flat_grid.count("X") + flat_grid.count("O") == 18:
                break
            
    printGrid(grid)
    time.sleep(1)
    print(f"...\n..\nPlayer {p1p2(i)} wins!\n..\n...") if win != 0 else print("Draw!")
    time.sleep(2)

while True:
    player_count = int(input("--------Tic tac toe--------\n1 or 2 players?\n"))
    if player_count == 2:
        twoPlayers()