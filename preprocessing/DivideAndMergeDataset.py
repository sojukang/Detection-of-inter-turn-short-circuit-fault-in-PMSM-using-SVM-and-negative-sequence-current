from numpy.core.fromnumeric import reshape
import pandas as pd 
import numpy as np 

class DivideDataset():
    def __init__(self, dataset: pd.DataFrame):
        self.dataset = dataset 

    def reshape_dataset(self):
        self.dataset = pd.DataFrame(self.dataset.values.reshape(40, 83))
        
        return self.dataset

    def divide_dataset(self, divide_num = 4):
        self.reshape_dataset()
        dic_dataset = {}
        interval = len(self.dataset) // divide_num
        for i in range(divide_num):
            dic_dataset[i] = self.dataset.iloc[i*interval: (i+1)*interval]
        
        return dic_dataset
    
class MergeSubsets():
    def __init__(self, subset: pd.DataFrame) -> None:
        self.dataset = subset

    def add_subset(self, subset: pd.DataFrame):
        self.dataset = pd.concat([self.dataset, subset], ignore_index=True)
    
    