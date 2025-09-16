# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jo = Character("Jordan")
define s = Character("Samira")
define je = Character("Jeante")
define e  = Character("Ernesto")
define m = Character("Master")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg dusk

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show master serious at left

    # These display lines of dialogue.

    "A middle aged woman glares at the sky. There's an almost imperceptible bead of sweat on her brow."
    "She's standing there motionlessly, waiting and waiting."

    scene bg night

    show master serious at leftG

    "Finally, as the last rays of sun dissappear, she turns around and tilts her head towards the youth standing next to her."

    show jordan serious at right

    m "It's time"

    "Jordan holds out their hand. Into it, the woman places a small, black key specked with gold."

    m "When the time comes, strike swift and true. The spirits will guide you. Good luck."

    "A corner of the teen's mouth tilts up."

    jo "Don't you say that the skilled don't rely on luck."

    "For just a moment, the master allows herself to smile back. She's trained them well."

    m "Open the gate."

    "Jordan closes their eyes, holds the key out as if to insert it, and turns."#this might be a drawing
    "Nothing happens." 
    "The two wait a moment. Then another. Jordan twists the key again, more forcefully this time."
    "Still nothing."

    show master nervous at left

    "The woman grows paler and paler."

    m "It can't be"

    show jordan nervous at right

    "Jordan's cool composure gives way to the beginnings of panic"

    jo "Why...can't I open the gates?"

    "For a few minutes, the master just glares at the night sky."
    "Finally, the woman inhales deeply"

    m "It seems"

    m "You are not the savior the prophecy speaks of."

    scene bg revelation

    # there will be three trials. The trial of hubris, the trial of bravery, and the trial of justice
    # slow fade in to:

    scene bg bus stop
    "The youth stares so intensely at a compass, it's a wonder is had started melting"
    "They groan"
    "What's that now, 6 false alarms?"


    # This ends the game.

    return