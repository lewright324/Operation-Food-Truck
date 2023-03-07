# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the

define R = Character("[name]", color="#2b96ae", image="riley")
image define riley blank = "side riley blank.png"
image define riley shocked = "side riley shocked.png"
image define riley upset = "side riley upset.png"
image define riley funny = "side riley funny.png"
image define riley smile = "side riley smile.png"
image define riley worried = "side riley worried.png"

define W = Character("Worker", color="#1ade6288", image="worker")
image define worker blank = "side worker blank.png"
image define worker smile = "side worker smile.png"

define K = Character("Kiko", color="#e8d60ae4", image="kiko")
image define kiko smile = "side kiko smile.png"
image define kiko blank = "side kiko blank.png"
image define kiko chill = "side kiko chill.png"
image define kiko stressed = "side kiko stressed.png"
image define kiko worried = "side kiko worried.png"
image define kiko shocked = "side kiko shocked.png"

define M = Character("Official 2", color="#491bffc3", image="mark")
image define mark blank = "side mark blank.png"

define Ma = Character("Mark Richardson", color="#491bffc3", image="mark")
image define mark blank = "side mark blank.png"


image define rectangle = "gui/textbg.png"

define J = Character("Official 1", color="#ed0000ff", image = "john")
image define john blank = "side john blank.png"
image define john angry = "side john angry.png"

define G = Character("Gov. Ashby", color="#e01559dc", image="ashby")
image define ashby blank = "side ashby blank.png"
image define ashby smile = "side ashby smile.png"

define r_nvl = Character("[name]", kind=nvl, image="riley", callback=Phone_SendSound)
define k_nvl = Character("Kiko", kind=nvl, image="kiko", callback=Phone_ReceiveSound)

define config.adv_nvl_transition = None
define config.nvl_adv_transition = Dissolve(0.3)

define O = Character(None, window_left_margin=160, window_background = None, what_size=30, what_xalign=-0.1, what_yalign=-3.2, what_textalign=0.4)

default ice_cream = False
default hot_dog = False
default taco = False
default key = False
default badge = True
default health_points = 3
define fakename = False
define realname = False

##TOWN DETAILS
# Governor = Martine Ashby
# Town = Meresioux, Population = 2000
# Town has serious pollution problem. Town is forced to abide by strict Environemntal laws.
# Official 1 - John
# Official 2 - Mark


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

image mark_walking:
    "sprites/player/mark_walking_1.png"
    pause 0.5
    "sprites/player/mark_walking_2.png"
    pause 0.5
    "sprites/player/mark_walking_3.png"
    pause 0.5
    "sprites/player/mark_walking_4.png"
    pause 0.5
    "sprites/player/mark_walking_5.png"
    pause 0.5
    "sprites/player/mark_walking_6.png"
    pause 0.5
    "sprites/player/mark_walking_7.png"
    pause 0.5

image riley_approach_official:
    "rileystep1.png"
    pause 0.3
    "rileystep2.png"
    pause 0.3
    "rileystep3.png"
    pause 0.3

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

image computer_lab:
    "lab/l0_computerlab01.png"
    pause 0.1
    "lab/l0_computerlab02.png"
    pause 0.1
    "lab/l0_computerlab03.png"
    pause 0.1
    "lab/l0_computerlab04.png"
    pause 0.1
    "lab/l0_computerlab05.png"
    pause 0.1
    "lab/l0_computerlab06.png"
    pause 0.1
    "lab/l0_computerlab07.png"
    pause 0.1
    "lab/l0_computerlab08.png"
    pause 0.1
    "lab/l0_computerlab09.png"
    pause 0.1
    "lab/l0_computerlab10.png"
    pause 0.1
    "lab/l0_computerlab11.png"
    pause 0.1
    "lab/l0_computerlab12.png"
    pause 0.1
    "lab/l0_computerlab13.png"
    pause 0.1
    "lab/l0_computerlab14.png"
    pause 0.1
    "lab/l0_computerlab15.png"
    pause 0.1
    "lab/l0_computerlab16.png"
    pause 0.1
    "lab/l0_computerlab17.png"
    pause 0.1
    "lab/l0_computerlab18.png"
    pause 0.1
    repeat 

image besties_approach2:
    "sprites/player/besties_walk2/besties_approach1.png"
    pause 0.4
    "sprites/player/besties_walk2/besties_approach2.png"
    pause 0.4
    "sprites/player/besties_walk2/besties_approach3.png"
    pause 0.4

image besties_approach:
    "sprites/player/besties_walk/besties_approach1.png"
    pause 0.4
    "sprites/player/besties_walk/besties_approach2.png"
    pause 0.4



define slowdissolve = Dissolve(1.0)
define chardissolve = Dissolve(0.25)
define config.default_text_cps = 20 #0-100 is accepted
define hide_textbox = Character(None,window_background=None)


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

transform mid_ground_sprite:
    xalign -0.010
    yalign -.23
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

transform approach_official:
    xalign -0.009
    yalign -.10
    xoffset - 20
    yoffset 80

init python:
    def set_computer_lab_bg():
        renpy.menu("stayorgo")
        renpy.show("computer_lab", at_position(0,0))



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
                self.start = [ self.anchors.get(i, i) for i in start ]
                self.dist = dist   
                self.child = child
                
            def __call__(self, t, sizes):           
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
        
            return renpy.display.layout.Motion(move, time, child, add_sizes=True,**properties)

        Shake = renpy.curry(_Shake)
    #

#


init:
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)

style button:
    properties gui.button_properties("button")
    activate_sound "audio/Retro10.ogg"

init:
    $ inventory  = []

#############################################
### ######### LABEL START ### ############
#############################################

label start:
       
stop music
play music "audio/Infiltrated.wav" volume .3
scene bg black
    
centered "Welcome to Operation Food Truck."

init:
    $ health_points = 3

scene bg black 

window hide
python:
    name = renpy.input(_("What is your first name?"))
    name = name.strip().capitalize() or __("Riley")

scene bg black
centered "Welcome [name]."
centered "This game will depict scenes of violence. Player discretion is advised."

stop music fadeout 1.0

scene city2 with slowdissolve
$ renpy.layer_at_list([pan_scene_right])

"Out of everything they could have put here."
"Out of all of the things your little town could have benefitted from…"
"They made a plaza…"
"For food trucks."

#PAN ACROSS THE CITY SLOWLY

#Fade into a scene showing the main Character standing at the bottom of the plaza

"Something has always felt somewhat off about this town, but recently - even more so."
"Over the past few years your small town, officially named {color=#6c198b}Meresioux{/color}, locally known as {color=#6c198b}the Zoo{/color}, has been overcome by pollution."

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

scene apocalypsetowntruck with chardissolve

"At one point a tractor trailer came through town with new electronics and updated equipment such as touch screen cell-phones and flat-screen TVs."
"Other than that, it was as if {color=#6c198b}Meresioux{/color} was frozen in time."

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
    $ inventory.append("ice_cream")
    show item ice_cream at Position(xpos=0.5, ypos=0.53)
    show pixelrectangle at Position(xpos=0.5, ypos=.83)
    centered "{color=#000000}You acquired ice cream!{/color}"
    hide item ice_cream
    hide pixelrectangle
    jump snackdecision

label tacotruck:
    $inventory.append("taco")
    show item taco at Position(xpos=0.50, ypos=0.48)
    show pixelrectangle at Position(xpos=0.5, ypos=.83)
    centered "{color=#000000}You acquired a taco!{/color}"
    hide pixelrectangle
    hide item taco
    jump snackdecision

label hotdog:
    $ inventory.append("hot_dog")
    show item hot_dog at Position(xpos=0.5, ypos=0.47)
    show pixelrectangle at Position(xpos=0.5, ypos=.83)
    centered "{color=#000000}You acquired a hot dog!{/color}"
    hide pixelrectangle
    hide item hot_dog
    jump snackdecision
    

label snackdecision:
    show screen gameUI
    show screen InvUI
    "My favorite. How satisfying."
    "Even if the food trucks were an adjustment as a whole, you could get used to this."
#

scene riley_bedroom with slowdissolve

R blank "I spend so much time scrolling meaningless and mind-numbing forums just to pass the time."
R "There was never anything to do here anyway."
R "I'm at the point of restlessness where I feel like I could jump out of my skin."
R "When will things change?"

play sound "collapsing.ogg" volume .5

scene riley_bedroom with sshake

pause 2.0

R "\"What the hell was that?!\""

## pan to image outside of window
# There should be a food truck parked outside and two men in black suits standing next to it.

R "\"I should go see what that was.\""

pause .03

scene city4truck with slowdissolve
show screen gameUI with chardissolve

show riley_walking_2 at ground_sprite
show officials_idle at Position(xalign = .2, yalign = .66, xoffset = -20, yoffset = 50)
show dog_5 at dog_sprite

"So far nothing seems to look out of order..."
"For such a loud explosion, no one seems to be freaking out."
"{i}Was it all in my head?{/i}"
"In any case, if  I want to figure out what's going on I have to act natural."

hide riley_walking_2
show riley_walking at ground_sprite


menu stealth:
    "What's my next move?"
    "Approach slowly":
        show officials_idle at Position(xalign = .2, yalign = .66, xoffset = -20, yoffset = 50)
        jump approach
    "Look around":
        jump lookaround

label approach:
    show riley_walking at ground_sprite
    show officials_idle at Position(xalign = .2, yalign = .66, xoffset = -20, yoffset = 50)


"I've done nothing wrong, I'm just an average patron looking to get a snack from a food truck."
hide riley_walking
hide riley_walking_2
show riley_approach_official at Position(xalign = .16, yalign = -.1, xoffset = -20, yoffset = 50)
"There's nothing wrong with approaching a food truck. That's what they're here for."
hide riley_approach_official
show riley_approach_official at Position(xalign = .63, yalign = -.1, xoffset = -20, yoffset = 50)

"So why do my feet feel so heavy the closer I get to the truck?"

O "."
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
    $ inventory.append("ice_cream")


if hot_dog:
    R blank "\"Just a hotdog, please.\""
    W smile "\"One hot dog coming right up!\""
    $ inventory.append("hot_dog")

if taco:
    R blank "\"Just a chicken taco, please.\""
    W smile "\"One chicken taco coming right up!\""
    $ inventory.append("taco")

R blank "{i}I usually leave a tip but who knows who it would go to. Was he working with them?{/i}"
R "{i} Was this food even safe?{/i}"

show govdudes at officials_truck with chardissolve

"As you wait for him to prepare your food you notice that the two suited men you saw from your window are watching you."

"Before you can ask any questions, the worker returns with your food."

R "\"Hey, who are those guys?\""

W "\"Oh, they're still here? Well, they're just some officers from the government. The {b} federal {/b} government!\""
W "\"They've been coming around a lot lately. Isn't that exciting?\""

"I don't know if I would use those words."

R "\"Oh, so like government officials?\""

W smile "\" Yeah, they're just here to check up on us. Make sure we're following the rules.\""

R shocked "\"Rules?\", you wondered out-loud."

if ice_cream:
    W blank "The man looked at you for a moment before smiling and handing you your ice cream,"
    W smile "\"You better enjoy this before it melts.\""
    show worker smile at Position(xpos = 0.34, xanchor=0.5, ypos=0.276, yanchor=0.1)

    "You took your ice cream hesitantly before handing over your cash."

else:
    W blank " The man looked at you for a moment before smiling and handing you your food,"

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

"Anyway, there's not much more I can learn from here. I have to approach the truck."
show officials_idle at Position(xalign = .2, yalign = .7, xoffset = -20, yoffset = 50)
hide screen PlazaPC
jump approach

label leavetruck:

show city4truck with slowdissolve
"How menacing."
"If you didn't have a bad feeling before, you definitely do now."

if ice_cream:
    $ inventory.remove("ice_cream")

if hot_dog:
    $ inventory.remove("hot_dog")

if taco:
    $ inventory.remove("taco")

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
show besties at Position(xalign = .6, yalign = -.7, xoffset = -20, yoffset = 50)

R blank "\"Okay. So this is where they were standing earlier before I saw them again when I was ordering from the food-truck."

K blank "\"Weird, since the food trucks came over here, it looks like businesses must be opening up.\""

R "\"That's what I thought too but something doesn't seem right. I suspect they're doing something inside the cafe.\""

K "\"So what makes you think this whole area isn't tapped?\""

R shocked "..."

R "\"I guess I didn't think of that. Act natural for the rest of the time we're out here.\""

K "\"[name], if they have the place tapped then you can guarantee that they already heard that and are on to you.\""

R upset "\"Don't freak me out!\""

K "\"Sorry, sorry.\""

K "\"Seriously though, we need figure out what's going on and get out of here.\""

R blank "\"Agreed.\""

"You looked around for a moment, seeing if anything stood out."
"If you didn't look suspicious before, you were definitely looking more suspicious as this was your third time hanging around this truck today."
"You had to find what you needed now or else you would have to wait a few days to return in order to avoid any questionings or detection."

R "Look! - There's a {b}{color=#ffd700}key{/b}{/color} attached to the umbrella."
R "Watch my back while I grab it."

hide besties
show besties_walk at Position(xalign = .6, yalign = -.7, xoffset = -20, yoffset = 50)
pause .8
hide besties_walk
show besties_apart at Position(xalign = .6, yalign = -.7, xoffset = -20, yoffset = 50)

play sound "audio/achievement.mp3"
show acquiredkey at Position(xalign = 0.55, yalign = 0.5)
centered "{b}{color=#00ff00}You found a {/color}{color=#FFFF}Key!{/color}{/b}"
stop sound
$ inventory.append("key")
hide acquiredkey

"I wonder what it goes to?"

O "Objective - Determine where the {color=#ffd700}Key{/color} should go"

### ADD TO INVENTORY ###

K "\"Maybe we should check inside the cafe. We can get an idea of what it may go to.\""

R shocked "\"Or walk into a government secret mission that we're not supposed to know anything about.\""

K "\"Or that.\""
K "\"But what other choice do we have? What else can we do from out here?\""

"You knew Kiko was right. Your best move was to check out the cafe."

scene cafe_noon_goods with slowdissolve

"Upon entering the coffee shop you were surprised to see the place so in-tact. It was frozen in time but was nearly spotless and smelled strongly of freshly brewed coffee."
"There were even a few customers sitting down either drinking coffee or waiting to be served."
"Could it be that your town was healing?"
"Maybe things weren't so nefarious after all."

########################################################################
### PUT A SECTION IN BETWEEN HERE TRANSITIONING BETWEEN THESE PARTS ###
########################################################################

scene city4truck with slowdissolve
show besties at Position(xalign=2.3, yalign=-1.1)
show officials_and_worker at Position(xalign=0.25, yalign=0.73)

"You and Kiko are standing outside of the food truck, trying to eavesdrop on the conversation between the officials and another food truck owner."

R blank "\"I can't hear anything. They're speaking too quietly.\""
K blank "\"Maybe we should follow them.\""
R shocked "\"Are you crazy? We can't just follow them.\""
K "\"Why not? We need to find out what's going on.\""
K "\"Besides, is it a crime to get a coffee?\""
"Honestly, around here you weren't so sure."
R blank "\"Fine. But let's be careful.\""

hide besties
show besties_approach at Position (xalign=2.3, yalign=-1.1)
O "."
hide besties_approach
show besties_approach at Position(xalign=2.0, yalign =-1.1)
O "."
hide besties_approach
show besties_approach at Position(xalign=1.7, yalign =-1.07)
O "."
hide besties_approach
show besties_approach at Position(xalign=1.4, yalign =-1.03)
O "."
hide besties_approach
show besties_approach at Position(xalign=1.2, yalign =-1.0)
O "."
hide besties_approach
show besties_approach2 at Position(xalign=1.0, yalign=-1.0)

"As you and Kiko approached the cafe the tall, bald officer opened the door for you both."
scene city4truck_open
hide officials_and_worker
show officialsdoor_and_worker at Position(xalign=0.23, yalign=0.73)
show besties_backs at Position(xalign=0.68, yalign=-.9)



J "We best be getting back to work."
M "Yeah. Thanks for your help ma'am."
hide officialsdoor_and_worker
show officialsplit_and_worker at Position(xalign=0.22, yalign=0.73)
show besties_backs at Position(xalign=0.45, yalign=-.9)


J "\"After you folks.\""

"You and Kiko exchanged a quick glance before entering the cafe, the close officers behind you."

pause 0.5
scene cafe_noon_goods with slowdissolve


### Develop plot about entering cafe & encountering one of the government officials. 
G smile "\"Hi there! Welcome to {color=#6c198b}Meresioux's{/color} first-ever coffee bar!\""
R shocked "\"Oh my god...\""
K shocked "\"Is that-...\""
R "\"The literal governor...yes.\""
"You and Kiko were pretty much frozen in fear."
"Out of all of the weird things that you have witnessed recently, this one takes the cake."
"Nevermind the fact that this old cafe has been here for years, just boarded up and changing the name of it doesn't make it new or a 'first' - what in the world was the governor doing behind the counter?"

G smile "\"Well don't be shy, folks! Let this nice man here get your order!\", she exclaimed while pointing to the bald official who was moving behind the counter to stand next to her."
"Wait...they work for the cafe?"
"You gave Kiko a look before hesitantly approaching the counter. Kiko did not follow suit. He was practically frozen in shock."

R worried "\"Uh..I'll take just a regular coffee.\""
J blank "\"Sure, any add-ons?\""
R "\"Um,\"your eyes rolled over the menu but you took nothing in. You were too focused on how strange this was."
R "\"Uh no, a plain coffee is fine.\""
J blank "\"Can I get a name for your coffee?\""

menu realorfake:
    "Tell the officer your real name":
        jump realname
    "Give a fake name":
        jump fakename
    

label realname:
    $ realname = True
    R shocked "\"My name is [name].\""
    J blank "The officer pauses for a moment before taking your name down."
    J "\"Okay [name]. Your coffee should be ready shortly."
    J blank "Coming right up, [name]."

    jump continueon


label fakename:
    $ fakename = True
    R shocked "\"Uh..You can put Aubrey.\""
    J blank "\"Can I put Aubrey or is your name Aubrey?\""
    R "\"My name is Aubrey.\""
    "You tried to say it as convincingly as possible. You weren't too good at acting but hopefully he bought it."
    J blank "Coming right up.....Aubrey."

    jump continueon

label continueon:
    "You release a breath you didn't know you were holding as the officer turns to his partner to relay your order."
    "Taking a step back you notice how...normal it looks in here."
    "You can't remember the last time you were inside of a business that was this bright and modern."
    "Looking around, you notice patrons enjoying their coffee and treats."
    "{i}How was no one else weirded out by all of this?{/i}"
    if fakename:
        M blank "\"Coffee for Aubrey?\""
    
    if realname:
        M blank "\"Order for Riley..\""
    
    R shocked "\"Um..thanks.\""
    M blank "\"Have a good day.\""
    J blank "\"Be safe.\""
    R "\"...Thanks.\""
    "You hurried over to Kiko who was already waiting by the door."
    R "\"Let's get the hell out of here.\""



### You originally think going into the cafe is a waste but you discover that while you were talking to the official, Kiko swiped his badge from him.
## show badge on screen. only features it should have is a picture of the official and the badge number.

scene city4truck with slowdissolve
show besties at Position(xalign=0.9,yalign=-.8)
R blank "\"Well, that was a bust.\""
K smile "\"Maybe not..\""
K smile "\"Look what I got..\""
play sound "audio/achievement.mp3"
show official badge at Position(xalign=0.5, yalign=0.05) with chardissolve
$ badge = True
$ inventory.append("badge")
R smile "\"Kiko!! Where did you get this?\""
stop sound
K "\"While you and Officer Dingus were talking, I noticed his partner's badge hanging off of the back of a chair.\""
K "\"I hurried up and shoved it in my pocket while he made your coffee before anyone noticed.\""
K "\"Maybe it's best you take it now though, I almost lost it twice.\""
"You took the badge from Kiko and put it in your own pocket."
hide official badge with slowdissolve
R "\"Kiko you're a genius.\""
K "\"Thank you, I try.\""
K "\"I figured we could return later tonight and see what we can find. Maybe we can put this to good use.\""
R "\"True. Let's meet back at 11. Everyone should be in by then and it will be dark enough to sneak in.\""
K "\"Okay. 11 then. I'll see you at 11.\""

pause 2.0
scene cafe_night_goods with slowdissolve

R worried "\"Are you sure they don't have cameras in here?\""
K blank "\"Honestly, no. I didn't notice any earlier but they could have secret cameras so we need to be quick.\""
R "\"Kiko!\""
K "\"Hey! Don't say my name in here incase they are recording.\""
R "\"We should just leave...\""
K "\"No way. We're way too deep into the crime now. If they're onto us, we should at least try to find something before they come get us.\""
K chill "\"Besides, if they were that good at tracking people down they would've caught me getting the badge earlier.\""
R "\"Good point. Let's go.\""
"You and Kiko walk behind the cafe bar to the 'employees only' door"
K "\"Wait! Look, there's a keypad lock.\""
K "\"If we can crack the code we can see what's back there.\""

"{b}~Try and see if you can crack the code.~{/b}"
### The door behind the counter has a door with a code on it. The code will be the official's badge number --> "000582"

show screen keypad_screen
O "."

label crackedcode:
    show blank_computer

###### cut to backroom of cafe that is filled with a bunch of monitors and computers but they are all blacked out.

    R shocked "\"What the hell is going on here?\""
    K "\"Let's figure out how to turn these on.\""


## Note, if player tries to enter badge number again, Kiko should say something like "Yeah, of course it's not that easy."
## Player should have 3 tries. 
### After the third try there should be an option about being able to answer a security question.
    K smile "\"Man, they really thought of everything.\""
####### The security question should say something easy like - "Not an aquarium but a ..." #######
## The password is Zoo
## The computer will unlock and all of the monitors will turn on showing pictures of people's homes and empty streets
## Riley and Kiko are watching a bank of monitors, which show various parts of the town.

    scene computer_lab with slowdissolve

R shocked "\"Surveillance?\""
R "\"They've been using the food trucks to monitor our every move.\""
K worried "\"This is crazy..\""
R "\"Those two government officials talking to the owner of the food truck...they {i}are{/i} surveilling.\""
"{i}Why?{/i}"
K worried "\" And according to these files, that's just the tip of the iceberg.\""
"Kiko holds up a folder labeled {color=#00ff00}'Operation Food Truck'{/color}."
K stressed "\"I found this folder on one of the desks,\""
K worried "\"They've been watching us for months.\""

"You and Kiko exchange a worried look."

R "\"What is all of this?\""

"As you flip through the folder you realize that the government has been using the food trucks to monitor the town's citizens."
"They have been siloing away those who were caught uncovering the truth and the babies being born with deformities due to all of the contamination."
"There are folders filled with loads of sensitive information about every single person in the town - bank account information, marriage status,  blood type, all of it."
"Within the files you also find that the government has been experimenting with a new type of energy source."
"The experiments on the source have been causing the environmental damage and health problems for the people in the town." 
"{b}This{/b} was the reason for the orange skies."

R "\"This is insane. All this time we thought it was us and it was them!\""
R "\"We have to do something.\""
K worried "\"But what can we do? Who knows who they have on their side.\""
R "\"We have to push this past {color=#6c198b}The Zoo{/color}. We need national attention. Theyll have to listen.\""
R "\"Maybe they can save us from this hell.."
R "\"Maybe we can finally see blue skies.\""
K stressed "\"It's worth a try..\""

"You flip the page again and a manilla folder is revealed."
show folder
pause 1.0
hide folder with chardissolve
show folder paper
pause 1.5
hide folder paper with chardissolve
show screen Rules
play music "audio/anti-robot facility.wav"

R "\"Body cam footage??\""
K "\"Oh my god..\""
R "\"That's why that worker pretended to not hear the boom! He was recording me! He was being monitored.\""
R "\...\""
R "\" I...I was being monitored.\""
K "\" [name]...\""
R "\" They must already be onto us. They know I'm suspicious of them.\""
R "\"That's why they're running the cafe. They've need easy access to their surveillance."
hide screen Rules
### *play intense music here that's slowly building up. ###
K "\"Which means we have to move even quicker.\""
R "\"No. We have to get out of here.\""
K "\"Look, I know you're scared but there's another door and we should see what's on the other side.\""
R "\"But what if there's another door on the other side of that door Kiko? Are we just going to keep going depeer and deeper?\""
R "\"They're on me. This has become only that more dangerous.\""
K "\"So I ask you again, [name]. If you're apprehended would you rather have no chance of freedom or would you rather be taken and wish that you had looked into more?\""
R "\"The rules say they aren't apprehending people though - they're obliterating. So what does it matter what we learn here if they kill us anyway?"
K "\"It's worth the shot...\" Kiko says, standing up and approaching the other door."
K "\"We have to take a chance.\""

menu stayorgo:
    "Stay and explore further.":
        jump stay
    "Bail. Run out the door.":
        jump leave

    
label leave:
    ##############################
    ###### GAME OVER SECTION ####
    ##############################
    play music "audio/anti-robot facility.wav"

    R worried "\"I'm sorry K. I can't.\""
    R "\"I have to go. I need to protect myself.\""
    K "\"Speak for yourself, [name]. I'll do what I can and hopefully can report back.\""
    "You give Kiko one last look before making your way out of the cafe."
    scene city4truck_night
    show riley_approach_official at approach_official

    R worried "Did i make the right decision?"

    hide riley_approach_official
    show rileycafe at Position(xalign=0.3, yalign=-0.27)

    R "Should I have stayed?"
    R "Maybe I should clear my head before heading straight home."
    show mark_walking at mid_ground_sprite
    Ma blank "\"Hey! You!\""
    R shocked "No..."
    R "\"Um, me?\""
    Ma "\Yes, you! Where are you headed?\""
    R "\"Um.."

    menu where:
        "I'm heading home.":
            jump home
        "Just taking a walk.":
            jump walk
    
    label walk:
        play music "audio/anti-robot facility.wav"

        R "\"I'm uh, just out for a walk.\""
        Ma blank "\"Are you aware you are on this {i}walk{/i} 2 hours after curfew?\""
        R "\"No, I-..I didn't know there was a curfew.\""
        Ma "\"Looks like I need to take you in for some questioning.\""
        R "{i}I can't go in for questioning. They have that footage of me.{/i}"
        R "{i}I have to get out of this.{/i}"
        scene long_road
        "Before you even could process, you were running."
        play sound running
        "Your feet were pounding against the pavement and your breathing was heavy."
        "This was a bad decision and you knew it but what else could you have done?"
        "You couldn't let yourself be apprehended. That would lead to obliteration."
        "The only way out was to run."
        "You couldn't be obliterated. You hadn't done anything wrong."
        "You hadn't even uncovered anything yet."
        "This couldn't be the end, could it?"
        play sound "audio/distant-gunshot.ogg"
        stop sound
        scene pitch-black
        pause 4.0
        $ health_points -= 1
        show screen GameOver
        scene computer_lab
        O "."
        hide screen GameOver
        

    label home:
        play music "audio/anti-robot facility.wav"

        R "\"I'm just heading home.\""
        Ma "\"From where?\""
        R "\"....\""
        Ma "\"....\""
        R "\"....\""
        Ma "\"Okay let's see some ID.\""
        "You're frozen in fear. You realize you have no choice as he approaches so you hand over your ID.\""
        Ma "\"How are you heading home...if your home is in the opposite direction of where you're walking.\""
        
        if fakename:
            Ma "\"And I thought your name was Aubrey..."
            Ma "\"This ID says [name]."

        R "\"...\""
        Ma "\"You're coming with me. I need to take you in for questioning."
        R "{i}I can't go in for questioning. They have that footage of me.{/i}"
        R "{i}and we stole that badge. I'm screwed if he takes me."
        R "{i}I have to get out of this.{/i}"
        scene long_road
        "Before you even could process, you were running."
        play sound running loop
        "Your feet were pounding against the pavement and your breathing was heavy."
        "This was a bad decision and you knew it but what else could you have done?"
        "You couldn't let yourself be apprehended. That would lead to obliteration."
        "The only way out was to run."
        "You couldn't be obliterated. You hadn't done anything wrong."
        "You hadn't even uncovered anything yet."
        "This couldn't be the end, could it?"
        stop sound
        play sound "audio/distant-gunshot.ogg"
        scene pitch-black
        pause 4.0
        stop sound
        $ health_points -= 1
        show screen GameOver
        scene computer_lab
        O "."
        hide screen GameOver

label stay:
##############################
###### GAME CONTINUES ######
##############################
## If Riley stays, the game continues on -  

R blank"\"You're right. This should be worth something.\""
"You and Kiko stand up from the desk and move to unlock open the other other door."
scene backlot
"Upon opening the door, you're greeted by soft voices and bright lights."
"There was a whole operation happening out back."
"The sky wasn't orange at all. In fact, for it to be nighttime it was practically day-light out here."
"How could you not have seen this from the front of the cafe?"
K worried "\"Why is it so bright?\", Kiko exclaimed in a whisper while blocking his eyes with his arm."
K "\"It's almost midnight and it looks like dawn.\""
R shocked "\"And look - More trucks!\""
K worried "\"Sshh! We need to move quickly.\""
R "\"And go where?\""
K "\"We need figure out what's inside that truck.\""
R blank "\"How are we going to do that?\""
K "\"I have an idea.\""


scene bg black
centered "{color=#FF0000}DO NOT CONTINUE ON - GAME IS NOT FINISHED LOL. STOP AND SAVE HERE.{/color}"

O "."


label end:

# This ends the game.

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
