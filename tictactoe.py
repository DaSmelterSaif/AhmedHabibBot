from random import randint
import asyncio
from configparser import ConfigParser
import os
import copy
from discord import User, Message, Client

# ConfigParser.
config: ConfigParser = ConfigParser()
config_path: str = os.path.join(os.path.dirname(__file__), 'tictactoe.ini')
config.read(config_path)

# Get all tictactoe settings.
try:
    timeout = config.getint("settings", "PlayerTimeout")
except:
    print("Error parsing config file.")

# Tuples used for checking input validity.
columns: tuple = ('a', 'b', 'c')
rows: tuple = (1, 2, 3)

def gridFull(grid: list[list[str]])-> bool:
    """Checks if the grid is full."""
    for row in range(3):
        for col in range(3):
            if grid[row][col] == "":
                return False
    return True

async def startGame(playerUser: User, bot: Client, channel)-> None:
    # TODO - Randomize X and O for the player and the bot.

    global playerLetter, botLetter

    # The tic tac toe grid that will be edited by the players.
    grid = [["","",""],
            ["","",""],
            ["","",""]]

    turn = randint(0, 1) # 0 - player, 1 - bot

    # Player - Bot
    # X or O - X or O
    (playerLetter := "X") if randint(0, 1) == 0 else (playerLetter := "O") # 0 - X, 1 - O
    (botLetter := "X") if playerLetter == "O" else (botLetter := "O")

    await channel.send(f"You are playing with {playerLetter}, and I am playing with {botLetter}.")

    await channel.send(formattedGrid(grid))

    async def printWinner(winner: str)-> None:
        """Prints the winner of the game."""
        
        await channel.send(f"{winner} has won the game! The game has ended.")

    # Game loop.
    while not gridFull(grid):
        if turn == 0:
            await channel.send(f"Your turn, {playerUser}.")
            ranOutOfTime = await playerTurn(grid, playerUser, bot, channel)
            if ranOutOfTime:
                return
            if gameWon(grid):
                await printWinner(playerUser)
                return
            turn = 1
        else:
            await channel.send("My turn.")
            await botTurn(grid, channel)
            if gameWon(grid):
                await printWinner("The bot")
                return
            turn = 0
    else:
        await channel.send("It's a draw! The game has ended.")
        return

def formattedGrid(g: list[list[str]])-> str:
    """Formats the grid for display in Discord."""
    g_copy = copy.deepcopy(g)
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

def gameWon(grid: list[list[str]])-> bool:
    """Checks if the game is won by either player."""
    
    # Check rows
    for row in range(3):
        if (grid[row][0] == grid[row][1] == grid[row][2]) and grid[row][0] != "":
            return True
        
    # Check columns
    for col in range(3):
        if (grid[0][col] == grid[1][col] == grid[2][col]) and grid[0][col] != "":
            print(2) # Debugging line
            return True
        
    # Check diagonals
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != "":
        print(3)  # Debugging line
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != "":
        print(4)  # Debugging line
        return True
    
    return False

async def playerTurn(grid: list[list[str]], PlayerUser: User, bot: Client, channel)-> bool:
    def check(m)-> bool:
        """Checks if the message sent is from the player who started the game."""
        return m.author == PlayerUser and m.channel == channel
    
    def playerInputValid(playerInput: str)-> bool:
        """Checks if the input is valid."""
        if len(playerInput) != 2 or playerInput[0] not in columns or int(playerInput[1]) not in rows:
            return False
        
        return True
    
    def playerInputToGridIndex(playerInput):
        """Converts the player input to grid index."""
        r = 3 - int(playerInput[1])  # Converts row to index (1 -> 2, 2 -> 1, 3 -> 0)
        c = rows[columns.index(playerInput[0])] - 1 # Converts column to index (a -> 0, b -> 1, c -> 2)
        return r, c

    def spotTaken(grid, row, col):
        if grid[row][col].strip() == "":
            # The player takes the spot.
            return False
        return True
    
    # Player's turn repeats until the player inputs a valid input or times out.
    while True:
        try:
            playerInput = await bot.wait_for("message", timeout=timeout, check=check)
            playerInput = playerInput.content.strip().lower()

            if playerInputValid(playerInput):
                row, col = playerInputToGridIndex(playerInput)

                if not spotTaken(grid, row, col):
                    grid[row][col] = playerLetter # The player takes the spot.
                    await channel.send(formattedGrid(grid))
                    return False # False indicates that the game continues.
                else:
                    await channel.send("That spot is already taken. Please choose another spot.")

            else:
                await channel.send("Invalid input. Please write a letter (a, b, c)" +
                                    "followed by a number (1, 2, 3). Ex: a1, b2, c3.")

        except asyncio.TimeoutError:
            await channel.send("You have taken too long to make a move. The game has ended.")
            return True # True indicates that the player ran out of time.

    # Checks for the validity of the syntax of 'playerInput'.
    # The syntax should be a letter ('a', 'b', 'c') followed by a number (1, 2, 3).
    # Ex: a1 b3 c2.


def findBestMove(grid):
    """Finds the best move for the bot. UNIMPLEMENTED."""
    return None, None # Returns a tuple of (row, column) for the best move.

# The bot's turn.
async def botTurn(grid, channel):
    bestRow, bestCol = findBestMove(grid)
    try:
        grid[bestRow][bestCol] = botLetter # The bot takes the spot.
    except:
        exitOuterLoop = False
        for row in range(3):
            for col in range(3):
                if grid[row][col] == "":
                    grid[row][col] = botLetter
                    exitOuterLoop = True
                    break
            if exitOuterLoop:
                break

        await channel.send(formattedGrid(grid))
        await channel.send("Note: The bot's turn is not yet implemented properly.")

    # TODO - Implement the bot's turn using findBestMove.