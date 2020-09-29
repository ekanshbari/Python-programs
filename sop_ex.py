#!/usr/bin/env python

import pysftp
import re
import os, sys
import glob
import shutil
import pymysql
import sys
from datetime import datetime
from pytz import timezone


#cred of db 
# host = ''
# user = ''
# password = ''


#download files from sftp
def dwnldsftp():
    #connection with sftp server
    server = pysftp.Connection(host='139.15.173.37',
                  username='ftp_SGPAWS',
                  password='1P%@n`A#Ev-y')
    server.cwd('\BSHOUT')
    filelist = server.listdir()
    print ("connection established to FTP server logs will be captured in /opt/scriptlogs/sftp.log")
    for filename in filelist:
        filedate = re.search(".*\.csv$", filename)
        if filedate:
            print (filename)
            server.get("/BSHOUT/" + filename, "C:/Programs/python" + filename)    # this location is at sftp server (source) -> jenkins (destination)
            print("latest files downloaded to /opt/SOP_currentdata now proceeeding with creating backup")
        #     server.get("/BSHOUT/" + filename, "/opt/SOP_backupdata/" + filename)
        # print("backup files created in /opt/backupdata")

    print ("cleaning files from FTP server")
                
    print ("SFTP process completed closing FTP connection")
    server.close()
    print ("Bye Bye SFTP")

    # print ("Renaming files for updating database")
    # print(" ")

    # dir= "/opt/SOP_currentdata"    # this location is at jenkin server

#     #renaming the files
#     for newname in os.listdir(dir):
#          if(newname.split('.')[0]=='INDR2C' and "Y" in newname):
#                 print (newname,'masterVIB.csv')
#                 shutil.move(newname, "masterVIB.csv")

#     for newname in os.listdir(dir):
#             if(newname.split('.')[0]=='INDR2C' and "X" in newname):
#                     print (newname,'masterData.csv')
#                     shutil.move(newname, "masterData.csv")

#     print ("renaming files completed, triggering Database update")
#     #push csv to db
#     csv_to_mysql(load_sql, host, user, password)
#     #update tym in db with table name update_time needs to be created if not present
#     tymup()


# #This function load a csv file to MySQL table according to the load_sql statement.
# def csv_to_mysql(load_sql, host, user, password):
#     '''
#     This function load a csv file to MySQL table according to
#     the load_sql statement.
#     '''
#     try:
#         con = pymysql.connect(host=host,
#                                 user=user,
#                                 password=password,
#                                 autocommit=True,
#                                 local_infile=1)
#         print('Connected to DB: {}'.format(host))
#         # Create cursor and execute Load SQL
#         cursor = con.cursor()
#         # cursor.execute("truncate table sop_db.sales_master_data_v2;")
#         cursor.execute("truncate table sop_db.masterVIB;")
#         print("truncated old values from database...updating current values")
#         cursor.execute(load_sql)
#         cursor.execute(load_sql1)
#         print('Succuessfully updated the table from currentdata dir')
#         con.close()

#     except Exception as e:
#         print('Error: {}'.format(str(e)))
#         sys.exit(1)


# # Execution Example
# load_sql = """ LOAD DATA LOCAL INFILE '/opt/SOP_currentdata/masterData.csv' INTO TABLE sop_db.sales_master_data_v2\
#  FIELDS TERMINATED BY ';' ENCLOSED BY '"' IGNORE 1 LINES; """

# load_sql1 = """ LOAD DATA LOCAL INFILE '/opt/SOP_currentdata/masterVIB.csv' INTO TABLE sop_db.masterVIB\
#  FIELDS TERMINATED BY ';' ENCLOSED BY '"' IGNORE 1 LINES; """


# #function update the update_time table after every successful execution of script
# def tymup():
#     zone=timezone('Asia/Singapore')
#     timenow=datetime.now(zone)
#     db = pymysql.connect(host='DB_Host_Name', user='DB_User_Name', password='DB_Password', autocommit=True, local_infile=1)
#     cursor = db.cursor()
#     cursor.execute("truncate table sop_db.update_time;")
#     cursor.execute('INSERT INTO sop_db.update_time (date) values(%s)', (timenow.strftime('%d-%m-%Y %H:%M') + " SGT" ))
#     db.close()



#starting the run
#flow of code dwnlsftp() -> csv_to_mysql() -> tymup()
dwnldsftp()




