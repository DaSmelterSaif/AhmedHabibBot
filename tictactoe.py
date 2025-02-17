from random import randint

# Tuples used for checking input validity.
columns = ('a', 'b', 'c')
rows = (1, 2, 3)

def startGame(messagerName, bot):
    # Ends the game when False.
    playing = True

    playerName = messagerName

    # The tic tac toe grid that will be edited by the players.
    grid = [["","",""],
            ["","",""],
            ["","",""]]

    turn = randint(0, 1) # 0 - player, 1 - bot

    while playing:
        if turn == 0:
            playerTurn(grid, playerName, bot)
        else:
            botTurn(grid)


# TODO - Combine printGrid with formatGrid.
# Returns the grid 'g'.
def printGrid(g):
    return f"{g[0][0]}|{g[0][1]}|{g[0][2]}  3"\
    "________________________"\
    f"{g[1][0]}|{g[1][1]}|{g[1][2]}  2"\
    "________________________"\
    f"{g[2][0]}|{g[2][1]}|{g[2][2]}  1"\
    "a\tb\tc"

# The player's turn
async def playerTurn(grid, playerName, bot):
    # TODO - Check if the channel is the same as the one the game started in.
    def check(m):
        return m.author == playerName

    # TODO - Test the game so far.
    # TODO - Add a timeout action.
    # Checks for the validity of the syntax of 'playerInput'.
    # The syntax should be a letter ('a', 'b', 'c') followed by a number (1, 2, 3).
    # Ex: a1 b3 c2.
    playerInput = await bot.wait_for("message", check=check, timeout=120)
    while (len(playerInput) != 2 and
                playerInput[0] not in columns and
                int(playerInput[1]) not in rows):
        playerInput = await bot.wait_for("message", check=check, timeout=120)
        #Invalid syntax. The player's turn is repeated.
        
    # After the syntax is validated, the syntax is translated to list indexes.
    r = 3 - int(playerInput[1])
    c = rows[columns.index(playerInput[0])] - 1
    
    # Checks if the picked slot poisition is already taken.
    while grid[r][c] != "":
        playerInput = await bot.wait_for("message", check=check, timeout=120)
    

# The bot's turn.
def botTurn(grid):
    pass

# TODO - Fix the playing is not defined error.
# Should the bot or the player start first?
def botOrPlayer(a):
    if a == True:
        # Keeps the game running until the condition is false
        # (Player wins, bot wins, or draw).
        while playing:
            botTurn()
            playerTurn()
    else:
        while playing:
            playerTurn()
            botTurn()

def formatGrid(g):
    pass