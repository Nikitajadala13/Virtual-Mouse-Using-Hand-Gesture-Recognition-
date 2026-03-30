import numpy as np
import pyautogui
import cv2

def map_coordinates(x, y, frame_w, frame_h, screen_w, screen_h, prev_x, prev_y, smoothing=5):
    x = np.interp(x, [0, frame_w], [0, screen_w])
    y = np.interp(y, [0, frame_h], [0, screen_h])
    curr_x = prev_x + (x - prev_x) / smoothing
    curr_y = prev_y + (y - prev_y) / smoothing
    return curr_x, curr_y, curr_x, curr_y

def take_screenshot(path="screenshot.png"):
    screenshot = pyautogui.screenshot()
    screenshot.save(path)

def show_screenshot_message(img):
    cv2.putText(img, "Screenshot Taken!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 3)
    return img
