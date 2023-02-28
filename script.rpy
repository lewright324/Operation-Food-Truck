# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the

define R = Character("[name]", color="#2b96ae", image="riley")
image define riley blank = "side riley blank.png"
image define riley shocked = "side riley shocked.png"
image define riley upset = "side riley upset.png"
image define riley funny = "side riley funny.png"
image define riley smile = "side riley smile.png"


define W = Character("Worker", color="#1ade6288", image="worker")
image define worker blank = "side worker blank.png"
image define worker smile = "side worker smile.png"

define K = Character("Kiko", color="#e8d60ae4", image="kiko")
image define kiko smile = "side kiko smile.png"
image define kiko blank = "side kiko blank.png"
image define kiko chill = "side kiko chill.png"

define G = Character("Gov. Ashby", color="#e01559dc")

define r_nvl = Character("[name]", kind=nvl, image="riley", callback=Phone_SendSound)
define k_nvl = Character("Kiko", kind=nvl, image="kiko", callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

##TOWN DETAILS
# Governor = Martine Ashby
# Town = Meresioux, Population = 2000
# Town has serious pollution problem. Town is forced to abide by strict Environemntal laws.

#Images
image R:
    "side riley blank.png"

image W:
    "side worker.png"

image riley_walking:
    "riley_walking_1.png"
    pause 0.3
    "riley_walking_2.png"
    pause 0.3
    "riley_walking_3.png"
    pause 0.3
    repeat

image dog_running:
    "dog_1.png"
    pause 0.1
    "dog_2.png"
    pause 0.1
    "dog_3.png"
    pause 0.1
    "dog_4.png"
    pause 0.1
    "dog_5.png"
    pause 0.1

image riley_to_truck:
    "rileystep1.png"
    pause 0.3
    "rileystep2.png"
    pause 0.3
    "rileystep3.png"
    pause 0.3
    "rileystep4.png"
    pause 0.3
    "rileystep5.png"
    pause 0.3
    "rileystep6.png"

image background_video:
    "typing/sprite_00.png"
    pause 0.1
    "typing/sprite_01.png"
    pause 0.1
    "typing/sprite_02.png"
    pause 0.1
    "typing/sprite_03.png"
    pause 0.1
    "typing/sprite_04.png"
    pause 0.1
    "typing/sprite_05.png"
    pause 0.1
    "typing/sprite_06.png"
    pause 0.1
    "typing/sprite_07.png"
    pause 0.1
    "typing/sprite_08.png"
    pause 0.1
    "typing/sprite_09.png"
    pause 0.1
    "typing/sprite_10.png"
    pause 0.1
    repeat


define slowdissolve = Dissolve(1.0)
define chardissolve = Dissolve(0.25)
define config.default_text_cps = 20 #0-100 is accepted
define hide_textbox = Character(None,window_background=None)

default ice_cream = False
default hot_dog = False
default taco = False
default health_points = 3
default item_descriptions = {"key" : "Try using it in a door.", "Ice Cream" : "Sweet, frozen, sugary goodness!"}
default item_description = ""


init:
    python:
        left = Position(xpos=0.20)
        right = Position(xpos=0.70)

transform pan_scene_right:
    xpos 100
    linear 2 xpos 0

transform ground_sprite:
    xalign -0.005
    yalign -.14
    xoffset - 20
    yoffset 80

transform dog_sprite:
    xalign 0.0
    yalign 3.4
    xoffset - 20
    yoffset 50

transform ground_truck:
    xalign -10
    yalign 1.0
    xoffset -60
    yoffset 80

transform officials_truck:
    xalign 2.5
    yalign .95
    xoffset 70
    yoffset 80

transform pc_officials:
    xalign 2.5
    yalign .95
    xoffset 70
    yoffset 80

transform to_truck:
    xalign -0.02
    yalign -.9
    xoffset - 20
    yoffset 80

init python:

    class Inventory():
        def __init__(self, items, no_of_items):
            self.items = items
            self.no_of_items = no_of_items
            
        def add_item(self, item):
            self.items.append(item)
            self.no_of_items += 1
            
        def remove_item(self, item):
            self.items.remove(item)
            self.no_of_items -= 1
            
        def list_items(self):
            if len(self.items) < 1:
                R("I'm not carrying anything.")
            else:
                R("I am currently carrying:")
                for item in self.items:
                    R(f"{item.name}. {item.description}.")


    class InventoryItem():
        def __init__(self, name, description):
            self.name = name
            self.description = description

init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

#


init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)


### LABEL START

label start:

    default inventory = Inventory([],0)
        
    define ice_cream = InventoryItem("Ice Cream", "A sweet treat that can satisfy anyone who dares to indulge.")
    define door_key = InventoryItem("Key", "Try using it in a door.")
    define taco = InventoryItem("Taco", "A crispy corn tortilla stuffed with all the meat and fixin's of your stomach's desires.")
    define hot_dog = InventoryItem("Hot Dog", "Don't ask what it's made of, just enjoy.")

## END OF INVENTORY ITEMS ##

scene bg black

centered "Welcome to Operation Food Truck."

init:
    $ health_points = 3

scene bg black 

window hide
python:
    name = renpy.input(_("What is your first name?"))
    name = name.strip() or __("Riley")

menu R_pronoun_select:
        "Which gender-presentation would you prefer?"
        "Feminine-presenting":
            $ gender = "female"

        "Masculine-presenting":
            $ gender = "male"

scene bg black
centered "Welcome [name]."
centered "This game will depict scenes of violence. Player discretion is advised."

scene city2 with slowdissolve
$ renpy.layer_at_list([pan_scene_right])

"Out of everything they could have put here."
"Out of all of the things your little town could have benefitted from…"
"They made a plaza…"
"For food trucks."

#PAN ACROSS THE CITY SLOWLY

#Fade into a scene showing the main Character standing at the bottom of the plaza

"Something has always felt somewhat off about this town, but recently - even more so."
"Over the past few years your small town, officially named {color=#6c198b}Meresioux{/color}, locally known as {color=#6c198b} the Zoo{/color}, has been overcome by pollution."

scene apocalypsetown2 with slowdissolve

"No one was entirely sure where it had even come from."
"Your childhood was filled with blue skies, you couldn't remember exactly what it looked like but you were sure of it."

scene apocalypse1 with slowdissolve

"You were so sure, in fact, because you remember how terrified your mother was when everything changed."
"Suddenly your entire neighborhood was boarding up windows and wearing respirators."

scene apocalypsetown2_after with chardissolve

"{color=#6c198b}Meresioux's {/color} town governor,{color=#e01559dc}Gov. Martine Ashby{/color} sent out multiple local ordinances informing that any person or business that didn't comply would be prosecuted."
"So many animals were dead in the street and schools were closed because no one could breathe through all of the smog."
"When the dust eventually settled all that was left was an orange cloud above your town."
"Fields of grass were now brittle and brown and planes no longer flew overhead."
"Nothing had really even changed since."

show towntruck at ground_truck

"At one point a tractor trailer came through town with new electronics and updated equipment such as touch screen cell-phones and flat-screen TVs."
"Other than that, it was as if Meresioux was frozen in time."

scene apocalypsetown with slowdissolve
show rileystanding at ground_sprite

"Honestly, if you thought about it too long you would start to panic."
"It was during your teenage years that you realized that sometimes it was just easier to blow things off and go with the status quo."

scene city4truck with slowdissolve

"Now that you were feeling that same anxiety with the food trucks, you realized your coping mechanism wasn't working."
"Perhaps it was because all of these food-trucks were anything but status quo for this place."

"Maybe you could avoid all of the overthinking with a little snack."

#THIS SCENE THE PLAYER CAN CHOOSE TO PICK A FOOD TRUCK THAT HAS ICE CREAM, A TACO, OR A HOTDOG.

menu whichtruck:
    "You just had to decide just which snack to pick?"
    "Ice Cream Truck":
        $ ice_cream = True
        jump icecream
    "Taco Truck":
        $ taco = True
        jump tacotruck
    "Hot Dog Truck":
        $ hot_dog = True
        jump hotdog

label icecream:
    $ inventory.add_item(ice_cream)
    jump snackdecision

label tacotruck:
    $ inventory.add_item(taco)
    jump snackdecision

label hotdog:
    $ inventory.add_item(hot_dog)
    jump snackdecision
    

label snackdecision:
    show screen gameUI
    $ inventory.list_items()
    "My favorite. How satisfying."
        

#

scene riley_bedroom

"I spend so much time scrolling meaningless and mind-numbing forums just to pass the time."
"There was never anything to do here anyway."
"I'm at the point of restlessness where I feel like I could jump out of my skin."
"When will things change?"

play sound "collapsing.ogg" volume .5

scene riley_bedroom with sshake

pause 2.0

"What the hell was that?!"

## pan to image outside of window
# There should be a food truck parked outside and two men in black suits standing next to it.

"I should go see what that was."

pause .03

scene city4truck with slowdissolve
show screen gameUI with chardissolve

show riley_walking_2 at ground_sprite
show officials_idle at Position(xalign = .2, yalign = .7, xoffset = -20, yoffset = 50)
show dog_5 at dog_sprite

"So far nothing seems to look out of order..."
"For such a loud explosion, no one seems to be freaking out."
"{i}Was it all in my head?{/i}"
"In any case, if I want to figure out what's going on I have to act natural."

hide riley_walking_2
show riley_walking at ground_sprite


menu stealth:
    "What's my next move?"
    "Approach slowly":
        jump approach
    "Look around":
        jump lookaround

label approach:
    show riley_walking at ground_sprite

"I've done nothing wrong, I'm just an average patron looking to get a snack from a food truck."
hide riley_walking
hide riley_walking_2
show riley_to_truck at to_truck
"There's nothing wrong with approaching a food truck. That's what they're here for."
"So why do my feet feel so heavy the closer I get to the truck?"

hide riley_walking

scene closetruck2 with slowdissolve
show foodguy at Position(xpos = 0.34, xanchor=0.5, ypos=0.276, yanchor=0.1)

W smile "\" Hi there! What can I get for you?\""

R shocked "\"Did you not just hear that explosion?\""

W smile "\" Not sure what you mean?\""

R shocked "\"What?!\""
R shocked "\" The explosion that just shook my entire apartment building? You're telling me you didn't just hear that?\""

W smile "\"I'm afraid I'm not so sure what you're talking about. I've been out here all day and haven't heard a thing.\""

"What in the hell was going on?"

R shocked "..."

W smile "\"So, about that order - What can I get for you?\""

R "{i} There was no way I imagined that explosion. {/i}"
"{i} Something strange is definitely going on and now I don't know who to trust.{/i}"

if ice_cream:
    R blank "\"Just a vanilla cone, please.\""
    W smile "\"One vanilla cone coming right up!\""
    $ inventory.add_item(ice_cream)


if hot_dog:
    R blank "\"Just a hotdog, please.\""
    W smile "\"One hot dog coming right up!\""
    $ inventory.add_item(hot_dog)

if taco:
    R blank "\"Just a chicken taco, please.\""
    W smile "\"One chicken taco coming right up!\""
    $ inventory.add_item(taco)

R blank "{i}I usually leave a tip but who knows who it would go to. Was he working with them?{/i}"
R "{i} Was this food even safe?{/i}"

show govdudes at officials_truck

"As you wait for him to prepare your food you notice that the two suited men you saw from your window are watching you."

"Before you can ask any questions, the worker returns with your food."

R "\"Hey, who are those guys?\""

W "\"Oh, they're still here? Well, they're just some officers from the government. The {b} federal {/b} government!\""
W "\"They've been coming around a lot lately. Isn't that exciting?\""

"I don't know if I would use those words."

R "\"Oh, so like government officials?\""

show worker

W smile "\" Yeah, they're just here to check up on us. Make sure we're following the rules.\""

R shocked "\"Rules?\", you wondered out-loud."

if ice_cream:
    W blank "The man looked at you for a moment before smiling and handing you your ice cream,"
    W smile "\"You better enjoy this before it melts.\""
    hide worker
    show worker smile at Position(xpos = 0.34, xanchor=0.5, ypos=0.276, yanchor=0.1)

    "You took your ice cream hesitantly before handing over your cash."

else:
    W blank " The man looked at you for a moment before smiling and handing you your food,"
    hide worker

    W smile "\"You better enjoy this before it gets cold.\""
    "You took the foil-wrapped treat hesitantly before handing over your cash."

hide worker with slowdissolve
hide truck bg with slowdissolve
jump leavetruck

label lookaround:
    hide riley_walking
    show riley_walking_2 at ground_sprite

"Where the hell did that sound come from?"
"I should investigate."
"~{b}Note: Only click on the officials. Hover everything else.{/b}~"

show dog_running at dog_sprite
show screen PlazaPC
show riley_walking_2 at ground_sprite 
centered "."


## Possibly put in a point and click so player can look around and click on different elements 
## If this works, make clickable the 2 government men, a dog, a dark puddle by the food truck
## when you click the gov dudes there should be some commentary about how suspicious and out of place they look in your small town
## clicking the dog should be something neutral. Nothing interesting just a cute dog
## the puddle should say something like "Is that blood or oil?" "Am I getting paranoid?"

"Anyway, there's not much more I can learn from here. I have to approach the truck."
show officials_idle at Position(xalign = .2, yalign = .7, xoffset = -20, yoffset = 50)
hide screen PlazaPC
jump approach

label leavetruck:

show city4truck with slowdissolve
"How menacing."
"If you didn't have a bad feeling before, you definitely do now."

pause .8

scene riley_bedroom with slowdissolve

"As you pace back and forth in your bedroom room you can't get your mind off of what you just witnessed."
"What would the government want with your town?"
"What did they need to check up on?"
"What {b}{i}rules{/i}{/b} were you supposed to be following?"

R blank "\"This just doesn't make any sense. Why would they be worried about the food trucks specifically?\""

"You needed to talk to someone."

## Insert audio of a phone text sound
## show picture of a phone on the screen

nvl_narrator "New message with Kiko"
r_nvl "Kiko"
k_nvl "Hey [name]! What's up?"
r_nvl "Kiko you will not believe what I just saw."
k_nvl "What did you see?"
r_nvl "There are these government officials lingering around the new food trucks in town. I feel like something weird is going on."
k_nvl " Maybe they're just making sure they're not polluting the area anymore than they already have?"

"It was true. The sky was basically blood orange at all times thanks to years of pollution and 'accidental' chemical spills that took place in your town."
"You couldn't remember the last time you saw a blue sky."

r_nvl "I don't know K, things seem a bit weirder than that. Something is going on."
k_nvl smile "Eh well, Im down for an adventure if you want to check it out"
r_nvl "This is why youre my best friend. Meet me in the alley behind the old warehouse. Im afraid to talk on the phone."
k_nvl smile "Did I ever mention that you are incredibly dramatic?"

scene city1 with slowdissolve

K smile "\"Hey, crazy. \""

R funny "\" Im glad you find this funny? \""

K "\" Considering we have no idea what's even going on, I'm going to say yes I do. \""

R smile "You rolled your eyes. \"Whatever. \""

R "\"So anyway, earlier the guy from the food truck told me that the government guys are here to make sure that we're following 'rules'.\""

K "\" Do you think he meant our environmental laws? You know {color=#e01559dc}Governor Ashby{/color} has really cracked down on anyone who isn't abiding by them.\""

K "\"Apparently last year {color=#6c198b}The Zoo{/color} showed up as being 5 percent more polluted than 2 years ago.\""

R "\" Where did you hear that?\""
K "\"Uh..I don't know, I just heard it. \""

R upset "..."

R upset "\"Anyway - I think we should look into this. Even if that is the case, it still doesn't explain why they're hanging around the food trucks.\""

R blank "\" And {color=#e01559dc}Ashby{/color} always sends out press releases when she's changing something. These men came out of nowhere...Something isn't right. \""

R "\"Besides, didn't you hear that explosion earlier?\""

K chill "\"You know, I thought I heard something when I was in the shower but my mind usually plays tricks on me in there anyway so I wasn't sure.\""

R "\" You get paranoid in the shower?\""

K smile "\"My eyes are closed and the curtain sometimes moves. It can get kind of spooky in there.\""

R shocked "\"...\""

R smile "\" I worry about you. \""

K chill "\"Alright, alright. Anyway, I heard it so where do we start? \""

R "\" Well, I think we should go back and find those guys again. Once we find them maybe we can follow them and see what they're up to. \""

R "\" But we need to be careful. They're working with the food-truck guy I think. He acted like he didn't hear a thing.\""

K smile "\" Was he old? Maybe he can't hear too well. \""

R shocked "\"...\""

R blank "\" Let's just go.\""

scene city4truck with slowdissolve












# This ends the game.




"\"I never thought I'd uncover a government cover-up, but I did.\""
"\"And I'll keep fighting for the truth, no matter what.\""

return

## ALTERNATE TEXT SCENE 
# R "\" {i} Kiko.\""
# K blank "\"{i} Hey, [name]! What's up? \""
# R "\"{i} Kiko you will not believe what I just saw.{/i}\""

# K "\" {i} What did you see? {/i} \""

# R "\" {i} There are these government officials lingering around the new food trucks in town. I feel like something weird is going on. {/i} \""

#K "\" {i} Maybe they're just making sure they're not polluting the area anymore than they already have? {/i} \""

# "It was true. The sky was basically blood orange at all times thanks to years of pollution and ‘accidental' chemical spills that took place in your town."
# "You couldn't remember the last time you saw a blue sky."

# R "\" I don't know K, things seem a bit weirder than that. Something is going on.\""

# K smile "\" Eh well, Im down for an adventure if you want to check it out \""

# R smile "\" This is why youre my best friend. Meet me in the alley behind the old warehouse. Im afraid to talk on the phone. \""

# K smile "\" Did I ever mention that you are incredibly dramatic?\"" ### 
