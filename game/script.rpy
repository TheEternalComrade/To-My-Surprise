# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jo = Character("Jordan", color="#d87210")
define s = Character("Samira", color="#780606")
define je = Character("Jeante", color="#bf77f6")
define m = Character("Mrs.Huynh", color="#000435")
define e = Character("Ernesto", color="#d5c58a")


# The game starts here.

label start:

    scene bg park night
    show master serious


    "A middle aged woman stares at her watch intensely. There's an almost imperceptible bead of sweat on her brow."
    "She's standing there motionlessly, waiting and waiting."

    show master serious 

    "Finally, as the clock hits midnight, she turns around and tilts her head towards the youth standing next to her."
    show master serious at left
    show jordan serious at right

    "Jordan holds out their hand. In it, there is a small, dark key specked with gold."
    m "Good luck."

    show jordan smile

    "A corner of the teen's mouth tilts up."
    jo "I'll be back soon."

    show jordan smile at right
    show master smile at left

    "For just a moment, the master allows herself to smile back. She's trained them well."

    show master serious at left
    show jordan serious

    "Jordan holds the key out as if to insert it, and turns."
    "Nothing happens." 
    "The two wait a moment. Then another. Jordan twists the key again, more forcefully this time."
    "Still nothing."

    show jordan nervous at right
    show master nervous at left

    "The woman grows paler and paler."
    m "Damn it"

    show jordan nervous at right

    "Jordan's cool composure gives way to the beginnings of panic"

    jo "Why...isn't it working?" 
    "For a few minutes, the master just glares at the ground."
    "Finally, the woman inhales deeply"
    m "It seems"
    m "You are not the savior the prophecy speaks of."

    scene bg revelation
    pause

    # slow fade in to:

    #Merry meet

    scene bg black
    scene busy hall
    show Samira angry at right
    show Jeante smiling at left
    s  "What the hell was that test? I swear she didn't cover half of that shit in class"

    show jeante bashful at left

    je "Eh, it wasn't that bad."

    show jordan indignant at left

    "Samira flicks his letterman jacket."
    s "Ok, nerd. We can always count on you to fuck up the curve."
    je "Hey, you keep talking like that and I eat all the jerk chicken!"
    
    show samira thoughtful at right

    "Samira rolls her eyes."
    s "Fineeeeeee"
    "They head over to their \"VIP Senior Table\"."

    scene bg VIPST
    "Jeante lays out the spread of food he had brought for them: rice and peas, jerk chicken, and even some fried plantain!"
















    # This ends the game.

    return