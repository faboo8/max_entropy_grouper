# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 15:09:24 2018

@author: DE104752
"""

from GroupingClass import EntropyGrouping 
import pandas as pd
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='excelfile', type=str)
    parser.add_argument('input1_2', help='sheet', type=str)
    parser.add_argument('input2', help='name column', type =str )
    parser.add_argument('input3', help='feature columns',  type =list )
    parser.add_argument('input4', help='number of columns',  type =int )
    parser.add_argument('input5', help='random swap',  type =bool, default=False,nargs='?' )
    
    
    
    args = parser.parse_args()
    
    col_num_name = ord(args.input2)-ord('A')
    col_num_feat = [ord(it)-ord('A') for it in args.input3.split(',')]
    
    df= pd.read_excel(sheet_name=args.input1_2, io = args.input1,
                   header=0, usecols=args.input2+args.input3, names=)

    
    test = EntropyGrouping(df, 'name', ['role', 'branch', 'gender'], random_swap=True, shuffle =True, N=7)
    

    parser = argparse.ArgumentParser()
    #