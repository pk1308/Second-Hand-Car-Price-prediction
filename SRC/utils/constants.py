import os 
from datetime import datetime
import logging as lg
from re import TEMPLATE
from SRC.utils.logger import APP_Logger


lg = APP_Logger(os.path.basename(__file__))

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d')}"
lg.debug(f"Current Time Stamp: {CURRENT_TIME_STAMP}")

ROOT_DIR = os.getcwd()
lg.debug(f"Root Directory: {ROOT_DIR}")

TEMPLATE_DIR = os.path.join(ROOT_DIR, "templates")
os.makedirs(TEMPLATE_DIR, exist_ok=True)

# Artifacts Directory 
ARTIFACTS = os.path.join(ROOT_DIR,"Artifacts")
os.makedirs(ARTIFACTS, exist_ok=True)


ARTIFACTS_DIR = os.path.join(ARTIFACTS, CURRENT_TIME_STAMP)
os.makedirs(ARTIFACTS_DIR , exist_ok = True)
lg.debug(f"Artifacts Directory: {ARTIFACTS_DIR}")


LOG_DIR = os.path.join(ARTIFACTS_DIR, "LOGS")
os.makedirs(LOG_DIR, exist_ok=True)

# dump Directory
DUMP_DIR = os.path.join(ARTIFACTS_DIR, 'DATA_DUMP')
os.makedirs(DUMP_DIR, exist_ok=True)

# Raw DATA DIR
RAW_DATA_DIR = os.path.join(ARTIFACTS_DIR ,"RAW_DATA")
os.makedirs(RAW_DATA_DIR, exist_ok = True)
lg.debug(f"Raw Data Directory: {RAW_DATA_DIR}")

# PROCEEDED DATA PATH
PROCEEDED_DATA_DIR = os.path.join(ARTIFACTS_DIR ,"PROCCESED_DATA")
os.makedirs(PROCEEDED_DATA_DIR , exist_ok = True)
lg.debug(f"Proceeded Data Directory: {PROCEEDED_DATA_DIR}")

#PREPROCESSING_DATA DIR 
PREPROCESSING_DATA_DIR = os.path.join(ARTIFACTS_DIR ,"PREPROCESSING_DIR")
os.makedirs(PREPROCESSING_DATA_DIR , exist_ok = True)
lg.debug(f"Preprocessing Data Directory: {PREPROCESSING_DATA_DIR}")


# IMPUTER DIR
IMPUTER_DIR = os.path.join(ARTIFACTS_DIR ,"IMPUTER_DIR")
os.makedirs(IMPUTER_DIR , exist_ok = True)
lg.debug(f"Imputer Directory: {IMPUTER_DIR}")

#SCALER DIR
SCALER_DIR = os.path.join(ARTIFACTS_DIR ,"SCALER_DIR")
os.makedirs(SCALER_DIR , exist_ok = True)
lg.debug(f"Scaler Directory: {SCALER_DIR}")

# MODEL_ DIR
MODEL_DIR = os.path.join(ARTIFACTS_DIR ,"MODEL_DIR")
os.makedirs(MODEL_DIR , exist_ok = True)
lg.debug(f"Model Directory: {MODEL_DIR}")

DUMP_DIR = os.path.join(ARTIFACTS_DIR, 'DATA_DUMP')
os.makedirs(DUMP_DIR, exist_ok=True)


#File Names 
# DATA url 
RAW_DATA_URL = 'https://raw.githubusercontent.com/pk1308/datasets/master/secondhand%20car/data_train.csv'
lg.debug(f"Raw Data URL: {RAW_DATA_URL}")

TEST_DATA_URL = 'https://raw.githubusercontent.com/pk1308/datasets/master/secondhand%20car/data_test.csv'
lg.debug(f"Test Data URL: {TEST_DATA_URL}")


