import logging
import os

def debugOn():
    debugOn = os.getenv("DEBUG")

    if debugOn:
        return True

    return False

class Logger():

    def __init__(self, level, data, logfile=None, stdout=True):
        self.data    = data
        self.level   = level
        self.logfile = logfile
        self.stdout  = stdout
        self.logger  = logging.getLogger(__name__)

    def log(self):
        logRecord = f"{self.level}: {self.data}"

        if self.level == "WARNING":
            self.logger.warning(logRecord)

        if self.level == "INFO":
            self.logger.info(logRecord)

        if self.level == "ERROR":
            self.logger.error(logRecord)

        if self.level == "CRITICAL":
            self.logger.critical(logRecord)

        if debugOn() and self.level == "DEBUG":
            self.logger.debug(logRecord)

        if self.logfile:
            with open(self.logfile, "a") as log:
                log.writelines(logRecord + "\n")