import logging
from monitor import Monitor

lgr = logging.getLogger()
lgr.setLevel(logging.DEBUG)
fh = logging.FileHandler('log.csv')
fh.setLevel(logging.DEBUG)
frmt = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
fh.setFormatter(frmt)
lgr.addHandler(fh)

Monitor.monitor()