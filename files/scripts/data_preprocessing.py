import pandas as pd

# Read the .csv
df_recs = pd.read_csv(r"files\data\USREC.csv")
df_yc = pd.read_csv(r"files\data\par-yield-curve-rates-1990-2023.csv")

# Modify the columns
df_recs = df_recs.rename(columns={"observation_date": "date"})

# Convert df_recs data from monthly to daily
df_recs['date'] = pd.to_datetime(df_recs['date'], format="%Y-%m-%d")
df_recs = df_recs.set_index('date')
df_yc = df_yc.set_index('date')

# Identify columns with many missing values 
nan_cols = df_yc.isna().sum()
# print(nan_cols) # series is either inconsistent, or started later
df_yc.drop(["1 mo", "2 mo", "4 mo", "20 yr", "30 yr"], axis=1, inplace=True)
df_yc = df_yc.dropna() # drop the last dates containing NaN's

# Note that the "exact" start day and end day of the recessions are lost
df_recs = df_recs.reindex(df_yc.index, method='ffill')
df_recs.to_csv(r"files\data\f_USREC.csv")
df_yc.to_csv(r"files\data\f_YC-rates-1990-2023.csv")