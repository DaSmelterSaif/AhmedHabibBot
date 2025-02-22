from random import randint

import asyncio

# Tuples used for checking input validity.
columns = ('a', 'b', 'c')
rows = (1, 2, 3)

async def startGame(messagerName, bot, channel):
    # Ends the game when False.
    playing = True

    playerName = messagerName

    # TODO - Randomize X and O for the player and the bot.

    # The tic tac toe grid that will be edited by the players.
    grid = [["","",""],
            ["","",""],
            ["","",""]]

    turn = randint(0, 1) # 0 - player, 1 - bot

    # Game loop.
    while playing:
        # TODO - Add a function to check for a win in the grid.

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

def formattedGrid(g):
    g_copy = g.copy()
    # Adds spaces " " to empty spots on the grid.
    for row in range(len(g_copy)):
        for col in range(len(g_copy[row])):
            if g_copy[row][col] == "":
                g_copy[row][col] = " "

    return f"```3 {g_copy[0][0]}|{g_copy[0][1]}|{g_copy[0][2]}\n"\
    " __.__.__\n"\
    f"2 {g_copy[1][0]}|{g_copy[1][1]}|{g_copy[1][2]}\n"\
    " __.__.__\n"\
    f"1 {g_copy[2][0]}|{g_copy[2][1]}|{g_copy[2][2]}\n"\
    "  a b c```"

async def playerTurn(grid, playerName, bot, channel, playing):
    timeout = 10

    # TODO - Check if the channel is the same as the one the game started in.
    def check(m):
        return m.author == playerName
    
    # Checks for the validity of the syntax of 'playerInput'.
    # The syntax should be a letter ('a', 'b', 'c') followed by a number (1, 2, 3).
    # Ex: a1 b3 c2.
    while True:
        try:
            playerInput = await bot.wait_for("message", check=check, timeout=timeout)
            playerInput = playerInput.content.strip().lower()

            # Checks if the syntax is valid.
            if (len(playerInput) == 2 and
                    playerInput[0] in columns and
                    int(playerInput[1]) in rows):
                
                # If the syntax is valid, it gets translated to list indexes.
                r = 3 - int(playerInput[1])
                c = rows[columns.index(playerInput[0])] - 1

                # Checks if the spot is already taken.
                if grid[r][c].strip() == "":
                    # The player takes the spot.
                    grid[r][c] = "X"
                    await channel.send(formattedGrid(grid))
                    break
                else:
                    await channel.send("That spot is already taken.")

            # If no break statements are reached, the player is prompted to try again
            # and another "timeout" seconds are given.

        except asyncio.TimeoutError:
            await channel.send("You have taken too long to make a move. The game has ended.")
            playing = False
            break

    return playing

def findBestMove(grid):
    return grid

# The bot's turn.
async def botTurn(grid, channel, playing):
    await channel.send(formattedGrid(findBestMove(grid)))
    await channel.send("Note: The bot's turn is not yet implemented.")

    # TODO - Implement the bot's turn using findBestMove.

    return playing