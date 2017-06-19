from twilio.rest import Client
from dropbox import Dropbox
from config import Config
import logging
import time

class Reporter(object):
  log = logging.getLogger('Reporter')
  last_sms_time = 0
  sms_rate = 300 # Send a text message at most once every 'sms_rate' seconds

  @classmethod
  def send_sms(cls, filename):
    client = Client(Config.account_sid, Config.auth_token)
    client.api.account.messages.create(to=Config.to_phone_number,
                                       from_=Config.from_phone_number,
                                       body='Intruder Detected! File was uploaded'\
                                            ' to Dropbox under: ' + filename)
    cls.log.info('Sent an SMS for file "' + filename + '".')

  @classmethod
  def upload_to_dropbox(cls, filename):
    file = open(filename, 'rb')
    dropbox_client = Dropbox(Config.access_token)
    dropbox_client.files_upload(file.read(), '/' + filename)
    cls.log.info('Uploaded "' + filename + '"file to Dropbox.')

  @classmethod
  def report(cls, filename):
    cls.upload_to_dropbox(filename)
    current_time = int(time.time())
    if current_time - cls.last_sms_time > cls.sms_rate:
      cls.log.debug('Current time is outside of SMS NO SEND window.')
      cls.log.debug('Sending an SMS.')
      cls.last_sms_time = current_time
      cls.send_sms(filename)
    else:
      cls.log.debug('Current time is within SMS NO SEND window.')
