import numpy as np
import cv2 as cv

# cap.read() returns a bool (True/False). If the frame is read correctly, it will be True
cap = cv.VideoCapture(0)

if not cap.isOpened():
 print("Cannot open camera")
 exit()


while True:
  # Capture frame-by-frame
  ret, frame = cap.read()

  # if frame is read correctly ret is True
  if not ret:
    print("Can't receive frame, Exiting ...")
    break

  # Our operations on the frame come here
  gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

  # Display the resulting frame
  cv.imshow('frame', gray)

  if cv.waitKey(1) == ord('q'):
    cv.imwrite("pic_data/stream_end.jpg", frame)
    cv.imwrite("pic_data/gray_stream_end.jpg", gray)
    break


# When everything done, release the capture
cap.release()
cv.destroyAllWindows()