import pandas as pd 
import numpy as np 

class Preprocessing():
    def __init__(self, rpm):
        self.rpm = rpm
        self.freq_source = rpm / 30
        self.period = 1 / self.freq_source 

    def fundamental_total_sample_period(self, time_sample):
        '''
        time_sample: a sampling timem. return the fundamental number of samples in total sample period
        '''
        self.time_sample = time_sample
        self.freq_sample = 1 / self.time_sample 

        return self.period / time_sample

    def dft(self, data: pd.DataFrame):
        
