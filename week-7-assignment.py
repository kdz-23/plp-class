# Part 1: Load and Explore the Dataset
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"  # Iris dataset
df = pd.read_csv(url)

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())


# Part 2: Basic Data Analysis

# Basic statistics
print("\nData Statistics:")
print(df.describe())

# Group by species and compute the mean of each numeric column
grouped = df.groupby('species').mean()
print("\nMean values grouped by species:")
print(grouped)

# Find any patterns
print("\nInteresting Finding:")
print("Versicolor seems to have intermediate petal and sepal sizes between Setosa and Virginica.")



# Part 3: Data Visualization

# Line Chart - Example: Line plot of sepal length for first 30 samples
plt.figure(figsize=(10, 6))
plt.plot(df['sepal_length'][:30], marker='o', label='Sepal Length')
plt.title('Sepal Length Trend for First 30 Samples')
plt.xlabel('Sample Index')
plt.ylabel('Sepal Length (cm)')
plt.legend()
plt.grid(True)
plt.show()

# Bar Chart - Average petal length per species
plt.figure(figsize=(8, 6))
grouped['petal_length'].plot(kind='bar', color=['skyblue', 'salmon', 'limegreen'])
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.xticks(rotation=45)
plt.show()

# Histogram - Distribution of petal width
plt.figure(figsize=(8, 6))
plt.hist(df['petal_width'], bins=20, color='purple', edgecolor='black')
plt.title('Distribution of Petal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot - Sepal length vs Petal length
plt.figure(figsize=(8, 6))
plt.scatter(df['sepal_length'], df['petal_length'], c='green', alpha=0.7)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.grid(True)
plt.show()
