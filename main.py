import logging
from monitor import Monitor
from config import Config

Config.setup()
Monitor.monitor()
