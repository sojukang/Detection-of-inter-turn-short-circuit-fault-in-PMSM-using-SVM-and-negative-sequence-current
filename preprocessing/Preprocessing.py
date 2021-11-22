import pandas as pd 
import numpy as np 

class Preprocessing():
    def __init__(self, dataset: pd.DataFrame, rpm):
        self.rpm = rpm
        self.freq_source = rpm / 30
        self.period = 1 / self.freq_source 
        self.dataset = dataset

    def fundamental_total_sample_period(self, time_sample):
        '''
        time_sample: a sampling timem. return the fundamental number of samples in total sample period
        '''
        self.time_sample = time_sample
        self.freq_sample = 1 / self.time_sample 

        return self.period / time_sample

    def dft(self):
        pass 

    def nsc_augment(self):
        '''
        Calculate NSC(Negative Sequantial Current) and add columns to pandas dataframe
        '''
        a = complex(-0.5, 0.866 * np.pi)
        a2 = complex(-0.5, -0.866 * np.pi)
        self.dataset['Max(A)'] = 0 
        self.dataset['Max(B)'] = 0 
        self.dataset['Max(C)'] = 0 
        self.dataset['NSC'] = 0 

        for i in range(len(self.dataset.iloc[: , 1]) - (self.period-1)):
            self.dataset['Max(A)'][i: i + self.period] = self.dataset.iloc[i: i + self.period, 1].max()
            self.dataset['Max(C)'][i: i + self.period] = self.dataset.iloc[i: i + self.period, 3].max()
            self.dataset['Max(B)'][i: i + self.period] = self.dataset.iloc[i: i + self.period, 2].max()

        self.dataset['NSC'] = abs(0.333 * (self.dataset.loc[:, 'Max(A)'] + a2 * self.dataset.loc[:, 'Max(B)'] +  a * self.dataset.loc[:, 'Max(C)']))
        self.dataset.drop(['Max(A)', 'Max(B)', 'Max(C)'], axis=1, inplace=True)

        return self.dataset