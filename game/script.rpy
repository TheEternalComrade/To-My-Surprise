# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define jo = Character("Jordan", color="#d87210", image="jordan")
define s = Character("Samira", color="#780606", image="samira")
define je = Character("Jeante", color="#bf77f6", image="jeante")
define m = Character("Mrs.Huynh", color="#000435", image="master")
define e = Character("Ernesto", color="#d5c58a", image="ernesto")

define config.side_image_only_not_showing = True


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

    "A grin breaks out across Mrs. Huynh's face. She's trained them well."

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
    with fade
    # slow fade in to:

    #Merry meet

    scene bg busy hallway
    show samira angry at right
    show jeante smile at left
    s  "What the hell was that test? I swear she didn't cover half of that shit in class"

    show jeante bashful at left

    je "Eh, it wasn't that bad."

    show samira smile at right

    "Samira flicks his letterman jacket."

    show jeante smile at left

    s "Ok, nerd. We can always count on you to fuck up the curve."
    je "Hey, you keep talking like that and I eat all the jerk chicken!"
    
    show samira thoughtful at right

    "Samira rolls her eyes."

    show samira smile

    s "Fineeeeeee"

    scene bg busy hallway

    "They head over to their \"VIP Senior Table\"."

    scene bg vipst
    
    "Jeante lays out the spread of food he had brought for them."

    #maybe a drawing of this if I have time
    "Rice and peas, jerk chicken, and even some fried plantain!"

  
    "Samira scoops up a generous amount of each."

 

    je serious "Hey! Save some for me"
    s smile"Your parents may be assholes, but they sure can cook!"
    je nervous"Yeah"

    "However, before she can get more than a few spoonfuls-"

    show jordan serious

    "???" "Hey, can we talk? It\'s really important"
    "Samira reluctantly looks up at the person who\'d dared to interrupt their feast"
    "It was another senior that Samira didn\'t know that well. Jordan something? She vaguely remembered thinking in passing that they were cute but not much else"
    "She looks at Jeante"
    "He just shrugs"
    show jordan serious at left

    # yes or no
    # no makes them slightly annoyed at you and they sit down anyway or maybe they crash out at the rejection and they get kicked out fo school. that would be funny+++++
    #yes is the good girl option

menu:
    "Let them sit":
        jump let_sit_choice
    "Rebuke them":
        jump rebuke_choice

label rebuke_choice:
    s neutral "Nah, I'm kind occupied right now"
    "She gestures towards her plate"
    s neutral "It can't be {i}that{/i} important. Maybe later"

    
    jo serious "..."

    #it would be cool if there was some sort of shake
    jo angry "HOW DARE SHE!"
    "What they had spent so much of their life training for, she simply dismisses?"
    "They see red"

    scene bg black

    "Jordan has to be escorted out of the school."
    "It took several security guards to do it."
    "They never got to tell Samira that she was the chosen one."
    "The world ends"

    scene bg bad ending
    pause

    return



label let_sit_choice:    

    s neutral "Aight, pull up a seat I guess"

    scene bg vipst3

    "She continues eating her food"

    jo serious"I might as well get to the point"
    "They pull out a key crafted in a beautiful star motif"
    s surprised "Woah!"
    s "That's a helluva key!"
    "They offer it up to Samira."
    s thoughtful"Thanks?"
    "Gingerly, she reaches out to grab it"
    "Suddenly, she's transported...somewhere else."

    scene bg treasure

    "Where the food was just a moment before, she sees an intricate chest."
    "It felt familiar and strange at the same time."
    "For some reason, she felt compelled to reach out for it."

    scene bg vipst3

    "But instead of the chest, there was her plate of food."
    "She drops it like it's made of lava."
    s surprised"What the fuck was that?"
    jo surprised "Jordan stares at her in disbelief"

    scene bg black
    jo "You're going to save this realm"

    #An explanation, disbelief, and some magical feats later

    scene bg vipst3

    je nervous "This is so cooked. What if you get attacked or something?"

    s nervous"I mean, Jordan seems pretty strong."
    "Their shirt is baggy, but it doesn\'t hide the impressive muscle beneath"
    s nervous"Plus they have those weapons"
    s nervous"They could probably protect me?"


    jo annoyed"Of course I'll protect you."

    je nervous"But you still have to go to some other realm!"


    s thoughtful"I'd rather not do this, but I also don't really want to see what happens if I do nothing"
    s thoughtful"I must've been chosen because I'll succeed."
    s smile"I'll be fine!"
    je nervous"I guess..."
    s smile"Now come on, let\'s finish this food before lunch is over"
    je serious"Bruh. How do you still have an appetite?"
    "Jordan stands up  to leave"
    s "You too Jordan!"
    "Samira had noticed them eyeing the spread"


    jo surprised"..."

    jo serious"I appreciate sentiment, but I have to leave."
    
    s sad"..."


    je sad"..."

    jo nervous"Maybe next time?"

    "With that, they take their leave."
    scene bg black
    with fade

    scene bg park night
    show jeante serious

    je "{i}This{/i} is it?"
    "Mrs. Huynh looks at him sideways."

    show jeante nervous

    je "Sorry, it's just... so normal."

    show jeante smile 

    je "Anyways"
    je "I brought some snacks! Y\'all should probably eat something before you go"
    
    show jeante smile at right
    show samira smile at left

    s "YEAAA!"

    hide samira
    show master smile at left
    
    m "How thoughtful!"

    scene bg park night
    show jordan thoughtful

    jo "We won't feel hunger in the dark realm"

    hide jordan
    show jeante sad at right
    show samira sad at left

    "..."
    
    show jordan nervous

    jo "I suppose it wouldn't hurt"

    show jeante smile at right
    show samira smile at left
    s "YEAA!"

    scene bg black
    pause
    #fade

    scene bg park night

    "Jeante suddenly has the presence of mind to check the time"

    show jeante surprised

    "It's half past 10!"

    show jeante sad

    "He groans"

    je "My parents are gonna kill me"

    show jeante nervous at right
    show samira sad at left

    s "Oof, curfew"

    scene bg park night
    show jordan thoughtful
    
    jo "Why don\'t you stay until midnight?"
    
    hide jordan
    show jeante nervous
    je "My parents are really strict"
    je "They\'re probably already planning to jump me when I get home"

    hide jeante
    show samira thoughtful
    s "On the other hand..."
    s "It would really mean a lot if you were there to send me off"

    show samira smile
    s "Plus, it\'s not like you can get into more trouble?"

menu:
        "Leave":
            jump leave_choice
        "Stay":
            jump stay_choice

label leave_choice:
    hide samira
    show jeante sad

    je "Sorry bro, but I need to get home"

    hide jeante
    show jeante sad at right
    show samira sad at left

    s "It was worth a shot"

    show samira sad smile

    s "c\'mere"

    scene bg hug

    je "Stay safe Samira"
    s "I'll be back to harass your sorry ass before you know it"

    scene bg black
    pause

    "That was the last time he ever saw her."
    "What was supposed to have been simple grab-n-go had turned awry."
    "They had failed, and the world was going to end."

    scene bg bad ending
    pause

    return

label stay_choice:
    scene bg park night
    show jeante serious
    
    je "You know what? Fuck it, I'm staying!"


    show jeante smile at right
    show samira smile at left

    s "Woo!"

    scene bg black
    with fade

    scene bg park night

    show samira nervous
    "As midnight drew closer, and closer, Samira grew more and more antsy."
    "Though she would be reluctant to admit it, Jeante knew how stressed she was probably feeling."
    "Jeante didn\'t want to add to it, but there was something nagging at him."
menu:
    "Stay quiet":
        jump stay_quiet_choice
    "Say it":
        jump say_choice
    ##choice to say it or not

label stay_quiet_choice:
    scene bg park night
    show jeante nervous

    "He decides to stay quiet"
    je "{i}It's probably nothing anyway{/i}"
    "Like everyone else, he watches in awe as Samira and Jordan enter and dissapear through the door."

    scene bg black

    "That was the last time he ever saw her."
    "What was supposed to have been simple grab-n-go had turned awry."
    "They had failed, and the world was going to end."

    scene bg bad ending
    pause

    return

label say_choice:
    scene bg park night
    show jeante thoughtful

    jo "Why this place?"
    "Once again, Ms. Huynh side-eyes him"

    show jeante nervous at right
    show master serious at left

    m "This place"
    m "Has the most clear magical signature for the Sun Chest"

    show jeante thoughtful at right

    jo "But if the Sun Chest is so imporant to the dark realm, wouldn\'t they hide it better?"
    
    show master thoughtful 

    m "..."

    show master surprised

    m "You're right"

    show master serious

    "This is the wrong gate"

    hide master
    show jordan surprised at left
    show samira surprised
    show jeante surprised at right
    "What?!"

    scene bg park night
    show master serious

    "But I know where the right one is. We need to go {i}now{/i}"

    scene bg car drive

    scene bg library

    "Somehow they made it just in the nick of time"
    "Thank goodness for all-day libraries"

    show master serious

    "Ms.Huynh nods at Samira"

    scene bg library

    "Jordan grabs onto Samira\'s hand"
    "Samira takes a deep breath, closes her eyes, reaches forwards, and turns the key."
    "A door appears. She and Jordan step through"

    scene bg black
    with fade

    scene bg library

    "Samira would have thought that they were still in the same library except..."
    "In front of them was the Sun Chest"

    scene bg treasure

    "It was just as she remembered it from her vision"

    show jordan surprised

    "Jordan gasped"

    scene bg library
    "s relief" "Well...that was easy"
    "???" "Stop right there scoundrels!"

    show jordan serious at left
    show samira nervous at right

    s "{i} Fucking jinxed it{/i}"
    #scene bg armed in in library?
    "At once, Jordan summoned their shield and spear"
    s "Grab it and escape Samira! I\'ll hold him off..."

    hide samira
    show ernesto nervous at left
    show jordan serious at right
    "???" "WHOA! Is violence really worth a chest that can\'t even be opened?"

menu:
    "Attack him":
        jump dead_ernesto_choice
    "Hear him out":
        jump live_ernesto_choice

label dead_ernesto_choice:
    "Jordan had been expecting the young man to put up a fight"
    "But he did nothing to stop the spear from piercing straight through his heart"

    scene bg ernesto dead
    pause

    "For a moment, there is silence"
    "Then the world explodes into darkness"

    scene bg bad ending
    pause
    return
label live_ernesto_choice:
    scene bg library
    show jordan serious at right
    show ernesto nervous at left

    "Jordan remains on guard"
    jo "We need that chest to save our world."
    "???" "Well I\'m sure we can come to an agreement if-"

    show ernesto surprised

    "???" "How did you open that?"
    "The young man is looking at Samira now"
    "She's staring at the contents of the now open chest, the star key in the lock."

    show ernesto surprised
    "???" "Wait a second"
    "???" "“I think there\'s been a misunderstanding"

    scene bg backstory
    pause

    scene bg stones
    pause


    show jordan thoughtful

    jo "But, what are these stones for?"

    scene bg library

    show ernesto neutral

    "Ernesto shrugs"
    e "Our prophecy wasn't very clear on that"

    hide ernesto
    show samira neutral
    
    s "Fuck if I know."

    scene bg library

    "They sit in silence for a moment, trying to figure out what the hell they were for"

    show samira surprised

    s "Wait a second!"

    show samira neutral

    "Wait no, that's stupid as hell"

    hide samira
    show ernesto surprised

    e "Perhaps?"
    
    show ernesto neutral

    e "No that can\'t be it"

    hide ernesto
    show jordan surprised
    
    "For some reason, Jordan felt compelled to look up."

    show ernesto neutral

    e "Oh come on. The answer isn't written on the ceiling"

    scene bg ceiling#the dark shall keep the light, and the light shall keep the dark. Then will balance be restored
    pause

    scene bg library

    show samira smile
    s "Guys, I think I know the answer!"

menu:
    "Take the dark stone":
        jump dark_stone_choice
    "Take the light stone":
        jump light_stone_choice

label light_stone_choice:
    scene bg black
    "The world explodes into darkness"
    scene bg bad ending
    pause
    return

label dark_stone_choice:
    scene bg bright
    "The world is saved, and everyone can live happily ever after"

    scene bg good ending
    pause
    return