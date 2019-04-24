"""installation file of script maze_game.py"""

from cx_Freeze import setup, Executable

# call of the function setup
setup(
    name = "Maze game",
    version = "0.1",
    description = "Maze game with Mac Gyver",
    executables = [Executable("maze_game.py")],
)
