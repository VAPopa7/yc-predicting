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

# Note that the "exact" start day and end day of the recessions are lost
df_recs = df_recs.reindex(df_yc.index, method='ffill')
df_recs.to_csv(r"files\data\f_USREC.csv")
df_yc.to_csv(r"files\data\f_YC-rates-1990-2023.csv")
