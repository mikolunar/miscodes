# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 23:29:06 2018

@author: mikolunar
"""
import csv
import os
from os import listdir
from os.path import isfile
from os import walk

import time
import datetime
from tika import detector
import platform


def write_report_to_file(file_name, record_list):
    print('*********** Writing to file CSV *************')
    myfile=open(file_name, 'w',  encoding='utf-8', newline='\n')
    with myfile:
        writer=csv.writer(myfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(record_list)
    
    print('writing complete')



def collect_filesystem_info(rootpath, full_scan, output_file):
    if not full_scan:
        full_scan=True
    
        

    print('*********************SensID Collecting System Info*************************')
    print('Roothpath: '+ rootpath)
    
    print('Scan Date: ',time.asctime(time.localtime(time.time())))
    print('Operating system detected: ', os.name, platform.system(), platform.release(), platform.architecture())
    print('File-system detected: ')
    
    array_list=[["Sequence No", "Root", "File", "Type", "Size"]]
    counter=0
    #myfile=open('scan_result2.csv', 'w',  encoding='utf-8', newline='\n')
    #print(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
    start_time=datetime.datetime.fromtimestamp(time.time())
    print('Timestamp: ',start_time)

    for root, dir_list, file_list in walk(rootpath):
        if len(dir_list)>0:         
            for directory in dir_list:           
                for file in file_list:
                    info=os.stat(os.path.join(root, file))
                    mod_time=time.asctime(time.localtime(info.st_mtime))
                    file_size= info.st_size
                    file_name, file_ext=os.path.splitext(file)
                    file_path = os.path.join(root, file)                
                    print(counter, root)
                    array_list.append([counter, root, file, file_ext, file_size])
                    counter=counter+1
        else:
            for file in file_list:
                info=os.stat(os.path.join(root, file))
                mod_time=time.asctime(time.localtime(info.st_mtime))
                file_size= info.st_size
                file_name, file_ext=os.path.splitext(file)
                file_path = os.path.join(root, file)
                print(counter, root)
                array_list.append([counter, root, file, file_ext, file_size])
                counter=counter+1
    finish_time=datetime.datetime.fromtimestamp(time.time())
    print('Finished. Timestamp: ',finish_time)
    print('Duration', finish_time-start_time)
    write_report_to_file(output_file, array_list)

    return True


#***************************************************************
# Main
    
collect_filesystem_info('d:\\temp', True, 'out11.csv')