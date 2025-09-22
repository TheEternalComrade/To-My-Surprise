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

    scene bg vipst
    
    "Jeante lays out the spread of food he had brought for them."

    #maybe a drawing of this if I have time
    "Rice and peas, jerk chicken, and even some fried plantain!"

    show samira devious
    show jeante smile

    "Samira scoops up a generous amount of each."

    show jeante indignant

    "Hey! Save some for me"

    show samira happy

    s "Your parents may be assholes, but they sure can cook!"

    show jeante nervous

    je "Yeah"

    show jeante happy

    "However, before she can get more than a few spoonfuls-"
    "???" "Hey, can we talk? It\'s really important"

    show samira unsure

    "Samira reluctantly looks up at the person who\'d dared to interrupt their feast"
    "It was another senior that Samira didn\'t know that well. Jordan something? She vaguely remembered thinking in passing that they were cute but not much else"

    show jeante nervous

    "She looks at Jeante"
    "He just shrugs"

    # yes or no
    # no makes them slightly annoyed at you and they sit down anyway or maybe they crash out at the rejection and they get kicked out fo school. that would be funny+++++
    #yes is the good girl option
    
    show samira unbothered

    s "Aight, pull up a seat I guess"

    scene bg vipst3

    "She continues eating her food"

    show jo serious

    jo "I might as well get to the point"
    "They pull out a key crafte in a beautiful star motif"

    show samira suprised

    "Woah!"
    "That's a helluva key!"
    "The offer it up to Samira."

    show samira confused

    "Thanks?"
    "Gingerly, she reaches out to grab it"
    "Suddenly, she's transported...somewhere else."

    scene bg treasure

    "Where the food was just a moment before, she saw an intricate chest."
    "It felt familiar and strange at the same time."
    "For some reason she felt compelled to reach out for it."

    scene vipst3
    "But instead of the chest, there was her plate of food."
    "She drops it like it's made of lava."
    
    show samira shocked

    s "What the fuck was that?"
    
    show samira sus
    show jo suprised #or in awe

    "Jordan stares at her in disbelief"

    scene proclamation

    "You're going to save this realm"

    show bg ph#An explanation, disbelief, and some magical feats later

    show jeante nervous

    je "This is so cooked. What if you get attacked or something?"

    show samira nervous

    s "I mean, Jordan seems pretty strong.”
    "Their shirt is baggy, but it doesn\’t hide the impressive muscle beneath"
    "Plus they have those weapons"
    "They could probably protect me?"

    show jordan annoyed
    "Of course I'll protect you."

    show Jeante nervous
    je "But you still have to go to some other realm!"
    show Samira resigned
    s "I'd rather not do this, but I also don't really want to see what happens if I do nothing"
    s "I must've been chosen for a reason."



    #choice?



    # This ends the game.

    return