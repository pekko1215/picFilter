import cv2

filename = "test.jpg"
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
cv2.imshow('window title', img)
cv2.waitKey(0)
cv2.destroyAllWindows()