screen keypad_screen:
    add "bg black.png"
    modal True
    
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

    hbox:
        spacing 10

    vbox:
        xalign 0.5
        yalign 0.5
        grid 3 4:

            textbutton "1" action Keypad("1") text_size 80
            textbutton "2" action Keypad("2") text_size 80
            textbutton "3" action Keypad("3") text_size 80
            textbutton "4" action Keypad("4") text_size 80
            textbutton "5" action Keypad("5") text_size 80
            textbutton "6" action Keypad("6") text_size 80
            textbutton "7" action Keypad("7") text_size 80
            textbutton "8" action Keypad("8") text_size 80
            textbutton "9" action Keypad("9") text_size 80
            textbutton "Clear" action Keypad("clear") text_size 60
            textbutton "0" action Keypad("0") text_size 80
            textbutton "Enter" action Keypad("enter") text_size 60

init python:
    class Keypad(object):
        def __init__(self, value):
            self.value = value
            self.input_string = "0582"

        def __call__(self):
            if self.value == "clear":
                self.input_string = ""
            elif self.value == "enter":
                if self.input_string == "0582":
                    renpy.hide_screen("keypad_screen")
                    renpy.call("success_screen")
                else:
                    renpy.call("failure_screen")
            else:
                self.input_string += self.value

label success_screen:
    "Success! We're in!"
    pause 0.1
    jump crackedcode

label failure_screen:
    "Sorry, that's not the correct code. Please try again."
    O "."
    jump keypad_screen2

screen keypad_screen2:
    add "buttons/keypad.png" at Position(xpos=0.2,ypos=0.05)
    modal True
    
    add "bg black.png"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

    hbox:
        xalign 0.5
        yalign 0.5

    vbox:
        xalign 0.5
        yalign 0.5
        grid 3 4:

            textbutton "1" action Keypad2("1") text_size 80
            textbutton "2" action Keypad2("2") text_size 80
            textbutton "3" action Keypad2("3") text_size 80
            textbutton "4" action Keypad2("4") text_size 80
            textbutton "5" action Keypad2("5") text_size 80
            textbutton "6" action Keypad2("6") text_size 80
            textbutton "7" action Keypad2("7") text_size 80
            textbutton "8" action Keypad2("8") text_size 80
            textbutton "9" action Keypad2("9") text_size 80
            textbutton "Clear" action Keypad2("clear") text_size 60
            textbutton "0" action Keypad2("0") text_size 80
            textbutton "Enter" action Keypad2("enter") text_size 60

init python:
    class Keypad2(object):
        def __init__(self, value):
            self.value = value
            self.input_string = ""

        def __call__(self):
            if self.value == "clear":
                self.input_string = ""
            elif self.value == "enter":
                if self.input_string == "0582":
                    renpy.hide_screen("keypad_screen2")
                    renpy.call("success_screen")
                else:
                    renpy.call("failure_screen")
            else:
                self.input_string += self.value


label complete_fail:    
    R "\"Damn...What now?\""
    K "\"Not sure. Guess this was a bust.\""
    R "\"Should we maybe try again tomorrow?\""
    K "\"I guess.\""
    play sound "audio/military-alarm.ogg"
    R worried "\"Kiko...\""
    K worried "\"Oh no.\""
    M "\"You're surrounded! Come out with your hands up!\""
    R "\"What do we do?\""
    K "\"What else can we do?\""
    R "\"Well..It's been nice knowing you Kiko.\""
    K "\"Same to you, [name]. I'll miss ya.\""
    pause 1.0
    show screen keypadFail
