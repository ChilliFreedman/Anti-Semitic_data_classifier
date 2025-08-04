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
        counter = self.first_df.groupby("Biased").size()
        antisemitic = counter[1]
        non_antisemitic = counter[0]
        total = counter.sum()
        dict_total_tweets["total_tweets"]["antisemitic"] = antisemitic
        dict_total_tweets["total_tweets"]["non_antisemitic"] = non_antisemitic
        dict_total_tweets["total_tweets"]["total"] = total
        dict_total_tweets["total_tweets"]["unspecified"] = total - (antisemitic + non_antisemitic)

        return dict_total_tweets

    def average_length(self):
        dict_average_length = {"average_length": {"antisemitic": 0,"non_antisemitic": 0,"total": 0}}
        new_df = self.first_df.copy()
        new_df["Count_Words"] = self.first_df['Text'].str.split().str.len()
        avarge_words = new_df.groupby('Biased')['Count_Words'].mean()
        avarge_words_all = new_df['Count_Words'].mean()
        avarge_antisemitic = avarge_words[1]
        avarge_non_antisemitic = avarge_words[0]
        dict_average_length["average_length"]["antisemitic"] = avarge_antisemitic
        dict_average_length["average_length"]["non_antisemitic"] = avarge_non_antisemitic
        dict_average_length["average_length"]["total"] = avarge_words_all


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
