from pywinauto import Application
import pyautogui
import cv2
import numpy as np

app = Application(backend="uia").connect(title='Minesweeper')

main_window = app.window(title='Minesweeper')

if main_window == None:
    print("Minesweeper is not running")
    exit()
else:
    print("Minesweeper is running")

# Przygotowanie obrazu źródłowego i szukanego wzorca
screenshot = pyautogui.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
template = cv2.imread('textures/tile_hidden.png', cv2.IMREAD_UNCHANGED)

found_scale = None
# Sprawdzenie różnych skal
for scale in np.linspace(0.2, 3.0, 20)[::-1]:
    resized_screenshot = cv2.resize(screenshot, (int(screenshot.shape[1] * scale), int(screenshot.shape[0] * scale)))
    result = cv2.matchTemplate(resized_screenshot, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    if max_val > 0.8:
        print("Found match with scale ", scale)
        print("Position (left={0}, top={1}), Size (width={2}, height={3})".format(max_loc[0], max_loc[1], template.shape[1], template.shape[0]))
        found_scale = scale
        break

if found_scale is not None:
    locations = np.where(result >= 0.8)
    for pt in zip(*locations[::-1]):
        print("Match at Position (left={0}, top={1}), Size (width={2}, height={3})".format(pt[0], pt[1], template.shape[1], template.shape[0]))
