import pyglet

window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world',
                          x=window.width//2, # origin - left
                          y=window.height//2, # origin - bottom
                          anchor_x='center',
                          anchor_y='center')

change_x = 1
change_y = 1
def update(dt):
    global change_x, change_y
    if label.x > 595:
        change_x = -1
    if label.y > 480:
        change_y = -1
    if label.x < 5:
        change_x = 1
    if label.y < 2:
        change_y = 1

    label.x += change_x
    label.y += change_y
    print(label.x, label.y)

@window.event
def on_draw():
    window.clear()
    label.draw()


pyglet.clock.schedule(update)   # cause a timed event as fast as you can
pyglet.app.run()