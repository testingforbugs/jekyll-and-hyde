#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:12:15 2020

@author: erik the well endowed, also gary aka smoldik
"""

import re
from datetime import datetime
import Job_Entry

class PurchaseOrder():
       
    def __init__(self):
        pass
    
    
    def job_id_check(self):
        
        """Check if the user supplied job ID is the appropriate data type and if already exists in the database"""
        
        job_ids = [12348]
        
        while True:
            self.job_id = input("\nEnter job number: ")

            break_bool = False
            if bool(re.compile("^\d+$").match(self.job_id)):
                while True:
                    if int(self.job_id) in job_ids:
                        break_bool = True
                        break
                    else:
                        print("\nJob number does not exist. Try another job number.")
                        break
            else:
                print("\nJob number is not a valid format. Please try again.")
                continue
            if break_bool:
                break
        
        return self.job_id
        
    
    def order_fill(self):
        
        """Fill out remaining purchase order fields after checking for a valid job ID"""
                
        job_id = PurchaseOrder.job_id_check(self)
        
        while True:
            self.due_date = input("\nEnter due date (YYYY-MM-DD): ")

            try:
                datetime.strptime(self.due_date, "%Y-%m-%d")
                break
            except:
                print("\nDate format is not valid.")
                continue
        
        while True:
            self.quantity = input("Enter quantity: ")
            
            if bool(re.compile("^\d+(\.\d+)*$").match(self.quantity)):
                break
            else:
                print("\nThat is not a valid quantity.")
                continue
        
        while True:
            self.price = input("Enter price (values only, no symbols): ")
            
            if bool(re.compile("^\d+(\.\d+)*$").match(self.price)):
                break
            else:
                print("\nThat is not a valid price.")
                continue
        
        return job_id, self.due_date, self.quantity, self.price
    
        
job, due_date, quantity, price = PurchaseOrder().order_fill()