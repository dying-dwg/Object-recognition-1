import cv2 as cv
import time
import numpy as np
from matplotlib import pyplot as plt
import os

def FindPosImage(standard, research, mode):

    global cor_field
    result = cv.matchTemplate(standard, research, cv.TM_CCORR_NORMED)
    # + приведение к общей яркости
    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)

    w, h = research.shape[:-1:] # Вернуть форму массива
    rasmer = (maxLoc[0] + w, maxLoc[1] + h)

    print("Вверхний левый край:", rasmer)
    print("Нижний правый край:", maxLoc)
    print("=====")

    # Draw a rectangle of black color of thickness 5 px
    draw = cv.rectangle(standard, maxLoc, rasmer, 0, 5)

    plt.figure()
    plt.imshow(result, clim=(0.6, 0.9))
    plt.colorbar()
    plt.savefig('D:\\Developer\\Python\\AOZDlab1\\Result\\result' + str(cor_field) + '.png', bbox_inches='tight')
    cor_field += 1

  # Displaying the image
    if mode == 1:
        cv.namedWindow('Find', cv.WINDOW_KEEPRATIO)
        cv.imshow('Find', draw)
        cv.resizeWindow('Find', 800, 800)
        cv.waitKey(0)
        cv.destroyAllWindows()


def RotateImage(standard, research):

    rotation_angleS = np.arange(-10, 10, 2)
    rotation_angleR = reversed(rotation_angleS)

    wS, hS = standard.shape[:-1:]
    wR, hR = research.shape[:-1:]

    centerS = (wS/2, hS/2)
    centerR = (wR/2, hR/2)

    matrix_S = map(lambda angle: cv.getRotationMatrix2D(centerS, angle, 0.8), rotation_angleS)
    rotated_S = map(lambda angles: cv.warpAffine(standard, angles, (wS, hS)), matrix_S)
    matrix_R = map(lambda angle: cv.getRotationMatrix2D(centerR, angle, 0.8), rotation_angleR)
    rotated_R = map(lambda angles: cv.warpAffine(standard, angles, (wR, hR)), matrix_R)

    for i, j in zip(rotated_S, rotated_R):
        FindPosImage(i, j, 0)


def ScaleImage(standard, research):

    scaling = np.arange(0.9, 1.1, 0.025)

    wS, hS = standard.shape[:-1:]
    wR, hR = research.shape[:-1:]

    shapeS = [(int(wS*i), int(hS*i)) for i in scaling]
    scaleS = map(lambda scale: cv.resize(standard, scale), shapeS)
    shapeR = [(int(wR*i), int(hR*i)) for i in scaling]
    scaleR = map(lambda scales: cv.resize(research, scales), shapeR)

    for i, j in zip(scaleS, scaleR):
        FindPosImage(i, j, 0)



def ShowImage():
    pictures = os.listdir('Result')
    pic_box = plt.figure(figsize=(16, 4))
    # Поочередно считываем в переменную picture имя изображения из списка pictures. В переменную i записываем номер итерации
    for i, picture in enumerate(pictures):
        # считываем изображение в picture
        picture = cv.imread('Result/' + picture)
        # добавляем ячейку в pix_box для вывода текущего изображения
        pic_box.add_subplot(4, 5, i + 1)
        plt.imshow(picture)
        # отключаем отображение осей
        plt.axis('off')
    # выводим все созданные фигуры на экран
    plt.show()


if __name__ == '__main__':
    cor_field = 0

    print("Open: \n1. own_2.jpg\n2. foreign_2.jpg\n")
    key = int(input("Enter: "))

    start_time = time.time()

    mainIM = cv.imread("main.jpg")
    ownIM = cv.imread("own_2.jpg")
    foreignIM = cv.imread("foreign_2.jpg")
    if ((mainIM is None) or
            (ownIM is None) or
                (foreignIM is None)):
        print("Check path images.")
        exit(0)

    if key == 1:
        FindPosImage(mainIM, ownIM, 1)
        RotateImage(mainIM, ownIM)
        ScaleImage(mainIM, ownIM)
    elif key == 2:
        FindPosImage(mainIM, foreignIM, 1)
        RotateImage(mainIM, foreignIM)
        ScaleImage(mainIM, foreignIM)
    else:
        print("Enter 1 / 2.")

    print("--- Время работы: %s ---" % (time.time() - start_time))
    ShowImage()
