import cv2
import numpy as np
import time

class FaceSensor(object):
  face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
  profileface_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
  eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

  def show_webcam(self, mirror=False):
    number = 0
    while True:
      time.sleep(2)
      cam = cv2.VideoCapture(0)
      _, img = cam.read()
      cam.release()
      if mirror:
        img = cv2.flip(img, 1)
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
      if len(faces) > 0:
        print('Faces found. Saving')
        self.saveImage(img)
      else:
        print('No faces found.')
      for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = self.eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
          cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        profilefaces = self.profileface_cascade.detectMultiScale(gray)
        for (ex,ey,ew,eh) in profilefaces:
          cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)


      cv2.imshow('img', img)
      if cv2.waitKey(1) == 27:
        break  # esc to quit
    cv2.destroyAllWindows()

  def saveImage(self, img):
    filename = 'face-' + time.strftime('%Y_%b_%d_%H_%M_%S', time.localtime(time.time())) + '.png'
    print(filename)
    cv2.imwrite('captures/' + filename, img)

if __name__ == '__main__':
  FaceSensor().show_webcam(mirror=True)