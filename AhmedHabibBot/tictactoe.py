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
    #while win == 0:
    for i in ["X","O"]:
        printGrid(grid)
        user_input = input(f"Player ({i}) turn. Enter the coordinates of {i} (ex: a1):\n")
        if user_input[0] in columns:
            r = 3 - int(user_input[1])
            c = columns_num[columns.index(user_input[0])]
        grid[r][c] = f"{i}\t"
        for j in range(3):
            if grid[j][0] == grid[j][1] == grid[j][2] == f"{i}\t":
                pass
        for j in range(3):
            if grid[0][j] == grid[1][j] == grid[2][j] == f"{i}\t":
                pass
    printGrid(grid)

while True:
    player_count = int(input("--------Tic tac toe--------\n1 or 2 players?\n"))
    if player_count == 2:
        twoPlayers()