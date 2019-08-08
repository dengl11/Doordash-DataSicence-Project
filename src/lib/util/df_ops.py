###########################################################
###############       Dataframe Ops       #################
###########################################################
import os, sys
import pandas as pd
from pandas import DataFrame 

def mat2df(mat, columns=None, index=None, dtype=None):
    """return a dataframe from a np matrix 
    Args:
        mat: np matrix 

    Return: 
    """
    return DataFrame(mat, index=index, columns=columns, dtype=dtype)
    

def dump(df, save_path, **kwargs):
    """save a dataframe to a file

    :save_path: path to save
    :returns: None

    """
    ext = os.path.splitext(save_path)[1]
    assert ext in {".xls", ".xlsx", ".tsv", ".csv"}, "File Type not Supported!"

    verbose = kwargs.get('verbose', True)
    index = kwargs.get('index', False)
    encoding = kwargs.get('encoding', "utf-8")

    if ext in [".xls", ".xlsx"]: # excel
        df.to_excel(save_path, index=index)
    elif ext == ".csv":
        df.to_csv(save_path, index=index, encoding=encoding)
    elif ext == ".tsv":
        df.to_csv(save_path, index=index, sep="\t")
    if verbose: print("Data Dumped to {}".format(save_path))

def to_dict_value_array(df, dtype=None):
    """return {col1: [...], col2: [...]}
    Args:
        df: 

    Return: 
    """
    keys = df.keys().tolist()
    columns = df.values.T
    if dtype:
        columns = columns.astype(dtype)
    return dict(zip(keys, columns.tolist()))


def load(file_path, **kwargs):
    """
    Args:
        file_path: 

    Return: 
    """
    sheetname = kwargs.get('sheetname', None)
    verbose = kwargs.get('verbose', True)
    encoding = kwargs.get('encoding', 'utf-8')
    index_col = kwargs.get('index_col', None)
    engine = kwargs.get('engine', None)
    header = kwargs.get('header', "infer")
    usecols = kwargs.get('usecols', None)
    sep = kwargs.get('sep', None)

    ext = os.path.splitext(file_path)[1]
    assert sep is not None or ext in {".xls", ".xlsx", ".tsv", ".csv"}, "File Type not Supported!"

    if ext in [".xls", ".xlsx"]: # excel
        return pd.read_excel(file_path, sheetname = sheetname)
    if sep is None:
        sep = '\t' if ext == '.tsv' else ','
    dataframe = pd.read_csv(file_path,
                            sep = sep,
                            index_col = index_col,
                            engine=engine,
                            usecols=usecols,
                            header=header,
                            encoding=encoding)
    if verbose: print("Data Imported: {}".format(dataframe.shape))
    return dataframe

def force_column_type(df, column, dtype):
    """force the data type of column to be dtype
    """
    df = df.astype(object)
    df[column] = df[column].astype(dtype)
    return df
