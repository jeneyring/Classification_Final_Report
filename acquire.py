import pandas as pd
import matplotlib as plt
import numpy as np
import os

#importing Cust1Table copy from my Telco excel file:
def excel_file():
    excel_sheet="Full Telco Data_ Jennifer Eyring.xlsx"
    df_excel = pd.read_excel(excel_sheet)
    return df_excel
#________________________________________________________
#using SQL database for Telco

from env import user, password, host
import os
import pandas as pd

def get_connection(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

#def new_telco_data():
    sql_query = '''SELECT * 
                    FROM customers AS cust
                        INNER JOIN
                        contract_types AS ct
                        ON ct.contract_type_id = cust.contract_type_id
                        INNER JOIN
                        customer_payments AS cp
                        ON cp.customer_id = cust.customer_id
                        INNER JOIN
                        internet_service_types AS ist
                        ON ist.internet_service_type_id = cust.internet_service_type_id;'''
    df = pd.read_sql(sql_query, get_connection('telco_churn'))
    df.to_csv('telco_df.csv')
    return df

def get_telco_data():
    filename = "telco_churn.csv"

    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col = 0)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('''SELECT * FROM customers
                            JOIN contract_types ON customers.contract_type_id = contract_types.contract_type_id
                            JOIN payment_types ON customers.payment_type_id = payment_types.payment_type_id
                            JOIN internet_service_types ON customers.internet_service_type_id = internet_service_types.internet_service_type_id;''', 
                            get_connection('telco_churn'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df