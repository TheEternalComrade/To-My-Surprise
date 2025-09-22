# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jo = Character("Jordan", color="#d87210", image="jordan")
define s = Character("Samira", color="#780606")
define je = Character("Jeante", color="#bf77f6")
define m = Character("Mrs.Huynh", color="#000435")
define e = Character("Ernesto", color="#d5c58a")

image side jordan happy = "test.jpg"

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
    "They pull out a key crafted in a beautiful star motif"

    show samira suprised

    s "Woah!"
    s "That's a helluva key!"
    "They offer it up to Samira."

    show samira confused

    s "Thanks?"
    "Gingerly, she reaches out to grab it"
    "Suddenly, she's transported...somewhere else."

    scene bg treasure

    "Where the food was just a moment before, she sees an intricate chest."
    "It felt familiar and strange at the same time."
    "For some reason, she felt compelled to reach out for it."

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

    scene bg ph
    pause
    #An explanation, disbelief, and some magical feats later

    show bg vipst3
    show jeante nervous

    je "This is so cooked. What if you get attacked or something?"

    show samira nervous

    s "I mean, Jordan seems pretty strong."
    s "Their shirt is baggy, but it doesn\'t hide the impressive muscle beneath"
    s "Plus they have those weapons"
    s "They could probably protect me?"

    show jordan annoyed

    jo "Of course I'll protect you."

    show jeante nervous

    je "But you still have to go to some other realm!"

    show samira resigned

    s "I'd rather not do this, but I also don't really want to see what happens if I do nothing"
    s "I must've been chosen because I'll succeed."
    s "I'll be fine!"

    show jeante nervous

    je "I guess..."
    s "Now come on, let\'s finish this food before lunch is over"
    je "Bruh. How do you still have an appetite?"
    "Jordan stands up  to leave"
    s "You too Jordan!"
    "Samira had noticed them eyeing the spread"

    show jordan suprised

    jo "..."

    show jordan serious 

    jo "I appreciate sentiment, but I have to leave."
    
    show samira unhappy

    s "..."

    show jeante unhappy

    je "..."

    show jordan nervous

    jo "Maybe next time?"

    #"With that, they take their leave."
    #choice?

    scene bg black
    scene park dusk
    show Jeante nervous

    je "{i}This{/i} is it?"
    "Mrs. Huynh shoots a glare at him."
    je "Sorry, it's just…so normal."

    show jordan smile 

    je "Anyways"
    je "I brought some snacks! Y\’all should probably eat something before you go"
    
    show samira excited

    show master smile 
    
    m "How thoughtful!"

    show jordan thoughtful

    jo "We won't feel hunger in the dark realm"

    show jeante sus
    show samira sus

    "..."
    
    show jordan nervous

    jo "I suppose it wouldn't hurt"
    s "YEAA!"

    scene bg picnic
    pause
    #fade

    scene bg park night

    "Jeante suddenly has the presence of mind to check the time"

    show jeante surprised

    "It's half past 10!"

    show jeante unhappy

    "He groans"

    je "My parents are gonna kill me"

    show jeante nervous at right
    show samira wince at left

    s "Oof, curfew"

    show jo confused
    
    jo "Why don\'t you stay until midnight?"

    je "My parents are really strict"
    je "They\'re probably already planning to jump me when I get home"

    show samira thoughtful at left
    s "On the other hand..."
    s "It would really mean a lot if you were there to send me off"
    s "Plus, it\'s not like you can get into more trouble?"

menu:
        "Leave":
            jump leave_choice
        "Stay":
            jump stay_choice

label leave_choice:

    show jeante unhappy

    je "Sorry bro, but I need to get home"

    show samira unhappy

    s "It was worth a shot"

    show samira sadsmile

    s "c\'mere"

    scene bg hug

    je "Stay safe Samira"
    s "I'll be back to harass your sorry ass before you know it"

    scene bg black

    "That was the last time he ever saw her."
    "What was supposed to have been simple grab-n-go had turned awry."
    "They had failed, and the world was going to end."

    scene bg bad ending
    pause

    return

label stay_choice:

    show jeante serious
    
    je "You know what? Fuck it, I'm staying!"

    show samira happy

    s "Woo!"

    scene bg black

    show samira nervous
    "As midnight drew closer, and closer, Samira grew more and more antsy."
    "Though she would be reluctant to admit it, Jeante knew how stressed she was probably feeling."
    "Jeante didn’t want to add to it, but there was something nagging at him."
menu:
    "Say what's on your mind":
    
    ##choice to say it or not






    # This ends the game.

    return