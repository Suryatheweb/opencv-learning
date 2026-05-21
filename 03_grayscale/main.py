import cv2
img = cv2.imread("../test.jpeg")

if img is None:
    print("image not found")
    exit()

gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
##converts the image from BGR → Grayscale.They are easier to process for:edge detection,thresholding,face detection,object tracking
cv2.imshow("original", img)
cv2.imshow("grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows

