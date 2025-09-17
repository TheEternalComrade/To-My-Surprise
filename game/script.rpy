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

    show master serious at left

    "Finally, as the last rays of sun dissappear, she turns around and tilts her head towards the youth standing next to her."

    show jordan serious at right

    m "It's time"

    "Jordan holds out their hand. Into it, the woman places a small, black key specked with gold."

    m "When the time comes, strike swift and true. The spirits will guide you. Good luck."

    "A corner of the teen's mouth tilts up."

    jo "the skilled don't rely on luck."

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

    pause

    # there will be three trials. The trial of hubris, the trial of bravery, and the trial of justice
    # slow fade in to:

    scene bg bus stop
    "The youth stares so intensely at a compass, it's a wonder it hasn't started melting"
    "They groan"
    "{i}What's that now, 6 false alarms?{/i}"
    "If they didn't know better, they would have though the thing was broken. But the mentor {i}had{/i} warned that it could work unexpectedly."
    show compass
    "For whatever reason, the compass was currently pointing at the sidewalk in front of them."
    "{i}Strange{/i}"
    "They had barely stepped onto bath before-"
    scene collision
    #He dropped
    pause
    scene bg bus stop
    "Both Jordan and the jogger stagger background"
    e "You-?"
    e "Who just stands in the middle of sidewalk?"
    "Jordan's heart is racing. But not because of the collision"
    "The compass is glowing"
    "{i}Is it him?{/i}"
    "However, the compass isn't pointing at the young man, but at the card he'd dropped"#maybe he was supposed to be helping samira hand out fliers for a special promotion at the restaurant
    "Jordan picks it up. It's a flier for some soul food restaurant."
    jo "Where did you get this?"
    "The jogger snatches it away from them before they can get a good look at the address"
    e "What's it too you?"
    jo "Uh"
    "Jordan realizes \"I'm looking for the one destined to prevent looming evil\" probably wouldn't go over well."
    shows jordan serious # or contemplative
    "They quickly think up a lie"
    jo "I think I used to go to this place when I was younger, but I don't remember the address"



    # This ends the game.

    return