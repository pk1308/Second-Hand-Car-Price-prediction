import logging as lg
from datetime import datetime
import os
from SRC.utils import constants as CN





def APP_Logger(name, level="DEBUG" ):
    logger = lg.getLogger(name)
    FILE_NAME = f"log_{name}.log"
    LOG_FILE = os.path.join(CN.LOG_DIR, FILE_NAME)
    logger.setLevel(lg.DEBUG)
    level = level
    # Creating Formatters
    format = lg.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    # Creating Handlers
    file_handler = lg.FileHandler(LOG_FILE)

    # Adding Formatters to Handlers
    file_handler.setFormatter(format)
    # Adding Handlers to logger
    logger.addHandler(file_handler)
    
    stream_handler = lg.StreamHandler()
    stream_handler.setLevel(lg.INFO)
    logger.addHandler(stream_handler)
    return logger
