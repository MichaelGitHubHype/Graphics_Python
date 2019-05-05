import pyglet
from pyglet.window import key


window = pyglet.window.Window()
keys = key.KeyStateHandler()
window.push_handlers(keys)

image = pyglet.resource.image('pong_paddle.png')
image_2 = pyglet.resource.image('pong_paddle.png')
ball = pyglet.resource.image('ball.png')

one_x = 600
one_y = 50
two_x = 10
two_y = 50
ball_x = 300
ball_y = 300
imageWidth = 100
imageHeight = 100
change_x = 1
change_y = 1
ball.width = imageWidth
ball.height = imageHeight


def update(dt):
    global ball_x, ball_y, change_x, change_y
    ball_x += change_x
    ball_y += change_y
    ball.x += change_x
    ball_y += 0.5
    if ball_x > 575:
        change_x = -1
    if ball_y > 440:
        change_y = -1
    if ball_x < 5:
        change_x = 1
    if ball_y < 2:
        change_y = 1


@window.event
def on_draw():
    global one_x, one_y, two_x, two_y, ball_x, ball_y
    ball.x, ball.y = ball_x, ball_y   # I think it helps the bug
    window.clear()
    image.blit(one_x, one_y)
    image_2.blit(two_x, two_y)
    ball.blit(ball_x, ball_y)

    if keys[key.UP]:
        one_y += 10
    if keys[key.DOWN]:
        one_y -= 10
    if keys[key.W]:
        two_y += 10
    if keys[key.S]:
        two_y -= 10

pyglet.clock.schedule(update)
pyglet.app.run()
