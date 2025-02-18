from random import randint

import asyncio

# TODO - Figure out how to integrate this with the responses.py file.

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
            turn = 1
        else:
            botTurn(grid, bot)
            turn = 0
    else:
        return


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
    # How long before the game ends if the player doesn't make a move.
    timeout = 120

    # TODO - Check if the channel is the same as the one the game started in.
    def check(m):
        return m.author == playerName

    # TODO - Test the game so far.
    # Checks for the validity of the syntax of 'playerInput'.
    # The syntax should be a letter ('a', 'b', 'c') followed by a number (1, 2, 3).
    # Ex: a1 b3 c2.
    try:
        playerInput = await bot.wait_for("message", check=check, timeout=timeout)
        while (len(playerInput) != 2 and
                playerInput[0] not in columns and
                int(playerInput[1]) not in rows):
            playerInput = await bot.wait_for("message", check=check, timeout=timeout)
            # After the syntax is validated, the syntax is translated to list indexes.
            r = 3 - int(playerInput[1])
            c = rows[columns.index(playerInput[0])] - 1

            # Repeats the loop if the slot is already taken.
            if grid[r][c] != "":
                continue
            else:
                grid[r][c] = "X"

    except asyncio.TimeoutError:
        print("Tic-tac-toe timeout.")
        await bot.send("You have taken too long to make a move. The game has ended.")
        playing = False
    

# The bot's turn.
async def botTurn(grid, bot):
    await bot.send(printGrid(grid))
    await bot.send("Note: The bot's turn is not yet implemented.")

# TODO - Fix the playing is not defined error.
# Should the bot or the player start first?

# def botOrPlayer(a):
#     if a == True:
#         # Keeps the game running until the condition is false
#         # (Player wins, bot wins, or draw).
#         while playing:
#             botTurn()
#             playerTurn()
#     else:
#         while playing:
#             playerTurn()
#             botTurn()

# def formatGrid(g):
#     pass