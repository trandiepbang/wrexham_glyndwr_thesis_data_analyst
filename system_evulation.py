import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the csv file
df = pd.read_csv('data/survey.csv')

# Find out how many people heard of predict policing before
heard_predictive_policing = df['Have you heard about predictive policing before? (https://www.brennancenter.org/our-work/research-reports/predictive-policing-explained)'].value_counts()

# How many people understand predictive policing
understand_predictive_policing = df['On a scale of 1-5, how well do you understand predictive policing? (1 - not at all, 5 - very well)'].mean()

# Do people believe the proposed system can help reduce crime
belief_reduce_crime = df['Do you believe that the proposed system, similar to predictive policing for public introduced in the previous section, can help improve your awareness and reducing crime? (Yes/No/Not sure)'].value_counts()

# How comfortable are they with the use of the proposed system
comfort_with_system = df['On a scale of 1-5, how comfortable are you with the use of the proposed system? (1 - not at all comfortable, 5 - very comfortable)'].mean()

# How likely would they be to use such a system on a regular basis
# Convert categorical likelihood of use to numerical
likelihood_mapping = {'Very likely': 5, 
                      'Likely': 4, 
                      'Neither likely nor unlikely': 3, 
                      'Unlikely': 2, 
                      'Very unlikely': 1}
df['How likely would you be to use such a system on a regular basis?'] = df['How likely would you be to use such a system on a regular basis?'].map(likelihood_mapping)

likelihood_use = df['How likely would you be to use such a system on a regular basis?'].value_counts()

# What concerns, if any, do they have about the use of the proposed system
concerns = df['What concerns, if any, do you have about the use of the proposed system?\n'].value_counts()

# Correlation between understanding, comfort with the system, and likelihood of use
correlation = df[['On a scale of 1-5, how well do you understand predictive policing? (1 - not at all, 5 - very well)', 
                  'On a scale of 1-5, how comfortable are you with the use of the proposed system? (1 - not at all comfortable, 5 - very comfortable)', 
                  'How likely would you be to use such a system on a regular basis?']].corr()

new_columns = ['Understanding\nof predictive\npolicing',
               'Comfortability with\nproposed system',
               'Likelihood of\nregular use']

correlation.columns = new_columns
correlation.index = new_columns

# Create a heatmap
sns.heatmap(correlation, annot=True)
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, fmt=".2f", cmap='coolwarm',
            xticklabels=correlation.columns,
            yticklabels=correlation.columns)

plt.xticks(fontsize=8, rotation=45)
plt.yticks(fontsize=8, rotation=0)
plt.show()

# Print results
print("People who have heard of predictive policing: \n", heard_predictive_policing)
print("\nAverage understanding of predictive policing (1-5 scale): ", understand_predictive_policing)
print("\nBelief that the proposed system can help reduce crime: \n", belief_reduce_crime)
print("\nAverage comfort with the use of the proposed system (1-5 scale): ", comfort_with_system)
print("\nLikelihood of using the system on a regular basis: \n", likelihood_use)
print("\nConcerns about the use of the proposed system: \n", concerns)
print("\nCorrelation between understanding, comfort, and likelihood of use: \n", correlation)
