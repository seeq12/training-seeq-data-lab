import pandas as pd
import numpy as np

def complex_health_score(df=None):
    '''
    This function does a complex analysis developed by some very smart people on the Data Analysis team.  
    
    This algorithm is designed to work on Seeq data that has been pulled in from Seeq using SDL and is in the form of a Pandas DataFrame
    
    Input:
    
    df : Pandas Dataframe
    
    Return: 
    Health Score (df) 
    '''
    
    
    df['Health Score'] = np.random.uniform(60, 100, df.shape[0])
    return(pd.DataFrame(df['Health Score']))
    