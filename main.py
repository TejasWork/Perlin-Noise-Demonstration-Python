import random
import pyglet

# This perlin noise generator works in a very simple way
def perlin_noise(n, intensity = 1) -> float:
    return random.uniform(n-intensity, n+intensity)

# Setting 16:9 ratio size for the window
size = 60
window_width = 16*size
window_height = 9*size

window = pyglet.window.Window(window_width, window_height, "Perlin Noise") # Initialising window

batch = pyglet.graphics.Batch() # Initialising graphics

perlin_intensity_lable = pyglet.text.Label('Perlin Intensity: 21',
                            font_size=20,
                            x=10, y=window.height-10,
                            anchor_x='left', anchor_y='top')

perlin_density_lable = pyglet.text.Label('Perlin Density: 100',
                            font_size=20,
                            x=window.width-10, y=window.height-10,
                            anchor_x='right', anchor_y='top')

# Window event
@window.event
def on_draw():
    window.clear()
    batch.draw()
    perlin_intensity_lable.draw()
    perlin_density_lable.draw()

pause = False # This variable is used by the program to know when to pause

@window.event
def on_key_release(symbol, modifiers):
    global pause
    # Checking if space was released
    if symbol == pyglet.window.key.SPACE:
        # Pausing if not paused and starting if paused
        if pause:
            pause = False
        else:
            pause = True

number_of_lines = 100 # This determines the number of lines that the chart will be created with (Can experiment with)
line_size = int(window.width/number_of_lines) # This determines the size of the lines according to the window width and the number of lines
lines = [] # This will store the lines
init_y = int(window.height/2) # This is the initial y position for the first line
y = init_y
x = line_size

perlin_intensity = 21

# Changing perlin values when specific buttons are pressed
@window.event
def on_key_press(symbol, modifiers):
    global perlin_intensity, number_of_lines, line_size
    if symbol == pyglet.window.key.UP:
        perlin_intensity += 1

        perlin_intensity_lable.text = f'Perlin Intensity: {perlin_intensity}'
    elif symbol == pyglet.window.key.DOWN:
        perlin_intensity -= 1

        perlin_intensity_lable.text = f'Perlin Intensity: {perlin_intensity}'
    elif symbol == pyglet.window.key.RIGHT:
        number_of_lines += 1
        line_size = int(window.width/number_of_lines)

        perlin_density_lable.text = f'Perlin Density: {number_of_lines}'
    elif symbol == pyglet.window.key.LEFT:
        number_of_lines -= 1
        line_size = int(window.width/number_of_lines)
        
        perlin_density_lable.text = f'Perlin Density: {number_of_lines}'

def logic(delta_time):
    if not pause:
        global y
        global x

        old_y = y
        y = int(perlin_noise(y, perlin_intensity)) # Can experiment with the intensity

        # Not letting the chart go of the window
        if y < 0 or y > window.height:
            y = init_y
        
        # Adding the new line to the lines list after assigning values
        lines.append(pyglet.shapes.Line(x-line_size, old_y, x, y, 2,  (20, 148, 20), batch=batch))

        x += line_size

        # Deleteing and starting a new cahrt after reaching the end of the number of lines
        if len(lines) == number_of_lines+15:
            lines.clear()
            y = init_y
            x = line_size

# this runs the logic function every frame
pyglet.clock.schedule(logic)

pyglet.app.run()
