import pandas as pd
import matplotlib as plt
import numpy as np
import os

#importing Cust1Table copy from my Telco excel file:
def excel_file():
    excel_sheet="Full Telco Data_ Jennifer Eyring.xlsx"
    df_excel = pd.read_excel(excel_sheet)
    return df_excel

