import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data(file_path):
    """Load sales data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        data['Date'] = pd.to_datetime(data['Date'])  # Convert dates to datetime objects
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def analyze_data(data):
    """Perform basic data analysis."""
    print("Data Summary:")
    print(data.describe())

    print("\nData Types:")
    print(data.dtypes)


def visualize_data(data):
    """Visualize the sales data."""
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=data['Date'], y=data['Sales'], marker='o', label='Sales')
    plt.title("Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()
    plt.grid(True)
    plt.show()
