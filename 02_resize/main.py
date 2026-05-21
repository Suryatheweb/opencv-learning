import cv2

img = cv2.imread("../test.jpeg")

if img is None:
    print("no image found")
    exit()

resized = cv2.resize(img,(400,800))

cv2.imshow("original", img)
cv2.imshow("resized", resized)

cv2.waitKey(0) ##This line tells OpenCV:“Keep the window open until the user presses a key.”Without it, the window appears for a fraction of a second and closes immediately because the script finishes.
cv2.destroyAllWindows() ##This line tells OpenCV:“Close every window that was opened by cv2.imshow.”If you don’t call it, the window may stay open or freeze.


