import numpy as np 
import pandas as pd 

def nsc_augment(df, T: int):
    '''
    Calculate NSC(Negative Sequantial Current) and add columns to pandas dataframe
    '''
    a = complex(-0.5, 0.866 * np.pi)
    a2 = complex(-0.5, -0.866 * np.pi)
    df['Max(A)'] = 0 
    df['Max(B)'] = 0 
    df['Max(C)'] = 0 
    df['NSC'] = 0 

    for i in range(len(df.iloc[: , 1]) - (T-1)):
        df['Max(A)'][i: i + T] = df.iloc[i: i + T, 1].max()
        df['Max(B)'][i: i + T] = df.iloc[i: i + T, 2].max()
        df['Max(C)'][i: i + T] = df.iloc[i: i + T, 3].max()

    df['NSC'] = abs(0.333 * (df.loc[:, 'Max(A)'] + a2 * df.loc[:, 'Max(B)'] +  a * df.loc[:, 'Max(C)']))
    df.drop(['Max(A)', 'Max(B)', 'Max(C)'], axis=1, inplace=True)
