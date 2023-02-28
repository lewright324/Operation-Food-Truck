screen gameUI():
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "UI/hearts_idle.png"
        hover "UI/hearts_hover.png"
        action ShowMenu("StatsUI")

    imagebutton:
        xalign .97
        yalign -0.074
        xoffset - 20
        yoffset 80
        idle "UI/satchel_idle.png"
        hover "UI/satchel_hover.png"
        action ShowMenu("InvUI")

screen StatsUI:
    add "UI/bg black.png"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40
            # Text Column
            vbox:
                spacing 10
                text "Health" size 40

            # Values Column     
            vbox:    
                spacing 10
                text "[health_points]" size 40
     
    ## Show a Return button
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/hearts_%s.png"
        action Return()
    
    imagebutton:
        xalign .97
        yalign -0.074
        xoffset - 20
        yoffset 80
        auto "UI/satchel_%s.png"
        action Return()

screen InvUI():
    add "UI/bg_inventoryscreen.png"
    modal True

    vbox:
        pos 0.1, 0.25
        for item in inventory.items:
            text "[item.name] - [item.description]\n"
    
    imagebutton auto "UI/inventoryscreen_return_%s.png":
        focus_mask True
        hover SetVariable("screen_tooltip", "Return")
        idle SetVariable("screen_tooltip", "")
        action Hide("InvUI"), ShowMenu("Stats")


## Point and Click Plaza

screen PlazaPC():
    imagebutton:
        auto "cafe_%s.png"
        action [Hide("displayTextScreen"), Return()]

        hovered Show("displayTextScreen", displayText = "Weird..You didn't notice before but shouldn't this place be boarded up?")
        unhovered Hide("displayTextScreen")

        
    imagebutton:
        xalign .2
        yalign .7
        xoffset -20
        yoffset 50
        auto "sprites/enemy/officials_%s.png"
        action ShowMenu("SpriteStats")

        hovered Show("displayTextScreen", displayText = "Creepy government officials? It might be best to take note.")
        unhovered Hide("displayTextScreen")
    
    imagebutton:
        xalign 0.12
        yalign 1.0
        xoffset -20
        yoffset 50
        auto "sprites/npc/dog_%s.png"
        action [Hide("displayTextScreen"), Return()]
    
        hovered Show("displayTextScreen", displayText = "A dog? You can't remember the last time that you've seen a dog.")
        unhovered Hide("displayTextScreen")


screen SpriteStats:
    add "UI/bg black.png"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40
            # Text Column
            vbox:
                spacing 10
                text "Official 1 Race" size 40
                text "Official 1 Height" size 40
                text "Official 1 Build" size 40
                text "Official 1 Age" size 40
                text "Official 1 Unique?" size 40

                text "Official 2 Race" size 40
                text "Official 2 Height" size 40
                text "Official 2 Build" size 40
                text "Official 2 Age" size 40
                text "Official 2 Unique?" size 40

            # Values Column     
            vbox:    
                spacing 10
                text "Pale" size 40
                text "Tall" size 40
                text "Average" size 40
                text "Almost-old" size 40
                text "Receding hairline" size 40

                text "Less Pale" size 40
                text "Shorter" size 40
                text "Chubby" size 40
                text "Probably 30's" size 40
                text "Hairy" size 40
        
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/return_%s.png"
        action Return()

                
# Display Text

screen displayTextScreen:
    default displayText = ""
    vbox:
        xalign 0.5
        yalign 0.2
        frame:
            text displayText