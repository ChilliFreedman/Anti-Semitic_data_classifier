from cconvert_to_data_frame import DataLoader
from  data_investigation import DataAnalyzer
from data_cleaner import Cleaner
#check DataLoader
df = DataLoader.csv_to_df()
#check DataAnalyzer
d1 = DataAnalyzer()
d1.get_df(df)
d1.df_testing()
print(d1.total_tweets())
print(d1.average_length())
print(d1.common_words())
print(d1.longest_3_tweets())
print(d1.uppercase_words())
#check Cleaner
clean_df = Cleaner.clean_df(df)
print(clean_df)

