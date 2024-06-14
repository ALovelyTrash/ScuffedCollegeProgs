import pygame as pg
#import os


pg.init()
sc = pg.display.set_mode((500, 500))
clock = pg.time.Clock()  # limits FPS to 60
#clock = pg.time.Clock()
run = True

dt = 0
vel = 600

player = pg.Vector2(sc.get_width()/2,sc.get_height())


while run:
    # poll for events
    # pg.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # fill the screen with a color to wipe away anythinpg from last frame
    sc.fill("purple")

    # RENDER YOUR pgAME HERE

    pg.draw.circle(sc,'pink',player,40)


    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player.y -= vel * dt
    if keys[pg.K_s]:
        player.y += vel * dt
    if keys[pg.K_a] and x > vel:
        player.x -= vel * dt
    if keys[pg.K_d] and x < sc.get_width():
        player.x += vel * dt


    # flip() the display to put your work on screen
    pg.display.flip()

    dt = clock.tick(10) / 1000

pg.quit()
