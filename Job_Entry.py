#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:09:52 2020

@Purpose: Enter job information, create table with date entered, date due,
            quantity, and price

@author: gary
"""
from datetime import datetime

job_table = {}

def job_entry():
    
    while True:
        data_in = input("Enter Job/Contract Number: ")
        confirm_in = input("Is "+str(data_in)+" correct?(y/n) ")
        if confirm_in == 'y':
            job_table.update({'jobID':data_in})
            break
    
    while True:
        data_in = input("Enter Due Date(MMDDYYY): ")
        confirm_in = input("Is "+str(data_in)+" correct?(y/n) ")
        if confirm_in == 'y':
            job_table.update({'dueDate':datetime.strptime(data_in,"%m%d%Y")})
            break
    
    while True:
        data_in = input("Enter QTY: ")
        confirm_in = input("Is "+str(data_in)+" correct?(y/n) ")
        if confirm_in == 'y':
            job_table.update({'QTY':data_in})
            break
    
    while True:
        data_in = input("Enter Price(Numbers only): ")
        confirm_in = input("Is "+str(data_in)+" correct?(y/n) ")
        if confirm_in == 'y':
            job_table.update({'Price':data_in})
            break
    
    job_table.update({"createDate":datetime.now()})
    
    print (job_table)
    
    
    
def main():
    while True:
        try:
            job_entry()
        except:
            pass
            break

main()