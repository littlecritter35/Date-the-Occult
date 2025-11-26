# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define sG = Character(name="Sebastian") #Sebastian Giles
define dH = Character(name="Darian") #Darian Hawthorne
define dG = Character(name="Dean") #Dean Gustin
define rD = Character(name="Reggie") #Reggie Draconia
define rV = Character(name="Roman") #Roman Voltaire
define wF = Character(name="Will") #Will Frederickson
define aS = Character(name="Aidan") #Aidan Swallow
define dL = Character(name="Daisuke") #Daisuke Li
define m = Character(name="Mysterious Voice") #To be used whenever the character isn't known

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
