import time
import cv2 as cv
import os

# Create output folder if it doesn't exist
def video_to_pic(name):
    os.makedirs(f'pic_data/{name}', exist_ok=True)
    gray = os.makedirs(f'pic_data/{name}/gray', exist_ok=True)
    cam = cv.VideoCapture(0) 

    frame_num = 0

    while True:
      ret, frame = cam.read()

      if not ret:
        break

      cv.imshow("video frame", frame)
      grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

  # Construct output filename and path
      pic_name = f'{name}/{frame_num}.jpg'
      save_file = os.path.join('pic_data', pic_name)
      gray_pic_name = f'{name}/gray/{frame_num}.jpg'
      save_gray = os.path.join('pic_data', gray_pic_name)

  # Save frame to disk
      cv.imwrite(save_file, frame) 
      cv.imwrite(save_gray, grayscale)
      time.sleep(0.5)
      frame_num += 1

  # Check for exit keys    
      key = cv.waitKey(1)
      if frame_num == 30 or key == ord("q"):
        break

    cam.release()
    cv.destroyAllWindows()



def main():
  name = "amir"
  video_to_pic(name)

if __name__ == '__main__':
  main()
