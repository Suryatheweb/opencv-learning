import cv2

img = cv2.imread("test.jpeg") 

if img is None:
    print("Image not found!")
else:
    cv2.imshow("My Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
