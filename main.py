import keyboard
import pyautogui

import Croper
import FindSample


def main():
    keyboard.wait('q')
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot/screenshot.png')
    coordinatesTask = [(1050, 200), (1150, 200), (1250, 200), (1050, 305), (1150, 305), (1250, 305), (1050, 410),
                       (1150, 410), (1250, 410)]
    coordinatesVariant = [(655, 645), (755, 645), (855, 645), (955, 645), (1055, 645), (1155, 645), (1255, 645),
                          (655, 750),
                          (755, 750), (855, 750), (955, 750), (1055, 750), (1155, 750), (1255, 750)]
    Croper.crop()
    log = []
    parts_array = FindSample.findSample()
    print(parts_array)
    parts_variant_array = FindSample.findVariantSample()
    print(parts_variant_array)
    for i in range(0, 9):
        part = parts_array[i]
        for j in range(0, 15):
            if part == parts_variant_array[j]:
                log.append('Finded ' + parts_variant_array[j] + ' simillar to '+part+' index of part = ' + str(i)
                           + ' index of finded ' + str(j) + '\n')
                parts_variant_array[j] = 'empty'
                pyautogui.moveTo(*coordinatesVariant[j])
                pyautogui.dragTo(*coordinatesTask[i], 0.11)
                break

    with open('file.txt', 'w') as f:
        f.write('\n'.join(log))
    pyautogui.click(960, 930)
    main()


main()
