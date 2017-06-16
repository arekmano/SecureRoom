import logging
import time
import cv2
from webcam import Webcam

class Monitor(object):
  log = logging.getLogger('Monitor')
  baseline = 1
  armDelay = 1

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
      # k = cv2.waitKey(30) & 0xff
      # if k != 255:
      #   print(k)
      #   Monitor.log.info('=== Exit signal received ===')
      #   Monitor.log.info('=== Shutting Down ===.')
      #   break

  ##
  # Delay for Monitor.armDelay seconds,
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
      current_baseline += 1

  @classmethod
  def report_image(cls, img):
    cls.log.info('Intruder detected!!')
    file_name = 'detections/intruder' + str(int(time.time())) + '.png'
    cv2.imwrite(file_name, img)
