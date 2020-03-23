# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Bob")


# The game starts here.

label start:

    "I don't even know why I keep trying."

    "Everything is pointless."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Bob sad

    # These display lines of dialogue.

    b "What am I even doing here ?"

    # This ends the game.

    return
