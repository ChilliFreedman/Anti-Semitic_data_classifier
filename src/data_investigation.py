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
        dict_total_tweets = {"total_tweets": {"antisemitic": 0,"non_antisemitic": 0,"total": 0,"unspecified" : 0}}

        return dict_total_tweets

    def average_length(self):
        dict_average_length = {"average_length": {"antisemitic": 0,"non_antisemitic": 0,"total": 0}}

        return dict_average_length



    def common_words(self):
        dict_common_words = {"common_words": {"total": []}}

        return dict_common_words

    def longest_3_tweets(self):
        dict_longest_3_tweets = {"longest_3_tweets": {"antisemitic": [],"non_antisemitic": []}}

        return dict_longest_3_tweets

    def uppercase_words(self):
        dict_uppercase_words = {"uppercase_words": {"antisemitic": 0,"non_antisemitic": 0,"total": 0}}

        return dict_uppercase_words

if __name__ == "__main__":
    d1 = DataAnalyzer()
    df = DataLoader.csv_to_df()
    d1.get_df(df)
    d1.df_testing()
