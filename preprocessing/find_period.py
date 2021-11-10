def find_period(df):
    '''
    return period
    '''
    T = 0 
    for i in range(df.shape[0] // 2 , df.shape[0]):
        if df.iloc[i, 1] > 0 and df.iloc[i, 1] * df.iloc[i+1, 1] < 0:
            if T == 0:
                T = i 
            else:
                T = i - T 
                return T  
    return 0  
        