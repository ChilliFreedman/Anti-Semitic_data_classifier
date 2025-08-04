from cconvert_to_data_frame import DataLoader
from  data_investigation import DataAnalyzer
from data_cleaner import Cleaner
#check DataLoader
df = DataLoader.csv_to_df()
#print(df.value_counts())
#print(df.count())
#print(df["Biased"].unique())
#nn = df.groupby("Biased").size().reset_index(name='counts')

#check DataAnalyzer
d1 = DataAnalyzer()
d1.get_df(df)
print(d1.total_tweets())

#d1.df_testing()

#check Cleaner
clean_df = Cleaner.clean_df(df)
#print(clean_df)

