from Datasets import Sentiment_dataset
import pandas as pd


class load_data(object):

    def __init__(self, name):
        self.df = pd.read_csv(name, headers=0, engine='python', sep=',')
        self.shape = df.shape

    def load(self):
        return self.df, self.shape
