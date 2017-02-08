# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

im = cv2.imread("test.jpg",1)
#im = cv2.cvtColor(im, cv2.COLOR_GRAY2RGB)


print(im.shape)
#cv2.imshow("Show",im)
#cv2.waitKey(0)
#cv2.destroyAllWindows()