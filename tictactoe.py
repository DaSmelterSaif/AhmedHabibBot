from random import randint

import asyncio

# TODO - Figure out how to integrate this with the responses.py file.

# Tuples used for checking input validity.
columns = ('a', 'b', 'c')
rows = (1, 2, 3)

async def startGame(messagerName, bot, channel):
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
            await channel.send(f"Your turn, {playerName}.")
            playing = await playerTurn(grid, playerName, bot, channel, playing)
            turn = 1
        else:
            await channel.send("My turn.")
            playing = await botTurn(grid, channel, playing)
            turn = 0
    else:
        await channel.send("The game has ended.")
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
async def playerTurn(grid, playerName, bot, channel, playing):
    # How long before the game ends if the player doesn't make a move.
    timeout = 10

    # TODO - Check if the channel is the same as the one the game started in.
    def check(m):
        return m.author == playerName

    # TODO - Test the game so far.
    # Checks for the validity of the syntax of 'playerInput'.
    # The syntax should be a letter ('a', 'b', 'c') followed by a number (1, 2, 3).
    # Ex: a1 b3 c2.
    while True:
        try:
            playerInput = await bot.wait_for("message", check=check, timeout=timeout)
            playerInput = playerInput.content.strip().lower()
            if (len(playerInput) == 2 and
                    playerInput[0] in columns and
                    int(playerInput[1]) in rows):
                # After the syntax is validated, the syntax is translated to list indexes.
                r = 3 - int(playerInput[1])
                c = rows[columns.index(playerInput[0])] - 1

                # Checks if the spot is already taken.
                if grid[r][c] == "":
                    grid[r][c] = "X"
                    break
                else:
                    await channel.send("That spot is already taken.")

        except asyncio.TimeoutError:
            await channel.send("You have taken too long to make a move. The game has ended.")
            playing = False
            break
    return playing
    

# The bot's turn.
async def botTurn(grid, channel, playing):
    await channel.send(printGrid(grid))
    await channel.send("Note: The bot's turn is not yet implemented.")
    return playing

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