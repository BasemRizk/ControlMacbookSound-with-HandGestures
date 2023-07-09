import time
import cv2
import applescript

def volume_up(thumbs_up, volume_start_time, img):
    if not thumbs_up:
        volume_start_time = time.time()
    thumbs_up = True
    if time.time() - volume_start_time >= 1:
        cv2.putText(img, ' Volume Up', (15, 200), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255))
        applescript.run('set volume output volume (output volume of (get volume settings) + 10)')
        volume_start_time = time.time()
    return thumbs_up, volume_start_time
def volume_down(thumbs_down, volume_start_time, img):
    if not thumbs_down:
        volume_start_time = time.time()
    thumbs_down = True
    if time.time() - volume_start_time >= 1:
        cv2.putText(img, ' Volume Down', (15, 200), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255))
        applescript.run('set volume output volume (output volume of (get volume settings) - 10)')
        volume_start_time = time.time()
    return thumbs_down, volume_start_time