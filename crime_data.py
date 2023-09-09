import pandas as pd
import os
import matplotlib.pyplot as plt


# Load all CSV files
frames = []  # This list will store all the dataframes

# os.walk returns a generator that produces filepaths in a directory tree 
for subdir, dirs, files in os.walk("./data"):
    for file in files:
        if file.endswith('.csv'):  # Only process CSV files
            filepath = subdir + os.sep + file  # Get the full path of the file
            df = pd.read_csv(filepath)
            frames.append(df)
data = pd.concat(frames, ignore_index=True)

# Extracting Year from the 'Month' column
data['Year'] = pd.to_datetime(data['Month']).dt.year

# Grouping by police station and year
grouped_data = data.groupby(['Reported by', 'Year'])

# Analyzing Frequency of Crimes Based on Crime Type
counts = grouped_data['Crime type'].value_counts().unstack().fillna(0)
print('Frequency of Crimes Based on Type:')
print(counts)

# Save DataFrame to CSV
counts.to_csv('crimes_by_type_and_year.csv')

# Plot and Save Diagram
counts.plot(kind='bar', figsize=(15, 7))
plt.title('Frequency of Crimes Based on Type')
plt.tight_layout()
plt.savefig('crimes_by_type_and_year.png')
plt.show()