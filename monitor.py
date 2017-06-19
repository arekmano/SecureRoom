import logging
import time
import cv2
import os
from webcam import Webcam
from reporter import Reporter

class Monitor(object):
  log = logging.getLogger('Monitor')
  baseline = 10 # Take 10 samples as a baseline before detecting intrusions
  armDelay = 10 # Wait 10 seconds; time to leave room

  @classmethod
  def monitor(cls):
    cls.delay()
    cls.prepare()

    cls.log.info('System is now armed')

    while 1:
      img = Webcam.sample_webcam()
      if img is not None:
        cls.report_image(img)
      time.sleep(1)
      # TODO: add abort signal

  ##
  # Delay for armDelay seconds,
  # so that I can leave the room
  ##
  @classmethod
  def delay(cls):
    run_time = 0
    while run_time < cls.armDelay:
      cls.log.info('Getting ready to Arm.')
      time.sleep(1)
      run_time += 1

  @classmethod
  def prepare(cls):
    current_baseline = 0
    while cls.baseline > current_baseline:
      Webcam.baseline()
      time.sleep(1)
      current_baseline += 1

  @classmethod
  def report_image(cls, img):
    cls.log.info('Intruder detected!!')
    filename = 'detections/intruder' + str(int(time.time())) + '.png'
    cv2.imwrite(filename, img)
    Reporter.report(filename)
    os.remove(filename)

