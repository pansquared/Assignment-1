#pandas approach:
#https://codesignal.com/learn/courses/basics-of-numpy-and-pandas-with-titanic-dataset/lessons/mastering-pandas-a-deep-dive-into-dataframes-and-data-manipulation
#https://medium.com/data-science/olympics-kaggle-dataset-exploratory-analysis-part-2-understanding-sports-4b8d73a8ec30
import pandas as pd

# your local filename:
filepath = "council_district_turnout.csv"

df = pd.read_csv(filepath)

# first N rows (like slicing your list)
print(df.head(2))

# "first row"
print(df.iloc[0])

# slice rows 10..19 (like councilDistricts[10:20])
print(df.iloc[10:20])

# column names (like councilDistricts[0].keys())
print(df.columns)

# one column
print(df["Turnout"].head(10))

# multiple columns (prints the first 10 rows of each column)
print(df[["Geo_Unit", "Election", "Turnout"]].head(10))

# how many records are from General Elections vs Primary Elections?
general_mask = df["Election"].str.contains("General")
general_count = general_mask.sum()
primary_count = (~general_mask).sum()
print("General:", general_count, "Primary:", primary_count)

# how many records per year (overall)
print(df["Year"].value_counts(dropna=False).sort_index())

# within General Election records, how many had turnout above 30% vs 30% or below
general_rows = df.loc[general_mask].copy()
general_rows["Turnout_Level"] = general_rows["Turnout"].apply(
    lambda t: "High (>30%)" if t > 0.30 else "Low (<=30%)"
)
print(general_rows["Turnout_Level"].value_counts())
