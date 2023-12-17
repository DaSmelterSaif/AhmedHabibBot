def twoPlayers():
    win = 0
    grid = [["\t","\t","\t"],
            ["\t","\t","\t"],
            ["\t","\t","\t"]]
    #while win == 0:
    print(f"{grid[0][0]}|{grid[0][1]}|{grid[0][2]}")
    print("________________________")
    print(f"{grid[1][0]}|{grid[1][1]}|{grid[1][2]}")
    print("________________________")
    print(f"{grid[2][0]}|{grid[2][1]}|{grid[2][2]}")

while True:
    player_count = int(input("--------Tic tac toe--------\n1 or 2 players?\n"))
    if player_count == 2:
        twoPlayers()