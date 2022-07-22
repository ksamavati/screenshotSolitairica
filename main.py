import pyautogui
import time


def grab_one_screen(fileIndex):
    bounds = []
    last_call = False

    firstloop = True
    for box in pyautogui.locateAllOnScreen('./FindThese/topedge.png'):  # returns [0=left,1=top,2=width,3=height]
        if index == 0 and box[1] > 207:  # If the first topedge found is positioned lower than usual, it's lastcall
            last_call = True
        else:
            index = 1
        bounds.append([box[0], box[1], box[2], box[3]])  # We pull each index individually to cast Box obj to list

    bounds.sort(key=lambda x: x[0])
    bounds.sort(key=lambda x: x[1])

    bottoms = []
    index = 0
    for box in pyautogui.locateAllOnScreen('./FindThese/bottomedge.png'):  # returns [left, top, width, height]
        bottoms.append([box[0], box[1], box[2], box[3]])  # We pull each index individually to cast Box obj to list
        index += 1

    # sorted(bottoms, key=itemgetter)

    # index = 0
    # for bottoms in pyautogui.locateAllOnScreen('./FindThese/bottomedge.png'):
    #     bounds[index][3] = (bottoms[1] + bottoms[3]) - bounds[index][1]
    #     index += 1

    index = 0
    while bounds[index][3] > 10:  # While height is greater than 10px, aka bottom visible
        pyautogui.screenshot('./Spells/Spell_' + str(fileIndex).zfill(3) + ".png", region=bounds[index])
        index += 1
        fileIndex += 1

    pyautogui.moveTo(bounds[index][0], bounds[index][1])
    pyautogui.mouseDown()
    time.sleep(0.05)
    pyautogui.moveTo(bounds[index][0], 147, 1)
    time.sleep(0.05)
    pyautogui.mouseUp()

    # pyautogui.dragTo(bounds[index][0], 202, 0.75, button='left')

    if not lastcall:
        grab_one_screen(fileIndex)


grab_one_screen(1)
