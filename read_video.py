import cv2 as cv

capture = cv.VideoCapture(0)

capture.set(cv.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

while True:
  ret, frame = capture.read()
  
  if ret == False:
    continue
  
  cv.imshow("video frame", frame)
  key = cv.waitKey(1)

  if key == ord("q"):
    break

capture.release()
cv.destroyAllWindows()
