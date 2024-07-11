import csv
import pandas as pd


#read in csv
df = pd.read_csv('Sleep_health_and_lifestyle_dataset_cleaned.csv', na_values=[' ','N/A','Null'], keep_default_na=False)
print(df.head())

#check for missing values
print(df.isnull().values.any())

#print(df['Sleep Disorder'].iloc[0])
#print(type(df['Sleep Disorder'].iloc[0]))


