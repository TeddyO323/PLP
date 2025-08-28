import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

def load_dataset():
    """
    Loads the Iris dataset from sklearn and converts it to a Pandas DataFrame.
    Includes error handling for unexpected issues.
    """
    try:
        iris = load_iris(as_frame=True)
        df = iris.frame
        df['species'] = iris.target_names[iris.target]
        return df
    except Exception as e:
        print("Error loading dataset:", e)
        return None


def explore_dataset(df):
    """Displays the first few rows, info, and checks for missing values."""
    print("🔍 First 5 rows of dataset:")
    print(df.head(), "\n")

    print("📊 Dataset info:")
    print(df.info(), "\n")

    print("❓ Missing values check:")
    print(df.isnull().sum(), "\n")

    # Clean missing values if any
    df = df.dropna()
    return df


def basic_analysis(df):
    """Performs basic statistical analysis and groupings."""
    print("📈 Descriptive statistics:")
    print(df.describe(), "\n")

    # Grouping example
    print("📊 Average sepal length by species:")
    grouped = df.groupby("species")["sepal length (cm)"].mean()
    print(grouped, "\n")


def visualize_data(df):
    """Creates 4 plots: line chart, bar chart, histogram, scatter plot."""
    plt.figure(figsize=(10, 6))

    # 1. Line chart: cumulative mean sepal length over index
    df["sepal length cummean"] = df["sepal length (cm)"].expanding().mean()
    plt.plot(df.index, df["sepal length cummean"], label="Cumulative Mean Sepal Length")
    plt.title("Line Chart: Cumulative Mean Sepal Length")
    plt.xlabel("Index")
    plt.ylabel("Sepal Length (cm)")
    plt.legend()
    plt.show()

    # 2. Bar chart: average petal length per species
    plt.figure(figsize=(8, 5))
    sns.barplot(x="species", y="petal length (cm)", data=df, ci=None)
    plt.title("Bar Chart: Avg Petal Length by Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Length (cm)")
    plt.show()

    # 3. Histogram: distribution of sepal width
    plt.figure(figsize=(8, 5))
    plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
    plt.title("Histogram: Sepal Width Distribution")
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Frequency")
    plt.show()

    # 4. Scatter plot: sepal length vs petal length
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df)
    plt.title("Scatter Plot: Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title="Species")
    plt.show()


if __name__ == "__main__":
    df = load_dataset()
    if df is not None:
        df = explore_dataset(df)
        basic_analysis(df)
        visualize_data(df)
