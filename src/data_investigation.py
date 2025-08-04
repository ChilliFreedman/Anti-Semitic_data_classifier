import pandas as pd
import numpy as np
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
        #print(new_df["Count_Words"].sum())
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
        new_df = self.first_df.copy()
        common_10_words = new_df.Text.str.split(expand=True).stack().value_counts().head(10)
        for word in common_10_words.keys():
            dict_common_words["common_words"]["total"].append(word)

        return dict_common_words

    def longest_3_tweets(self):
        dict_longest_3_tweets = {"longest_3_tweets": {"antisemitic": [],"non_antisemitic": []}}
        #Gets a copy of the original data frame
        new_df = self.first_df.copy()
        # Adds a column with the number of characters
        new_df["Count_Leters"] = self.first_df['Text'].str.len()
        # Splits into 2 data frames
        ant_df = new_df.loc[new_df['Biased'] == 1]
        non_ant_df = new_df.loc[new_df['Biased'] == 0]
        # Gets the 3 lines with the most characters
        ant_top_3_leters = ant_df["Count_Leters"].sort_values(ascending=False).head(3)
        ant_df_top_3 = ant_df.loc[ant_df['Count_Leters'].isin(ant_top_3_leters)]
        # Inserts the 3 long texts into the dictionary
        for i in ant_df_top_3['Text']:
            dict_longest_3_tweets["longest_3_tweets"]["antisemitic"].append(i)
        # Gets the 3 lines with the most characters
        non_ant_top_3_leters = non_ant_df["Count_Leters"].sort_values(ascending=False).head(3)
        non_ant_df_top_3 = non_ant_df.loc[non_ant_df['Count_Leters'].isin(non_ant_top_3_leters)]
        # Inserts the 3 long texts into the dictionary
        for i in non_ant_df_top_3['Text']:
            dict_longest_3_tweets["longest_3_tweets"]["non_antisemitic"].append(i)

        return dict_longest_3_tweets

    def uppercase_words(self):
        dict_uppercase_words = {"uppercase_words": {"antisemitic": 0,"non_antisemitic": 0,"total": 0}}
        new_df = self.first_df.copy()
        ant_df = new_df.loc[new_df['Biased'] == 1]
        non_ant_df = new_df.loc[new_df['Biased'] == 0]
        #b = pd.new_df(new_df['Text'].tolist()).stack().str.split(expand=True).stack().str.isupper().sum()

        ant = pd.Series(ant_df['Text']).str.split(expand=True).stack().str.isupper().sum()
        non_ant = pd.Series(non_ant_df['Text']).str.split(expand=True).stack().str.isupper().sum()

        dict_uppercase_words["uppercase_words"]["antisemitic"] = ant
        dict_uppercase_words["uppercase_words"]["non_antisemitic"] = non_ant
        dict_uppercase_words["uppercase_words"]["total"] = ant + non_ant





        return dict_uppercase_words

if __name__ == "__main__":
    d1 = DataAnalyzer()
    df = DataLoader.csv_to_df()
    d1.get_df(df)
    d1.df_testing()
