# Main File
from picamera import PiCamera
import main
import time
import os

def identify_mask():
    #TODO: @Shinjini
    return False

def warn_user():
    #TODO: Pawan
    pass

# camera = PiCamera()
image_file = "capture.png"
cmd = "raspistill --timeout 100 -o Desktop/capture.png"
while True:
    # camera.capture(image_file)
    os.system(cmd)
    door_moving = main.get_movement()
    mask_on = identify_mask()
    if not mask_on and door_moving:
        warn_user()
    print(door_moving)
    time.sleep(0.3)