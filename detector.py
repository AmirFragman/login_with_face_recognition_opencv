import cv2 as cv

def face_detector():
    cap = cv.VideoCapture(0)
    cascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml") 

    while True:
      ret, frame = cap.read()

      if not ret:
        break   

      grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
      faces = cascade.detectMultiScale(grayscale, 1.1, 5)
  
      for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 1)

      cv.imshow('frame', frame)

      key = cv.waitKey(1)
      if key == ord('q'):
        break

    cap.release()
    cv.destroyAllWindows()



def main():
  face_detector()

if __name__ == '__main__':
  main()