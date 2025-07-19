from random import randint
import asyncio
from configparser import ConfigParser
import os

# ConfigParser.
config = ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'tictactoe.ini')
config.read(config_path)

# Get all tictactoe settings.
try:
    timeout = config.getint("settings", "PlayerTimeout")
except:
    print("Error parsing config file.")

# Tuples used for checking input validity.
columns = ('a', 'b', 'c')
rows = (1, 2, 3)

async def startGame(playerName, bot, channel):
    # TODO - Randomize X and O for the player and the bot.

    # The tic tac toe grid that will be edited by the players.
    grid = [["","",""],
            ["","",""],
            ["","",""]]

    turn = randint(0, 1) # 0 - player, 1 - bot

    await channel.send(formattedGrid(grid))

    async def printWinner(winner):
        """Prints the winner of the game."""
        
        await channel.send(f"{winner} has won the game! The game has ended.")

    # Game loop.
    for turnCount in range(9):
        if turn == 0:
            await channel.send(f"Your turn, {playerName}.")
            ranOutOfTime = await playerTurn(grid, playerName, bot, channel)
            if gameWon(grid):
                await printWinner(playerName)
                return
            turn = 1
        else:
            await channel.send("My turn.")
            await botTurn(grid, channel)
            if gameWon(grid):
                await printWinner("The bot")
                return
            turn = 0

        if turnCount == 8:
            await channel.send("It's a draw! The game has ended.")
            return

def formattedGrid(g):
    """Formats the grid for display in Discord."""
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

def gameWon(grid):
    """Checks if the game is won by either player."""
    
    # Check rows
    for row in grid:
        if grid[row][0] == grid[row][1] == grid[row][2] and grid[row][0] != "":
            return True
        
    # Check columns
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != "":
            return True
        
    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != "":
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != "":
        return True
    
    return False

async def playerTurn(grid, playerName, bot, channel):
    # TODO - Check if the channel is the same as the one the game started in.
    def check(m):
        """Checks if the message sent is from the player who started the game."""
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
                
                # If the syntax is valid, it gets translated to list indices.
                r = 3 - int(playerInput[1])
                c = rows[columns.index(playerInput[0])] - 1

                # Checks if the spot is already taken.
                if grid[r][c].strip() == "":
                    # The player takes the spot.
                    grid[r][c] = "X"
                    await channel.send(formattedGrid(grid))
                    break # Breaks out of the while loop.
                else:
                    await channel.send("That spot is already taken.")

            # If no break statements are reached, the player is prompted to try again
            # and another "timeout" seconds are given.

        except asyncio.TimeoutError:
            await channel.send("You have taken too long to make a move. The game has ended.")
            return True  # Indicates that the player ran out of time.


def findBestMove(grid):
    """Finds the best move for the bot. UNIMPLEMENTED."""
    return grid

# The bot's turn.
async def botTurn(grid, channel):
    await channel.send(formattedGrid(findBestMove(grid)))
    await channel.send("Note: The bot's turn is not yet implemented.")

    # TODO - Implement the bot's turn using findBestMove.