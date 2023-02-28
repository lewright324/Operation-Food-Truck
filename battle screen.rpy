screen gameover():
    if health_points <= 0:
        action Show("GameO")

screen GameO:
    add "UI/pitchblackbg.png"
    centered "Game Over"
