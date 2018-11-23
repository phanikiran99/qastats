""""
Author : Phanikiran S
Version 1.0
"""
# this class creates the excel from an sql by connecting to db2 automatically
# imports
import ibm_db
import pandas as pd
import numpy as np
import datetime as dt


class SqlExcel():
    """ Connect and extract the data from sql to excel sheet
    Usage : 1. create instance of the class with nw = SqlExcel(sid,uid,pwd,sql)
            2. connect to db using nw.db_connect()
            3*. convert sql file to sql string by nw.fl_to_sql('file path')
            4.1. run sql and get data to dataframe sql_to_df(cn, sql)
            4.2. run sql and get data to excel sql_to_xl(cn, sql, path)"""
    def __init__(self, sid='DB2P', uid='', pwd=''):
        self.sid = sid
        self.uid = uid
        self.pwd = pwd
        # self.sql = sql

    def db_connect(self):
        """ Connect to Db2 Server.
        Usage: conn = db_connect() , Initiate instance with SqlExcel(sid,port,uid,pwd,sql)
        :returns: connection instance of ibm_db.connect() """
        valid = True
        if self.sid.upper() == 'DB2P':
            db = '<DBNAME>'
            port = '<PORTNUM>'
        else:
            valid = False
        if valid:
            # connstr = str('''"DATABASE={0};HOSTNAME={1};PORT={2};PROTOCOL=tcpip;uid={3};PWD={4};"'''.format(db, self.sid, port,  self.uid, self.pwd))
            conn_str = "DATABASE=%s;HOSTNAME=%s;PORT=%s;PROTOCOL=tcpip;UID=%s;PWD=%s;" % (
            db, self.sid, port, self.uid, self.pwd)
            # print conn_str
            conn = ibm_db.connect(conn_str, '', '')
        return conn

    def run_sql(self):
        pass

    def sql_to_df(self,conn,sql):
        """
        :param conn: connection instance from class SqlExcel()
        :param sql: sql text or string value
        :returns: Dataframe with the SQL Extract
        """
        # execute and export result to xls
        stmt = ibm_db.exec_immediate(conn, sql)  # exec sql
        lst = []
        df = pd.DataFrame()  # empty df
        cols = []
        # fetch results
        dictionary = ibm_db.fetch_assoc(stmt)
        # print dictionary
        if dictionary:
            cols =  dictionary.keys()
        while dictionary != False:
            lst.append(dictionary.values())
            dictionary = ibm_db.fetch_assoc(stmt)

        # form df
        df = pd.DataFrame(lst)
        df.columns = cols
        # print df.columns
        # print df.dtypes

        for col in df.columns:
            # print col
            if ('TIME' not in col and 'time' not in col) and (df[col].dtype != '<M8[ns]'):
                # print 'processing ' + col
                df[col] = pd.to_numeric(df[col], errors='ignore')
            # df[col] = pd.to_datetime(df[col], errors='ignore')
        # print df.head(2)
        return df

    def sql_to_xl(self,conn, sql, path):
        """
        :param conn: connection instance from class SqlExcel()
        :param sql: sql text or string value
        :param path: path where xls need to be stored
        :returns: sql output as stored in Excel file in the path given
        """
        # execute and export result to xls
        stmt = ibm_db.exec_immediate(conn, sql)  # exec sql
        lst = []
        df = pd.DataFrame()  # empty df

        # fetch results
        dictionary = ibm_db.fetch_assoc(stmt)
        while dictionary != False:
            lst.append(dictionary.values())
            dictionary = ibm_db.fetch_assoc(stmt)

        # form df
        df = pd.DataFrame(lst)
        # return df
        df.to_excel(path+'\sql_excel.xlsx')
        # return True

    def fl_to_sql(self, path_fl):
        """"
        :param path_fl: path where sql is stored along with sql file name
        :returns: sql string value for sql processing
        """
        sql = ''
        for ln in open(path_fl, 'r'):
            sql = sql + ' ' + ln
        return sql