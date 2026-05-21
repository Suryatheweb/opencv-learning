import cv2

##cv2.VideoCapture(0)-open your default webcam.1-for second camera,2-for third camera
cap = cv2.VideoCapture(0)


##cap.isOpened()- Check camera
if not cap.isOpened():
    print("cannot open camer")
    exit()


##ret = True/False,True → frame captured successfully,False → camera failed
while True:
    ret,frame =cap.read()

    if  ret == False:
        print("faild to grab the frame")
        break
    else:
        cv2.imshow("webcam",frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()




