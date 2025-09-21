# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jo = Character("Jordan", color="#d87210")
define s = Character("Samira", color="#780606")
define je = Character("Jeante", color="dab10a")
define m = Character("Mrs.Huynh", color="#000435")
define e = Character("Ernesto", color="#d5c58a")


# The game starts here.

label start:

    scene bg parknight

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

    #Merry meet
    scene bg bus stop
    show jordan mad
    "The youth stares so intensely at a compass, it's a wonder it hasn't started melting"
    "They groan"
    "{i}What's that now, 6 false alarms? At this rate, the Dark Realm with get to the one first{/i}"
    "If they didn't know better, they would have though the thing was broken. But the mentor {i}had{/i} warned that it could work unexpectedly."
    
    show compass
    "For whatever reason, the compass was currently pointing at the sidewalk in front of them."
    "{i}Strange{/i}"
    "They had barely stepped onto bath before-"
    
    scene collision
    #how to add question marks until you get person's name
    pause

    scene bg bus stop
    show jordan serious at right
    show ernesto annoyed at left

    "Both Jordan and the jogger stagger backwards"

    e "You-?"
    e "Who just stands in the middle of sidewalk?"

    "Jordan's heart is racing. But not because of the collision"
    "The compass is glowing"
    "{i}Is it him?{/i}"
    "However, the compass isn't pointing at the young man, but at the card he'd dropped"#maybe he was supposed to be helping samira hand out fliers for a special promotion at the restaurant. maybe the one dropped was the last flier
    "Jordan picks it up. It's a flier for some soul food restaurant."

    jo "Where did you get this?"

    "The jogger snatches it away from them before they can get a good look at the address"

    e "What's it too you?"

    show jordan nervous
    jo "Uh"

    "Jordan realizes \"I'm looking for the one destined to prevent looming evil\" probably wouldn't go over well."

    show jordan serious # or contemplative
    "They quickly think up a lie"
    jo "I think I used to go to this place when I was younger, but I don't remember the address"

    e "..."

    show ernesto neutral

    e "I suppose you can take a photo of it"

    "He holds it out"
    "Jordan takes out their phone and snaps a picture"

    jo "Thank you"

    e "I'm Ernesto by the way."

    show jordan nervous

    jo "..."
    jo "My name is Jordan"

    e "You should probably stop standing in the middle of sidewalks."

    "Ernesto jogs away"
    "As soon as Ernesto is gone, Jordan takes out their phone and enters the restaurant address"
    "{i}Huh, it's really close by? What does preventing great evil have to do with a soul food restaurant though{/i}"

    #maybe change this  to the library. perhaps she was just leaving for 
    scene bg gigis soulfood parking lot
    "It was this they were still wondering as they arrived at the parking lot of the restaurant"
    #question mark until we know her name
    "Before they can get to the door a young woman passes them to get to her car"
    "The compass goes haywire, and glows so intensly that they have to look away"
    "{i}That's new...Could it be?{/i}"
    "Jordan approaches the woman . Every step they take, the compass glows brighter and brighter"

    jo "Um, excuse me?"

    show samira sus
    "The woman turns to look at them, a wary look on her face."
    "It was at that moment that Jordan realized the next thing to come out of their mouth would probably sound really creepy or weird."
    "Perhaps it was for the best that they never got the chance to speak"

    #scene bg guy appears
    hide samira sus
    show knife guy
    "Out of nowhere, a man with strange blue skin appears. He starts heading towards Samira and Jordan. He's brandishing a knife"

    #scene bg jordan touching arrows
    "Instincts kicking in, Jordan draws their bow and prepares to loose an arrow"

    #scene bg ernesto defends/attacks
    "But before they can take take aim, Ernesto tackles the man."
    "Jordan knew that the man could easily escape and Ernesto would be bleeding on the pavement"
    "But he wasn't after the young man"
    "If he made another move, he'd have an arrow through his skull in an instant."
   
    "Instead, he glares at Samira"
    "man" "You win...for now. But next time, we won't go as easy." 
    "With that, he dissappears into a cloud of smoke"

    show ernesto panicked
    show samira panicked
    s "..."
    e "..."

    "Both Ernesto and the woman are staring at Jordan now"

    jo "Well... I suppose that makes this easie-"
    s "WHY THE FUCK DO YOU HAVE A FUCKING BOW AND ARROW!"
    e "Why was that man chasing Samira?" 
    "{i}So that's what her name is...{/i}"
    #For some reason, that line up there makes a good ending. If nothing else, I'd like to have an ending scene with them looking in the parking lot. But what about the kneeling scene TT. If need be, we could skip over the parking lot attack and just mention it in retrospect

    scene bg hq #aka, a council member's living room/basement.  They're near the end of the meeting
    #Just a bunch of comments from the council members here
    #She's prolly using her crutches here because she's expecting to be moving less

    show s nervous
    "Samira is very uncomfortable with all the attention being placed on her"

    scene jo suave kneel
    
    # maybe instead of at hq, they're discussing this in the car
    scene hq
    "She remembers how Jordan swore that no harm would befall her "
    "Sure, all of this was weird as fuck, but for seem reason she kinda believed them?"
    "At least they let her bring Jeante."
    "Speaking of Jeante, he looked as uncomfortable as she was"

    show je sus
    show s nervous
    
    je "This is so cooked. I don't know how they expect someone to learn all of this in a month."
    s "I mean, Jordan looks like they can kill someone? And Ernesto knows how to fight too? That'll probably make things easier"
    je "But you're the one who has to kill the boss!" 
    "Samira sighs"
    s "I'd rather not do this, but I also don't really want to see what happens if I do nothing"
    s "I must've been chosen for a reason"
    s "If I just follow everything they say, I'll be fine"
    je "I guess..."

    #it would be cool to have cutscenes, to be added later if i have
    #Trial of Bravery

    #honeslty, Imma prolly delete ernesto from teh character roster. he doesn't really even do much, and it would give more time to focuse on the other characters
    scene bg jeantes car
    "RING!!!!"
    "Jeante taps a button on his "












    # This ends the game.

    return