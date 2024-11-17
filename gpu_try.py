import pyglet
from pyglet.gl import *
import time
from pystray import Icon, MenuItem as Item, Menu
from PIL import Image, ImageDraw
import threading

# Create a minimized window to run the OpenGL task
window = pyglet.window.Window(visible=False)

def create_icon_image():
    # Create an icon image for the system tray
    image = Image.new('RGB', (64, 64), color=(0, 128, 255))
    d = ImageDraw.Draw(image)
    d.ellipse((16, 16, 48, 48), fill=(255, 0, 0))
    return image

@window.event
def on_draw():
    # Clear the screen to engage the GPU
    glClear(GL_COLOR_BUFFER_BIT)
    window.flip()

def run_gpu_task(dt):
    # Keep the GPU active by clearing the screen
    glClear(GL_COLOR_BUFFER_BIT)
    window.flip()

def setup_tray_icon():
    # Define exit function for the tray icon
    def on_exit(icon, item):
        pyglet.app.exit()  # Exit the pyglet event loop
        icon.stop()        # Remove the tray icon

    # Create the tray icon with an "Exit" option
    icon = Icon("GPU Task", icon=create_icon_image(), menu=Menu(Item("Exit", on_exit)))
    icon.title = "GPU Fixer Running"  # Set the tooltip text

    # Start the icon asynchronously so it doesn't block the main thread
    icon.run_detached()

# Set up the tray icon
setup_tray_icon()

# Schedule the GPU task and start the pyglet app loop
pyglet.clock.schedule_interval(run_gpu_task, 0.5)  # Adjust for desired GPU load
pyglet.app.run()
