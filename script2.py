import cv2
import numpy as np
import datetime

# Create a black image
blank = np.ones((1080,1920,3), np.uint8)
blank *= 255


img = cv2.imread("palette.png")
crop_img = img[765:1025, 1:1850]

# cv2.imshow("cropped", blank)
#  cv2.waitKey(0)

img2 = cv2.imread("temp.png")

crop_img2 = crop_img

blank[0:820, 0:1920] = img2

blank[820:1080, 0:1849] = crop_img

file_name = str(datetime.datetime.now().time()) + ".png"

print(file_name[-9:])

cv2.imwrite("./export/" + file_name[-13:], blank)

