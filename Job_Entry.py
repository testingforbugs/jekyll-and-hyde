#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:12:15 2020

@author: erik the well endowed, also gary aka smoldik
"""

import re
from datetime import datetime

def job_entry():
    
    job_list = {}
    
    while True:
        jobnum = input("What is the job number? ")
        
        while True:
            confirm = input("Is "+str(jobnum)+" correct? (y/n): ")
            if confirm == 'y':
                break
        
        duedate = input("What is the due date? (DDMMYYYY): ")
        
        while True:
            confirm = input("Is "+str(datetime.strptime(duedate, "%d%m%Y"))+" correct? (y/n): ")
            if confirm == 'y':
                break
        
        entrydate = datetime.now()
        
        job_list.update({"JobNum":jobnum})
        job_list.update({"DueDate":datetime.strptime(duedate, "%d%m%Y")})
        job_list.update({"EntryDate":entrydate})
        
        print(job_list)
        
job_entry()