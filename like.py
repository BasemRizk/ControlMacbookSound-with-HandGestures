import time
import cv2
import applescript

#Check if the thumbs up stays for 1 sec perform the applescript
def volume_up(thumbs_up, volume_start_time, img):
    if not thumbs_up:
        volume_start_time = time.time()
    thumbs_up = True
    if time.time() - volume_start_time >= 1:
        cv2.putText(img, ' Volume Up', (15, 200), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255))
        applescript.run('set volume output volume (output volume of (get volume settings) + 10)')
        volume_start_time = time.time()
    return thumbs_up, volume_start_time
#Check if the thumbs down stays for 1 sec perform the applescript
def volume_down(thumbs_down, volume_start_time, img):
    if not thumbs_down:
        volume_start_time = time.time()
    thumbs_down = True
    if time.time() - volume_start_time >= 1:
        cv2.putText(img, ' Volume Down', (15, 200), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255))
        applescript.run('set volume output volume (output volume of (get volume settings) - 10)')
        volume_start_time = time.time()
    return thumbs_down, volume_start_time
