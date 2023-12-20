#Ends the game when False.
playing = True

#The tic tac toe grid that will be edited by the players.
grid = [["\t","\t","\t"],
        ["\t","\t","\t"],
        ["\t","\t","\t"]]

#Tuples used for checking input validity.
columns = ('a', 'b', 'c')
rows = (1, 2, 3)

#Returns the grid 'g'.
def printGrid(g):
    return f"{g[0][0]}|{g[0][1]}|{g[0][2]}  3"\
    "________________________"\
    f"{g[1][0]}|{g[1][1]}|{g[1][2]}  2"\
    "________________________"\
    f"{g[2][0]}|{g[2][1]}|{g[2][2]}  1"\
    "a\tb\tc"

#The player's turn
def playerTurn(p):
    
    global grid
    
    #Checks for the validity of the syntax of 'p'.
    #The syntax should be a letter ('a', 'b', 'c') followed by a number (1, 2, 3).
    #Ex: a1 b3 c2.
    if len(p) != 2 and p[0] not in columns and int(p[1]) not in rows:
        #Invalid syntax. The player's turn is repeated.
        playerTurn(p)
        
    #After the syntax is validated, the syntax is translated to list indexes.
    r = 3 - int(p[1])
    c = rows[columns.index(p[0])] - 1
    
    #Checks if the picked slot poisition is already taken.
    if len(grid[r][c]) == 2:
        #The position is already taken. The player's turn is repeated.
        playerTurn(p)
    else:
        pass
    

#The bot's turn.
def botTurn():
    pass

#Should the bot or the player start first?
def botOrPlayer(a):
    if a == True:
        #Keeps the game running until the condition is false
        #(Player wins, bot wins, or draw).
        while playing:
            botTurn()
            playerTurn()
    else:
        while playing:
            playerTurn()
            botTurn()