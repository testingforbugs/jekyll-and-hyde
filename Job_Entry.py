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
        confirm = input("Is ",data_in," correct?(y/n) ")
        if confirm == 'y':
            job_table.update('jobID',data_in)
            False
    
    while True:
        data_in = input("Enter Due Date(MMDDYYY): ")
        confirm = input("Is ",data_in," correct?(y/n) ")
        if confirm == 'y':
            job_table.update('dueDate',datetime.strptime(data_in,"%m%d%Y"))
            False
    
    while True:
        data_in = input("Enter QTY: ")
        confirm = input("Is ",data_in," correct?(y/n) ")
        if confirm == 'y':
            job_table.update('QTY',data_in)
            False
    
    while True:
        data_in = input("Enter Price(Numbers only): ")
        confirm = input("Is ",data_in," correct?(y/n) ")
        if confirm == 'y':
            job_table.update('Price',data_in)
            False
    
    job_table.update("createDate",datetime.now())
    
    
    
def main():
    while True:
        try:
            job_entry()
        except:
            pass
            break