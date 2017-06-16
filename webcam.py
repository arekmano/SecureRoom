import logging
import time
import cv2
import numpy as np

class Webcam(object):
  log = logging.getLogger('Webcam')
  kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
  fgbg = cv2.createBackgroundSubtractorMOG2()
  threshold = 100000

  @classmethod
  def sample_webcam(cls):
    signal, img = cls.capture()
    if signal > cls.threshold:
      cls.log.debug('Intruder Detected. Signal level: ' + str(signal))
      return img
    else:
      cls.log.debug('All clear. Signal level: ' + str(signal))

  @classmethod
  def capture(cls):
    cam = cv2.VideoCapture(0)
    _, img = cam.read()
    cam.release()
    fgmask = cls.fgbg.apply(img)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, cls.kernel)
    return np.sum(fgmask), img

  @classmethod
  def baseline(cls):
    signal, _ = cls.capture()
    cls.log.debug('Baselining. Signal level: ' + str(signal))

