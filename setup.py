"""installation file of script labyrinth_game.py"""

from cx_Freeze import setup, Executable

# call of the function setup
setup(
    name = "Labyrinth game",
    version = "0.1",
    description = "Labyrinth game with Mac Gyver",
    executables = [Executable("labyrinth_game.py")],
)
