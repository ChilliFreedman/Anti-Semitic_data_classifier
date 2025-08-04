import pandas as pd
from cconvert_to_data_frame import DataLoader


class DataAnalyzer:
    def __init__(self):
        self.first_df = None

    def get_df(self,df):

        self.first_df = df



    def df_testing(self):
        # Checking for missing values
        print(self.first_df.isnull().sum())
        # get shape of df
        print(f"shape {self.first_df.shape}")

    def total_tweets(self):
        return

    def average_length(self):
        return

    def common_words(self):
        return

    def longest_3_tweets(self):
        return

    def uppercase_words(self):
        return

if __name__ == "__main__":
    d1 = DataAnalyzer()
    df = DataLoader.csv_to_df()
    d1.get_df(df)
    d1.df_testing()
