import pandas as pd
import matplotlib.pyplot as plt

# Question 1: Read the CSV into a DataFrame.
df = pd.read_csv("bicycle_data.csv")


# Question 2: Inspect the columns and convert their data types.
print(df.columns)
print(df.dtypes)

# Date contains the date and hour and should have a datetime type.
df["Date"] = pd.to_datetime(
    df["Date"], format="%m/%d/%Y %I:%M:%S %p"
)
print(df.dtypes)

# The remaining columns contain total, west, and east bicycle counts.
# They should be integers; Int64 also allows missing values.
for column in df.columns[1:]:
    df[column] = df[column].astype("Int64")

print(df.dtypes)


# Question 3: Add total bicycle count, hour, and year columns.
df["Total"] = (
    df["Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"]
    + df["Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk"]
)
df["Hour"] = df["Date"].dt.hour
df["Year"] = df["Date"].dt.year

print(df["Total"].head())
print(df[["Date", "Total", "Hour", "Year"]].head())


# Question 4: Create a DataFrame containing only 2016 data.
df_2016 = df[df["Year"] == 2016].copy()

print(df_2016.head())


# Question 5: Count and remove records with missing counts.
print(df_2016.isna().sum())

missing_rows = df_2016.isna().any(axis=1)
print(missing_rows.sum())
print(df_2016.loc[missing_rows])

# 1 time point has missing counts: 2016-03-13 02:00:00.
# Exclude it from the hourly totals and averages.
df_2016 = df_2016.dropna(subset=["Total"])

print(df_2016.shape)
print(df_2016["Total"].isna().sum())


# Question 6: Plot total bicycle counts by hour and save the figure.
hourly_counts = df_2016.groupby("Hour")["Total"].sum()

hourly_counts.plot(kind="bar")
plt.title("Fremont Bridge Bicycle Counts by Hour (2016)")
plt.xlabel("Hour of Day")
plt.ylabel("Total Bicycle Count")
plt.tight_layout()
plt.savefig("counts_by_hour.png")
plt.show()


# Question 7: Calculate the busiest hour on average.
hourly_average = df_2016.groupby("Hour")["Total"].mean()
busiest_hour = hourly_average.idxmax()

# The busiest hour on average is 17:00–18:00, with about 399 bicycles.
print(hourly_average)
print("Busiest hour:", busiest_hour)