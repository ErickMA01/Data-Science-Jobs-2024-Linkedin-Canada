import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('linkedin_canada.csv')

# Display basic information
print("Basic information about the dataset:")
print(df.info())

# Display the first few rows of the dataset
print("\nFirst few rows of the dataset:")
print(df.head())

# Display missing values in key columns
print("Missing values in key columns:")
print(df[['companyId', 'contractType', 'publishedAt', 'salary', 'sector', 'workType']].isnull().sum())

# Handling missing values
# Assuming appropriate strategies based on the nature of each column

# Fill missing values in 'companyId' with a placeholder or drop rows if appropriate
df['companyId'] = df['companyId'].fillna('Unknown')

# Fill missing values in 'contractType' with the most common contract type
df['contractType'] = df['contractType'].fillna(df['contractType'].mode()[0])

# Convert 'publishedAt' to datetime format and fill missing values with a placeholder or drop rows if appropriate
df['publishedAt'] = pd.to_datetime(df['publishedAt'], errors='coerce')
df['publishedAt'] = df['publishedAt'].fillna(pd.to_datetime('2024-01-01'))

# Fill missing values in 'salary' with a placeholder or drop rows if appropriate
df['salary'] = df['salary'].fillna('Not specified')

# Fill missing values in 'sector' with a placeholder or drop rows if appropriate
df['sector'] = df['sector'].fillna('Unknown')

# Fill missing values in 'workType' with the most common work type
df['workType'] = df['workType'].fillna(df['workType'].mode()[0])

# Display updated information after handling missing values
print("\nUpdated information after handling missing values:")
print(df[['companyId', 'contractType', 'publishedAt', 'salary', 'sector', 'workType']].isnull().sum())


# Explore the distribution of job types
df.title.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title('Distribution of Job Titles in Data Science')
plt.ylabel('Number of Job Postings')
plt.xlabel('Job Title')
plt.show()


# Display the most common job titles and their corresponding responsibilities
common_job_titles = df['title'].value_counts().head(10).index
for title in common_job_titles:
    responsibilities = df[df['title'] == title]['description'].values[0]
    print(f"\nJob Title: {title}\nResponsibilities:\n{responsibilities}\n{'='*50}")


# Get the count of all unique job titles
job_title_counts = df['title'].value_counts()

# Create a nicely formatted table
job_title_table = pd.DataFrame({'Job Title': job_title_counts.index, 'Count': job_title_counts.values})

# Display the table
print("Count of Unique Job Titles:\n")
print(job_title_table)

# Get the count of each unique experience level
experience_level_counts = df['experienceLevel'].value_counts()

# Create a nicely formatted table ordered by count in descending order
experience_level_table = pd.DataFrame({'Experience Level': experience_level_counts.index, 'Count': experience_level_counts.values})

# Order the table by count in descending order
experience_level_table = experience_level_table.sort_values(by='Count', ascending=False)

# Display the table
print("Experience Levels with Counts (Ordered by Count in Descending Order):\n")
print(experience_level_table)


# Set the style for the plot
sns.set(style="whitegrid")

# Create a bar chart of experience levels and their counts
plt.figure(figsize=(12, 6))
experience_level_chart = sns.barplot(x='Experience Level', y='Count', data=experience_level_table, hue='Experience Level', palette='viridis', legend=False)

# Set the title and labels
plt.title('Experience Levels and Their Counts')
plt.xlabel('Experience Level')
plt.ylabel('Count')

# Display the counts on the bars
for index, value in enumerate(experience_level_table['Count']):
    experience_level_chart.text(index, value, str(value), color='black', ha="center", va="bottom")

# Show the plot
plt.show()


# Get the count of each industry
industry_counts = df['sector'].value_counts()

# Create a nicely formatted table
industry_table = pd.DataFrame({'Industry Sector': industry_counts.index, 'Count': industry_counts.values})

# Display the table
print("Sector-specific Demand for Data Science Skills:\n")
print(industry_table)


# Get the count of applicants for each job role
applicants_table = df.groupby('title')['applicationsCount'].max().reset_index()

# Rename the columns for clarity
applicants_table.columns = ['Job Title', 'Number of Applicants']

# Display the table
print("Job Roles and Number of Applicants:\n")
print(applicants_table)


'''
# Set the style for the plot
sns.set(style="whitegrid")

# Create a bar chart of the top 20 job roles by the number of applicants
plt.figure(figsize=(14, 8))
applicants_chart = sns.barplot(x='applicationsCount', y='title', data=df.nlargest(20, 'applicationsCount'),
                               hue='applicationsCount', palette='Blues_d', dodge=False, legend=False)

# Set the title and labels
plt.title('Number of Applicants for Different Job Roles')
plt.xlabel('Number of Applicants')
plt.ylabel('Job Title')

# Display the counts on the bars
for index, value in enumerate(df.nlargest(20, 'applicationsCount')['applicationsCount']):
    applicants_chart.text(value, index, str(value), color='black', ha="left", va="center")

# Show the plot
plt.show()
'''


