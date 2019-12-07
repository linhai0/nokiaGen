import os
import cv2

import numpy as np

from matplotlib import pyplot as plt

def test(image_path):

    img = cv2.read(image_path)
    img1 = cv2.rotate(img, 20)

    cv2.imshow('nokia', img1)
    cv2.waitKey()
    cv2.destroyAllWindows()





if __name__ == "__main__":
    img = test()
    # plt.imshow(img)