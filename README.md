# Data-Science-Jobs-2024-Linkedin-Canada
In this project, I will use "LinkedIn Canada: Data Science Jobs 2024" data set from kaggle.com 

to analyze the Data Science and Analysis job market in Canada as depicted in LinkedIn at the beginning of 2024.

I will mainly aim to:

- Identify trends in job availability across different provinces or cities in Canada.

- Analyze the distribution of job types and roles within the data science field.

- Compare qualifications and experience levels sought by employers.

- Investigate sector-specific demand for data science skills.

**Key Findings**

1. **Dataset Overview:**
   - The dataset contains 275 entries with 13 columns.
   - Key columns include information about applications count, company details, contract type, job description, experience level, location, posting time, published time, salary, sector, job title, and work type.
   - Notable data types are float64 for the company ID and object (likely string) for other columns.

2. **Handling Missing Values:**
   - Initial analysis showed missing values in several key columns.
   - Appropriate strategies were applied to handle missing values, such as filling 'companyId' with 'Unknown,' 'contractType' with the most common type, and 'publishedAt' with a default date.
   - Other columns like 'salary,' 'sector,' and 'workType' were handled similarly, filling missing values with appropriate placeholders or common values.

3. **Job Titles and Counts:**
   - There are 215 unique job titles in the dataset.
   - The most common job title is "Machine Learning Engineer I, ML (Anywhere ML)" with 15 occurrences.
   - The dataset covers a diverse range of job titles, reflecting the varied nature of data science roles.

4. **Experience Levels:**
   - Mid-Senior level is the most common experience level, followed by Entry level and Not Applicable.
   - The dataset includes a variety of experience levels, indicating opportunities for professionals at different career stages.

5. **Sector-specific Demand:**
   - Technology, Information and Internet, Software Development, and Financial Services are the top sectors with high demand for data science skills.
   - The dataset covers a broad range of industries, including IT services, human resources, transportation, and more.

6. **Number of Applicants for Different Roles:**
   - The analysis revealed varying numbers of applicants for different job roles.
   - Some roles, such as "AI Engineer" and "Staff Machine Learning Software Engineer," attract a high number of applicants.

7. **Overall Insights:**
   - The dataset provides valuable insights into the Canadian data science job market, encompassing diverse roles, experience levels, and industry sectors.
   - Companies in the technology, software development, and financial services sectors are actively seeking data science professionals.
   - The analysis sets the stage for further exploration, such as salary trends, geographical distribution, and specific skill requirements.

8. **Considerations:**
   - The dataset, while rich in insights, has limitations due to its size (275 entries). Care should be taken when making broad generalizations.
   - Further analyses, visualizations, or machine learning models can be developed based on specific research questions or objectives.

