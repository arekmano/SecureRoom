import logging
import ConfigParser
from logging.handlers import TimedRotatingFileHandler
class Config():

  @classmethod
  def setup_logger(cls):
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    file_handler = TimedRotatingFileHandler('log.csv')
    file_handler.setLevel(logging.DEBUG)
    frmt = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
    file_handler.setFormatter(frmt)
    log.addHandler(file_handler)

  @classmethod
  def read_config_file(cls):
    config = ConfigParser.ConfigParser()
    config.read('config')
    cls.access_token = config.get('DROPBOX', 'access_token')
    cls.account_sid = config.get('TWILIO', 'account_sid')
    cls.auth_token = config.get('TWILIO', 'auth_token')
    cls.to_phone_number = config.get('TWILIO', 'to_phone_number')
    cls.from_phone_number = config.get('TWILIO', 'from_phone_number')

  @classmethod
  def setup(cls):
    cls.setup_logger()
    cls.read_config_file()
