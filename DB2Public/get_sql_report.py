"""
@authour: Phanikiran S
Version : 0.1
Updated date : 15-Jan-2018
"""
from sys import path
from os import getcwd

path.append('path') # appends SQL Path, Update required

from SqlExcel import SqlExcel  # Custom SQL to Excel class
import pyodbc
import pandas as pd
import numpy as np
# imports


def changeencode(data, cols):

    # print data.dtypes
    cols = []
    # print len(data.columns), len(cols)
    for col in data.columns:
        data[col] = pd.to_datetime(data[col], errors='ignore')
        if data[col].dtype == 'O':
            # print col
            try:
                data[col] = data[col].apply(lambda x: x.encode('UTF-8'))
                data[col] = data[col].apply(lambda x: ''.join([i if 32 < ord(i) < 126 else ' ' for i in x]))
            except AttributeError:
                data['col'] = data[col]
        else:
            pass
        # print col
        cols.append(''.join([i if 32 < ord(i) < 126 else " " for i in col]))

    try:
        # print len(data.columns), len(cols)
        data.columns = cols
    except ValueError:
        cols.append('?')
        data.columns = cols
    return data


def exec_sql(system='DB2T', user='<>', pwd='', sql_file='get_deadlocked_plans.sql', xl_path='', xl=False):
    """
    @Params:system -- DB2 subsystem
            user   -- db2 user
            pwd    -- password
            sql_file-- file in path I:\Dat\34BKALL\CRSM\Capacity Mgmt in CRSM\Reports\Source\SQL\
            xl_path -- default is C:\pyport\data
    """

    sql_file_path = r'I:\\Dat\\34BKALL\\CRSM\\Capacity Mgmt in CRSM\\Reports\\Source\\SQL\\' + str(sql_file)
    # path of sql including the sql file name, no comments are allowed in sql
    # print sql_file_path
    # create instance
    inst = SqlExcel(system, user, pwd)

    # create sql from file
    sql = inst.fl_to_sql(sql_file_path)
    # print sql
    # create connection
    cn = inst.db_connect()
    # print head of dataframe
    df = inst.sql_to_df(cn, sql)
    if xl:
        try:
            df.to_excel(xl_path + str('sql_result.xls'))
        except:
            df = changeencode(df, df.columns)
            # df.columns = df.columns.map(unicode)
            df.to_excel(xl_path + str('sql_result.xls'))
    return df
    # print df.head()




def exec_sqlserver(sql_file='get_deadlocked_plans.sql', path=True):
    """

    :param sql_file: file in path  I:\Dat\34BKALL\CRSM\Capacity Mgmt in CRSM\Reports\Source\SQL\
            path: path is True by default, if flase sql_file contains sql as tet instead of just the paths
    :return: dataframe with resultset of above sql file

    """
    cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=<>;"
                          "Database=<>;"
                          "Trusted_Connection=yes;")
    if path == True:
        sql_file_path = r'I:\\Dat\\34BKALL\\CRSM\\Capacity Mgmt in CRSM\\Reports\\Source\\SQL\\' + str(sql_file)
        # path of sql including the sql file name, no comments are allowed in sql

        sql = ''
        for ln in open(sql_file_path, 'r'):
            sql = sql + ' ' + ln

        # return sql result
        return pd.read_sql(sql, cnxn)
    else:
        sql = sql_file
        return pd.read_sql(sql, cnxn)

