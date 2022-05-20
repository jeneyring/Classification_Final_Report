def telco_split(df):
    '''
    This function takes in Telco data from the acquire.py file,
    performs a split and stratifies on churn.
    Returns train, validate, and test dfs.
    '''
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.churn)
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.churn)
    return train, validate, test

def prep_telco(df):
    '''
    This function takes in the Telco df(via acquire.py).
    It drops the species_id column and renames species_name to species, 
    Performs a 3-way split stratified on churn, and
    Returns train, validate, and test dataframes.
    '''
    # drop and rename columns
    df = df.drop(columns='customer_id').rename(columns={'has_churned': 'Churned_Customers'})
    
    # split dataframe into train, validate, and test
    train, validate, test = telco_split(df)
    
    return train, validate, test

train, validate, test = prep_telco(df)
