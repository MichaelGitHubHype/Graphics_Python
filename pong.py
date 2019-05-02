import pyglet
from pyglet.window import key


window = pyglet.window.Window()
keys = key.KeyStateHandler()
window.push_handlers(keys)

image = pyglet.resource.image('pong_paddle.png')
image_2 = pyglet.resource.image('pong_paddle.png')

one_x = 600
one_y = 50
two_x = 10
two_y = 50

@window.event
def on_draw():
    global one_x, one_y, two_x, two_y
    window.clear()
    image.blit(one_x, one_y)
    image_2.blit(two_x, two_y)

    if keys[key.UP]:
        one_y += 10
    if keys[key.DOWN]:
        one_y -= 10
    if keys[key.W]:
        two_y += 10
    if keys[key.S]:
        two_y -= 10



pyglet.app.run()