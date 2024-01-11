import Parts
import cv2
import numpy as np


def findSample():
    template1 = cv2.imread('source/scrap.png', 0)
    template2 = cv2.imread('source/gear.png', 0)
    template3 = cv2.imread('source/wood.png', 0)
    template4 = cv2.imread('source/tube.png', 0)
    parts_array = []
    for i in range(1, 4):
        for j in range(1, 4):
            # Загрузите изображение, в котором нужно найти шаблон
            image = cv2.imread('result/' + str(i) + '.' + str(j) + '.png', 0)

            # Найдите шаблон на изображении
            result1 = cv2.matchTemplate(image, template1, cv2.TM_CCOEFF_NORMED)
            result2 = cv2.matchTemplate(image, template2, cv2.TM_CCOEFF_NORMED)
            result3 = cv2.matchTemplate(image, template3, cv2.TM_CCOEFF_NORMED)
            result4 = cv2.matchTemplate(image, template4, cv2.TM_CCOEFF_NORMED)

            # Получите координаты найденного шаблона
            threshold = 0.7  # пороговое значение
            y1, x1 = np.unravel_index(np.argmax(result1), result1.shape) if np.max(result1) > threshold else (
                None, None)
            y2, x2 = np.unravel_index(np.argmax(result2), result2.shape) if np.max(result2) > threshold else (
                None, None)
            y3, x3 = np.unravel_index(np.argmax(result3), result3.shape) if np.max(result3) > threshold else (
                None, None)
            y4, x4 = np.unravel_index(np.argmax(result4), result4.shape) if np.max(result4) > threshold else (
                None, None)

            if (x1 and y1):
                parts_array.append(Parts.Parts.Scrap.name)
            if (x2 and y2):
                parts_array.append(Parts.Parts.Gear.name)
            if (x3 and y3):
                parts_array.append(Parts.Parts.Wood.name)
            if (x4 and y4):
                parts_array.append(Parts.Parts.Tube.name)
    return parts_array

def findVariantSample():
    parts_variant_array = []
    template1 = cv2.imread('source/scrap.png', 0)
    template2 = cv2.imread('source/gear.png', 0)
    template3 = cv2.imread('source/wood.png', 0)
    template4 = cv2.imread('source/tube.png', 0)
    for i in range(1, 3):
        for j in range(1, 8):
            # Загрузите изображение, в котором нужно найти шаблон
            image = cv2.imread('result/variant.' + str(i) + '.' + str(j) + '.png', 0)

            # Найдите шаблон на изображении
            result1 = cv2.matchTemplate(image, template1, cv2.TM_CCOEFF_NORMED)
            result2 = cv2.matchTemplate(image, template2, cv2.TM_CCOEFF_NORMED)
            result3 = cv2.matchTemplate(image, template3, cv2.TM_CCOEFF_NORMED)
            result4 = cv2.matchTemplate(image, template4, cv2.TM_CCOEFF_NORMED)

            # Получите координаты найденного шаблона
            threshold = 0.75  # пороговое значение
            y1, x1 = np.unravel_index(np.argmax(result1), result1.shape) if np.max(result1) > threshold else (
            None, None)
            y2, x2 = np.unravel_index(np.argmax(result2), result2.shape) if np.max(result2) > threshold else (
            None, None)
            y3, x3 = np.unravel_index(np.argmax(result3), result3.shape) if np.max(result3) > threshold else (
            None, None)
            y4, x4 = np.unravel_index(np.argmax(result4), result4.shape) if np.max(result4) > threshold else (
            None, None)

            if (x1 and y1):
                parts_variant_array.append(Parts.Parts.Scrap.name)
            if (x2 and y2):
                parts_variant_array.append(Parts.Parts.Gear.name)
            if (x3 and y3):
                parts_variant_array.append(Parts.Parts.Wood.name)
            if (x4 and y4):
                parts_variant_array.append(Parts.Parts.Tube.name)
    return parts_variant_array