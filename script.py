# %%
import pandas as pd 
import numpy as np

# %%
#read csv files to dataframe

df = pd.read_csv('data/world-data-2023.csv', encoding='ISO-8859-1', low_memory=False)
df1 = pd.read_csv('data/globalterrorism.csv', encoding='ISO-8859-1', low_memory=False)


# %%
len_terrorism=len(df1)
df1= df1.replace('', np.nan) #change empty strings to nulls
df1= df1.replace(0, np.nan) #change zeros to nulls

#for cycle to check if a column has more than 40% nulls, if so then its dropped
for column in df1.columns:
        if len(df1[df1[column].isna()])/len_terrorism > 0.4: 
            df1=df1.drop(column, axis=1)

pd.set_option('display.max_columns', None)
print(df1)

# %%
#only keep some of the columns

clean_df1 = df1[['eventid', 'iyear', 'imonth', 'iday', 'country_txt', 'region_txt', 'provstate', 'city', 'latitude', 'longitude', 'summary', 'attacktype1_txt', 'targtype1_txt', 'targsubtype1_txt', 'weaptype1_txt',  ]]
print(clean_df1)

# %%
#check the different countries
unique_values = clean_df1['country_txt'].drop_duplicates()
pd.set_option('display.max_rows', None)
print(unique_values)

# %%
#replace east and west germany by germany
clean_df1['country_txt'] = clean_df1['country_txt'].replace('East Germany (GDR)', 'Germany')
clean_df1['country_txt'] = clean_df1['country_txt'].replace('West Germany (FRG)', 'Germany')
print (df1['country_txt'])

# %%
#same logic that before but for the second dataframe, this one doesn´t necesserily need it but to check
len_global=len(df)
df= df.replace('', np.nan)
for column in df.columns:
        if len(df[df[column].isna()])/len_global > 0.5:
            df=df.drop(column, axis=1)

print(df)

# %%
#change the header so it's coerent, put it in lowercase and replace spaces by '_'

df.columns = df.columns.str.lower().str.replace(' ', '_') 

print(df)

# %%
pd.reset_option('display.max_rows', None)

clean_df=df[['country', 'abbreviation', 'capital/major_city', 'life_expectancy', 'official_language', 'population']]
print(df)

# %%
#merge the two dataframes by country

df_merged= pd.merge(clean_df, clean_df1, left_on= 'country', right_on= 'country_txt', how='inner')

df_merged.head()

# %%
#check and delete the null if they still exist

len_merged = len(df_merged)
df_merged= df_merged.replace('', np.nan)
for column in df_merged.columns:
        if len(df_merged[df_merged[column].isna()])/len_merged > 0.5:
            df_merged=df_merged.drop(column, axis=1)

print(df_merged)

# %%
#write dataframe t csv file
df.to_csv('final.csv', index=False)

# %%



