import PIL.Image


def crop():
    coordinates = []
    (left, upper, right, lower) = (600, 150, 700, 250)
    im = PIL.Image.open('screenshot/screenshot.png')
    for i in range(1, 4):
        for j in range(1, 4):
            im_crop = im.crop((left, upper, right, lower))
            #coordinate = (left+50, upper+50)
            #coordinates.append(coordinate)
            im_crop.save('result/' + str(i) + '.' + str(j) + '.png')
            (left, upper,) = (left + 100, upper)
            (right, lower) = (left + 100, upper + 100)
        (left, upper,) = (600, upper + 105)
        (right, lower) = (left + 100, upper + 100)

    (left, upper, right, lower) = (605, 595, 705, 695)
    for i in range(1, 3):
        for j in range(1, 8):
            im_crop = im.crop((left, upper, right, lower))
            coordinate = (left + 50, upper + 50)
            coordinates.append(coordinate)
            im_crop.save('result/variant.' + str(i) + '.' + str(j) + '.png')
            (left, upper,) = (left + 100, upper)
            (right, lower) = (left + 100, upper + 100)
        (left, upper,) = (605, upper + 105)
        (right, lower) = (left + 100, upper + 100)
    return coordinates
