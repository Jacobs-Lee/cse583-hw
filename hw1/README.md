# CSE 583 HW1: Bicycle Data Analysis

## Data

I used the [Fremont Bridge counter dataset](https://data.seattle.gov/api/views/65db-xm6k/rows.csv) from Seattle Open Data. The CSV is stored as `src/hw1_data_analysis/bicycle_data.csv`.

## Process

I wrote and ran `hw1.py` in PyCharm, checking the printed output after each step. Comments in the script label Questions 1–7.

1. Read the CSV into a pandas DataFrame and inspected the first few rows, column names, and data types.
2. Converted `Date` to datetime and the three count columns to nullable integers (`Int64`).
3. Added the East and West counts to create `Total`, then extracted `Hour` and `Year` from `Date`.
4. Selected the 2016 records into a separate DataFrame.
5. Found one record with missing counts, at 2016-03-13 02:00:00. I removed it rather than treating missing counts as zero, leaving 8,783 records.
6. Grouped the data by hour, summed the bicycle counts, and saved a labeled bar chart as `counts_by_hour.png`.
7. Calculated the mean count for each hour and used `idxmax()` to find the busiest hour: 17:00–18:00, averaging about 399 bicycles.

## Running the Script

From the `hw1` directory, with pandas and matplotlib available in the Python environment:

```bash
cd src/hw1_data_analysis
python hw1.py
```

The chart is saved in the working directory. If the plot window pauses execution, close it to see the remaining printed results.

## Bonus: Datetime Formats

Python's `datetime.datetime` represents an individual date and time. I converted the entire `Date` column using `pd.to_datetime()`. In my analysis, the resulting dtype was `datetime64[ns]`, where `ns` means nanoseconds. 

NumPy's `datetime64` supports different time units and efficient operations on arrays of dates and times. Pandas uses `Timestamp` for individual date-time values and provides datetime columns with convenient accessors such as `.dt.hour` and `.dt.year`.

## AI Assistance

I completed the hands-on work for this assignment in PyCharm. I set up the project folders and files, copied the dataset into the required location, and built the analysis script one section at a time. I entered and ran the code, inspected the output after each step, and shared results during the discussion to check my progress.

My work included inspecting the column names and data types, checking the datetime and integer conversions, and verifying the new total, hour, and year columns. I checked that the filtered data contained only 2016 records. I examined the missing-data output, confirmed the single record with missing counts, and checked that removing it left 8,783 records with no missing totals. I also ran the plotting code, inspected the chart, and checked the hourly averages and the computed busiest hour of 17:00. Finally, I removed unnecessary statements and personally reviewed and revised this README.

I used ChatGPT/Codex throughout the process for step-by-step explanations, example code, and help interpreting results. This assistance supported my work as I ran, checked, and revised the analysis in my own environment.
