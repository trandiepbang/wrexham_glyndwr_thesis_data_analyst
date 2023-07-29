import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Load the data
df = pd.read_csv('data/survey.csv')

# Data Cleaning
# Check for missing values
print(df.isnull().sum())

strategies = "What strategies do you currently use to stay aware of your surroundings?"
research = 'Do you conduct research about the safety of your destination when planning to travel?'
awareness_rating = "On a scale of 1-5, how would you rate your overall awareness of your surroundings? (1 being not aware at all, 5 being extremely aware, i.e a rating 5 would mean: I am able to perceive, understand,..."
safety_rating = "On a scale of 1-5, how would you rate the safety level of your city currently? (1 being extremely unsafe, 5 being extremely safe)"
df['awareness_rating'] = df[awareness_rating]
df['safety_rating'] =  df[safety_rating]
df["safety_research"] = df[research]
df["awareness_strategy"] = df[strategies]

# Fill missing values in safety and awareness ratings with their median
df['awareness_rating'] = df['awareness_rating'].fillna(df['awareness_rating'].median())
df['safety_rating'] = df['safety_rating'].fillna(df['safety_rating'].median())

# Fill missing values in safety_research and awareness_strategy with appropriate values
df['safety_research'] = df['safety_research'].fillna('Not specified')
df['awareness_strategy'] = df['awareness_strategy'].fillna('Not specified')

# Convert age and city to category data type
df['Age'] = df['Age'].astype('category')
df['City'] = df['City'].astype('category')

# Data Analysis
# Descriptive statistics for overall awareness and safety level
print(df['awareness_rating'].describe())
print(df['safety_rating'].describe())

# Breakdown by age
print(df.groupby('Age')['awareness_rating'].describe())
print(df.groupby('Age')['safety_rating'].describe())

# Breakdown by city
print(df.groupby('City')['awareness_rating'].describe())
print(df.groupby('City')['safety_rating'].describe())

# Calculate proportions for safety_research and awareness_strategy
print(df['safety_research'].value_counts(normalize=True) * 100)

strategies_df = df['awareness_strategy'].str.split(',', expand=True).stack()
print("research strategy")
print(strategies_df.value_counts(normalize=True) * 100)

# Correlation between age and awareness, and safety rating
# As age is a categorical variable, we'll first create an age_code column
df['age_code'] = df['Age'].cat.codes
correlation_matrix = df[['age_code', 'awareness_rating', 'safety_rating']].corr()

# Visualize the correlation matrix using a heatmap
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()
