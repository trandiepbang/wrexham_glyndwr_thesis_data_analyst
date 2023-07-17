import os
import pandas as pd
import matplotlib.pyplot as plt

# The root directory where the folders are located
root_dir = "./UK/NorthWale"

frames = []  # This list will store all the dataframes

# os.walk returns a generator that produces filepaths in a directory tree 
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.csv'):  # Only process CSV files
            filepath = subdir + os.sep + file  # Get the full path of the file
            df = pd.read_csv(filepath)
            frames.append(df)

# Concatenate all dataframes
df = pd.concat(frames)


df['Month'] = pd.to_datetime(df['Month'])

# Frequency Counts
print("Frequency of Crimes Based on Type:")
print(df['Crime type'].value_counts())

print("Frequency of Crimes Based on Location:")
print(df['Location'].value_counts())

print("Frequency of Crimes Based on Month:")
print(df['Month'].dt.month.value_counts())

print("Frequency of Crimes Based on Year:")
print(df['Month'].dt.year.value_counts())

print("Frequency of Crimes Based on Day of the Week:")
print(df['Month'].dt.dayofweek.value_counts())

# Percentages
print("Percentage of Each Crime Type:")
print(df['Crime type'].value_counts(normalize=True) * 100)

# Trends over Time
for crime in df['Crime type'].unique():
    df_crime = df[df['Crime type'] == crime]
    df_crime.resample('M', on='Month').size().plot(label=crime, legend=True)

plt.title("Crime Rate Over Time by Type")
plt.show()
plt.savefig(f'data.png')
