import cv2

img = cv2.imread("screengrab.png")
crop_img = img[130:950]

# cv2.imshow("cropped", crop_img)

cv2.imwrite("temp.png", crop_img)

