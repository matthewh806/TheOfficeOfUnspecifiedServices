import pandas as pd
import matplotlib.pyplot as plt

# Read in the data from the CSV file using Pandas
df = pd.read_csv('movie_data_2022.csv')

# Extract the month from the "Watch Date" column and count the number of movies watched in each month
movies_by_month = df['Watch Date'].str.split('/', expand=True)[1].value_counts()

# Extract the months and movie counts from the Pandas Series
months = movies_by_month.index
counts = movies_by_month.values

# Sort the months and counts by the months
months, counts = zip(*sorted(zip(months, counts)))

# Plot the histogram
plt.bar(months, counts)
plt.xlabel('Month')
plt.ylabel('Number of Movies Watched')
plt.title('Movies Watched by Month')
plt.show()

# Create a new column with the decade of release
df['Decade'] = df['Year of Release'].apply(lambda x: str(x)[:3] + '0s')

# Count the number of movies released in each decade
movies_by_decade = df['Decade'].value_counts()

# Extract the decades and movie counts from the Pandas Series
decades = movies_by_decade.index
counts = movies_by_decade.values

# Sort the decades and counts by the decades
decades, counts = zip(*sorted(zip(decades, counts)))

# Plot the histogram
plt.bar(decades, counts)
plt.xlabel('Decade')
plt.ylabel('Number of Movies Released')
plt.title('Movies Released by Decade')
plt.show()
