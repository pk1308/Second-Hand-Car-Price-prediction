
import pandas as pd 
from SRC.utils import constants
import os
import glob
from datetime import datetime
import logging as lg
from SRC.utils.logger import APP_Logger
from SRC.utils import constants

lg = APP_Logger(os.path.basename(__file__))


def get_null_percent(df: pd.DataFrame) -> pd.DataFrame:
    """ Funstion take a dataframe and return the percentage of null values in each column """
    null_values=df.isnull().sum()
    null_values=pd.DataFrame(null_values,columns=['null'])
    j=1
    sum_tot=len(df)
    null_values['percent']=null_values['null']/sum_tot
    round(null_values*100,3).sort_values('percent',ascending=False)
    return null_values

def sep_column_dtypes(df):
    """ Separate the dataframe into categorical and numerical columns """

    catgeories_columns = df.select_dtypes(include=['category']).columns.tolist()
    boolan_columns = df.select_dtypes(include=['bool']).columns.tolist()
    numeric_columns = df.select_dtypes(include=['int32', 'int16', 'int8' ,  'float32']).columns.tolist()
    lg.debug(f"Categorical Columns: {catgeories_columns}")
    lg.debug(f"Boolean Columns: {boolan_columns}")
    lg.debug(f"Numerical Columns: {numeric_columns}")

    return catgeories_columns, boolan_columns, numeric_columns 


def reduce_memory_usage(df, deep=True, verbose=False, categories=True):
    # All types that we want to change for "lighter" ones.
    # int8 and float16 are not include because we cannot reduce
    # those data types.
    # float32 is not include because float16 has too low precision.
    numeric2reduce = ["int16", "int32", "int64", "float64"]
    start_mem = 0
    start_mem = memory_usage_mb(df, deep=deep)

    for col, col_type in df.dtypes.iteritems():
        best_type = None
        if col_type == "object":
            df[col] = df[col].astype("category")
            best_type = "category"
        elif col_type in numeric2reduce:
            downcast = "integer" if "int" in str(col_type) else "float"
            df[col] = pd.to_numeric(df[col], downcast=downcast)
            best_type = df[col].dtype.name
        # Log the conversion performed.
        if verbose and best_type is not None and best_type != str(col_type):
            lg.info(f"Column '{col}' converted from {col_type} to {best_type}")

    end_mem = memory_usage_mb(df, deep=deep)
    diff_mem = start_mem - end_mem
    percent_mem = 100 * diff_mem / start_mem
    lg.info(f"Memory usage decreased from"
          f" {start_mem:.2f}MB to {end_mem:.2f}MB"
          f" ({diff_mem:.2f}MB, {percent_mem:.2f}% reduction)")
    return df
    
def memory_usage_mb(df, *args, **kwargs):
    """Dataframe memory usage in MB. """
    return df.memory_usage(*args, **kwargs).sum() / 1024**2


def get_latest_file(dir : str ):
    
    """ This function takes the a dir and get bthe latest modified file"""
    list_of_files = glob.glob(dir +"/*") # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getmtime)
    return latest_file



    


