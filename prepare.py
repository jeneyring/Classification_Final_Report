import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
# imputer from sklearn
from sklearn.impute import SimpleImputer

#Prepare Telco Data:
def clean_telco_data(df):
    #Replacing empty cells with nulls:
    df = df.replace(' ', np.nan)
    #Replacing ints with yes or no:
    df.senior_citizen = df.senior_citizen.replace([0, 1], ['No', 'Yes'])
    #Changing total_charges from 'object' type to 'float64':
    df.total_charges = df.total_charges.astype('float')
    #Dropping rows with nulls:
    df = df.dropna()
    #Dropping unneeded columns:
    columns_to_drop = ['contract_type_id', 'payment_type_id', 'internet_service_type_id']
    df = df.drop(columns = columns_to_drop)
    #creating bool/encode for churn
    df.churn = df.churn == 'Yes'
    #creating dummy variables of categorical columns
    dummy_df = pd.get_dummies(df[['gender', 'senior_citizen', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies', 'paperless_billing', 'contract_type', 'payment_type', 'internet_service_type']], drop_first = True)
    #concatenating dummy variables onto original dataframe
    df = pd.concat([df, dummy_df], axis = 1)
    return df

def prep_telco_data(df):
    df = clean_telco_data(df)
    train, test = train_test_split(df, train_size = 0.8, stratify = df.churn, random_state = 1234)
    train, validate = train_test_split(train, train_size = 0.8, stratify = train.churn, random_state = 1234)
    return train, validate, test