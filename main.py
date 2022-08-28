from time import sleep
import random
from threading import Thread
import pyglet

def perlin_noise(n, intensity = 1):
    return random.randint(n-intensity, n+intensity)

size = 60
window = pyglet.window.Window(16*size, 9*size, "Perlin Noise")

batch = pyglet.graphics.Batch()

@window.event
def on_draw():
    window.clear()
    batch.draw()

pause = False

@window.event
def on_key_release(symbol, modifiers):
    global pause
    if symbol == pyglet.window.key.SPACE:
        if pause:
            pause = False
        else:
            pause = True

number_of_lines = 100
line_size = int(window.width/number_of_lines)
lines = []
init_y = int(window.height/2)
y = init_y
x = line_size

def logic(delta_time):
    if not pause:
        global y
        global x
        old_y = y
        y = perlin_noise(y, 21)
        if y < 0 or y > window.height:
            y = init_y
        lines.append(pyglet.shapes.Line(x-line_size, old_y, x, y, 2,  (20, 148, 20), batch=batch))
        x += line_size
        if len(lines) == number_of_lines:
            lines.clear()
            y = init_y
            x = line_size

pyglet.clock.schedule(logic)
pyglet.app.run()