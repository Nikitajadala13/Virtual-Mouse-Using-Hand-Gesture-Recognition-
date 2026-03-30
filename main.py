import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import time

# Hand Detector
class HandDetector:
    def __init__(self, mode=False, maxHands=1, detectionCon=0.8, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=self.mode,
            max_num_hands=self.maxHands,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackCon
        )
        self.mpDraw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def find_position(self, img, handNo=0, draw=True):
        lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 6, (255, 0, 255), cv2.FILLED)
        return lmList

    def fingers_up(self, lmList):
        fingers = []
        fingers.append(1 if lmList[4][1] < lmList[3][1] else 0)  # Thumb
        for id in [8, 12, 16, 20]:
            fingers.append(1 if lmList[id][2] < lmList[id - 2][2] else 0)
        return fingers

# Initialize
cap = cv2.VideoCapture(0)
detector = HandDetector()
screen_width, screen_height = pyautogui.size()
frame_width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

prev_x, prev_y = 0, 0
smoothing = 5
last_screenshot_time = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    if not success:
        break

    img = detector.find_hands(img)
    lmList = detector.find_position(img, draw=False)

    if lmList:
        fingers = detector.fingers_up(lmList)
        index_finger = lmList[8]

        # Move mouse: Index only
        if fingers == [0, 1, 0, 0, 0]:
            x, y = index_finger[1], index_finger[2]
            curr_x = np.interp(x, [0, frame_width], [0, screen_width])
            curr_y = np.interp(y, [0, frame_height], [0, screen_height])
            screen_x = prev_x + (curr_x - prev_x) / smoothing
            screen_y = prev_y + (curr_y - prev_y) / smoothing
            pyautogui.moveTo(screen_x, screen_y, duration=0.1)
            prev_x, prev_y = screen_x, screen_y

        # Left click: Index + Middle
        elif fingers == [0, 1, 1, 0, 0]:
            pyautogui.click()
            time.sleep(0.3)

        # Right click: Middle only
        elif fingers == [0, 0, 1, 0, 0]:
            pyautogui.rightClick()
            time.sleep(0.3)

        # Double Click: Index + Middle + Ring
        elif fingers == [0, 1, 1, 1, 0]:
            pyautogui.doubleClick()
            time.sleep(0.3)

        # Scroll up: Index + Ring
        elif fingers == [0, 1, 0, 1, 0]:
            pyautogui.scroll(20)
            time.sleep(0.2)

        # Scroll down: Middle + Ring
        elif fingers == [0, 0, 1, 1, 0]:
            pyautogui.scroll(-20)
            time.sleep(0.2)

        # Drag: Thumb + Index
        elif fingers == [1, 1, 0, 0, 0]:
            pyautogui.mouseDown()

        # Drop: Index + Pinky
        elif fingers == [0, 1, 0, 0, 1]:
            pyautogui.mouseUp()

        # Screenshot: All fingers
        elif fingers == [0, 0, 0, 0, 0]:
            if time.time() - last_screenshot_time > 2:
                screenshot = pyautogui.screenshot()
                screenshot.save(f"screenshot_{int(time.time())}.png")
                last_screenshot_time = time.time()

    # Display Screenshot Saved Message
    if time.time() - last_screenshot_time < 2:
        cv2.putText(img, 'Screenshot Saved!', (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("Virtual Mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
