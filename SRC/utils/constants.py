import os 
from datetime import datetime
import logging as lg
from re import TEMPLATE
from SRC.utils.logger import APP_Logger


lg = APP_Logger(os.path.basename(__file__))

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
lg.debug(f"Current Time Stamp: {CURRENT_TIME_STAMP}")

ROOT_DIR = os.getcwd()
lg.debug(f"Root Directory: {ROOT_DIR}")

TEMPLATE_DIR = os.path.join(ROOT_DIR, "templates")
os.makedirs(TEMPLATE_DIR, exist_ok=True)

# Atrificats Directory 
ARIFACTS_DIR = os.path.join(ROOT_DIR,"Artifacts")
os.makedirs(ARIFACTS_DIR , exist_ok = True)
lg.debug(f"Artifacts Directory: {ARIFACTS_DIR}")


LOG_DIR = os.path.join(ARIFACTS_DIR, "LOGS")
os.makedirs(LOG_DIR, exist_ok=True)

# dump Directory
DUMP_DIR = os.path.join(ARIFACTS_DIR, 'DATA_DUMP')
os.makedirs(DUMP_DIR, exist_ok=True)

# Raw DATA DIR
RAW_DATA_DIR = os.path.join(ARIFACTS_DIR ,"RAW_DATA")
os.makedirs(RAW_DATA_DIR, exist_ok = True)
lg.debug(f"Raw Data Directory: {RAW_DATA_DIR}")

# PROCCESED DATA PATH
PROCCESED_DATA_DIR = os.path.join(ARIFACTS_DIR ,"PROCCESED_DATA")
os.makedirs(PROCCESED_DATA_DIR , exist_ok = True)
lg.debug(f"Proccesed Data Directory: {PROCCESED_DATA_DIR}")

#PREPROCESSING_DATA DIR 
PREPROCESSING_DATA_DIR = os.path.join(ARIFACTS_DIR ,"PREPROCESSING_DIR")
os.makedirs(PREPROCESSING_DATA_DIR , exist_ok = True)
lg.debug(f"Preprocessing Data Directory: {PREPROCESSING_DATA_DIR}")


# IMPPUTER DIR
IMPUTER_DIR = os.path.join(ARIFACTS_DIR ,"IMPUTER_DIR")
os.makedirs(IMPUTER_DIR , exist_ok = True)
lg.debug(f"Imputer Directory: {IMPUTER_DIR}")

#SCALER DIR
SCALER_DIR = os.path.join(ARIFACTS_DIR ,"SCALER_DIR")
os.makedirs(SCALER_DIR , exist_ok = True)
lg.debug(f"Scaler Directory: {SCALER_DIR}")

# MODEL_ DIR
MODEL_DIR = os.path.join(ARIFACTS_DIR ,"MODEL_DIR")
os.makedirs(MODEL_DIR , exist_ok = True)
lg.debug(f"Model Directory: {MODEL_DIR}")


#File Names 
# DATA url 
RAW_DATA_URL = 'https://raw.githubusercontent.com/pk1308/datasets/master/secondhand%20car/data_train.csv'
lg.debug(f"Raw Data URL: {RAW_DATA_URL}")
TEST_DATA_URL = 'https://raw.githubusercontent.com/pk1308/datasets/master/secondhand%20car/data_test.csv'
lg.debug(f"Test Data URL: {TEST_DATA_URL}")

# DATA File Names after loading
RAW_FILE_NAME = os.path.join(RAW_DATA_DIR,"RAW_DATA_TO_PROCESS" + "CURRENT_TIME_STAMP" +".csv")
lg.debug(f"Raw Data File Name: {RAW_FILE_NAME}")

PROCCESED_FILE_NAME = os.path.join(RAW_DATA_DIR,"RAW_DATA_TO_TRAIN" + "CURRENT_TIME_STAMP" +".csv")
lg.debug(f"Proccesed Data File Name: {PROCCESED_FILE_NAME}")


IMPUTER_FIle_NAME = os.path.join(IMPUTER_DIR,"IMPUTER_DATA_LOAD" + CURRENT_TIME_STAMP+ ".pkl")
lg.debug(f"Imputer Data File Name: {IMPUTER_FIle_NAME}")
SCALER_FILE_NAME = os.path.join(SCALER_DIR,"SCALER_DATA_LOAD" + "CURRENT_TIME_STAMP" + ".pkl")
lg.debug(f"Scaler Data File Name: {SCALER_FILE_NAME}")

TRAIN_RAW_DATA_FILE_NAME = os.path.join(PROCCESED_DATA_DIR,"TRAIN_RAW_DATA_LOAD" + "CURRENT_TIME_STAMP" + ".csv")
lg.debug(f"Train Raw Data File Name: {TRAIN_RAW_DATA_FILE_NAME}")

TRAIN_FILE_NAME = os.path.join(PROCCESED_DATA_DIR,"TRAIN_DATA_TO_LOAD" + "CURRENT_TIME_STAMP" + ".csv")
lg.debug(f"Train Data File Name: {TRAIN_FILE_NAME}")

