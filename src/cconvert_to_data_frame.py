import pandas as pd

class DataLoader:

    @staticmethod
    def csv_to_df():
        df = pd.read_csv('../data/tweets_dataset.csv')
        return df