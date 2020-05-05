#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 19:09:52 2020

@Purpose: Enter job information, create table with date entered, date due,
            quantity, and price

@author: gary
"""

job_table = {}

def job_entry():
    While True:
        data_in = input("Enter Job/Contract Number: ")
        confirm = input("Is ",data_in," correct?(y/n) ")
        if confirm === 'y':
            job_table.update('jobID',data_in)
            False
    
    While True:
        data_in = input("Enter Due Date(MMDDYYY): ")
        confirm = input("Is ",data_in," correct?(y/n) ")
        if confirm === 'y':
            job_table.update('dueDate',data_in)
            False
    
    While True:
        data_in = input("Enter QTY: ")
        confirm = input("Is ",data_in," correct?(y/n) ")
        if confirm === 'y':
            job_table.update('QTY',data_in)
            False
    
    While True:
        data_in = input("Enter Price(Numbers only): ")
        confirm = input("Is ",data_in," correct?(y/n) ")
        if confirm === 'y':
            job_table.update('Price',data_in)
            False
    
    
    
def main():
    while True:
        Try:
            job_entry()
        Except:
            False