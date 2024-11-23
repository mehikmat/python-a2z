Mini-Project: Sales Data Analysis and Prediction

Objective:
Analyze and visualize sales data using Python.
Build a basic linear regression model to predict future sales.
Python Concepts and Libraries Used:
File Handling: Reading and writing CSV files.
Data Manipulation: Using pandas.
Data Visualization: Using matplotlib and seaborn.
Linear Regression: Using scikit-learn.
Logging: For tracking errors and progress.
Step 1: Dataset Preparation
Dataset:
Prepare a dataset in CSV format (or download one from Kaggle). For simplicity, create a file named sales_data.csv with the following content:

csv
Copy code
Date,Sales
2023-01-01,200
2023-02-01,220
2023-03-01,250
2023-04-01,270
2023-05-01,300
2023-06-01,310
Step 2: Project Structure
bash
Copy code
sales_prediction/
├── sales_analyzer.py   # Contains data loading, analysis, and visualization functions.
├── sales_predictor.py  # Contains machine learning model implementation.
├── main.py             # Entry point for the application.
├── sales_data.csv      # Dataset.
Step 3: Code Implementation
1. Sales Analyzer Module
File: sales_analyzer.py
This module handles data loading, analysis, and visualization.

python
Copy code
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

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
2. Sales Predictor Module
File: sales_predictor.py
This module handles the machine learning logic (linear regression).

python
Copy code
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def prepare_data(data):
    """Prepare data for machine learning."""
    data['Month'] = data['Date'].dt.month
    X = data[['Month']]
    y = data['Sales']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    """Train a linear regression model."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """Evaluate the model on test data."""
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error: {mse:.2f}")
    return predictions

def predict_future_sales(model, future_months):
    """Predict future sales for the next few months."""
    future_data = pd.DataFrame({'Month': future_months})
    return model.predict(future_data)
3. Main Script
File: main.py
This is the entry point for the application.

python
Copy code
from sales_analyzer import load_data, analyze_data, visualize_data
from sales_predictor import prepare_data, train_model, evaluate_model, predict_future_sales

def main():
    # Load and analyze data
    file_path = "sales_data.csv"
    data = load_data(file_path)

    if data is None:
        print("Failed to load data. Exiting.")
        return

    analyze_data(data)
    visualize_data(data)

    # Prepare data for model training
    X_train, X_test, y_train, y_test = prepare_data(data)

    # Train and evaluate the model
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

    # Predict future sales
    print("\nPredicting future sales for the next 3 months...")
    future_months = [7, 8, 9]  # Example: July, August, September
    predictions = predict_future_sales(model, future_months)

    for month, sales in zip(future_months, predictions):
        print(f"Month {month}: Predicted Sales = {sales:.2f}")

if __name__ == "__main__":
    main()
Step 4: Running the Project
Save all the files (sales_analyzer.py, sales_predictor.py, and main.py) in the same directory as your dataset (sales_data.csv).

Run the project using the following command:

bash
Copy code
python main.py
Step 5: Output
Analysis Output:
Summary statistics (mean, median, etc.).
Data types for each column.
Visualization:
A line plot showing sales trends over time.

Prediction Output:
Predicted sales for future months.

Python Concepts Covered
Data Manipulation: pandas for loading and analyzing data.
Visualization: matplotlib and seaborn for data visualization.
Date Handling: Using datetime to extract useful information from dates.
Machine Learning:
Splitting data into training and testing sets.
Training a linear regression model using scikit-learn.
Evaluating model performance with metrics like mean squared error.
Modular Design: Code organized into reusable modules.
Next Steps
Extend the dataset with more features (e.g., marketing budget, region).
Experiment with advanced ML algorithms (e.g., decision trees or random forests).
Save the model using joblib for reuse.
This mini-project provides a practical introduction to Python tools commonly used in machine learning workflows. Let me know if you'd like further enhancements or additional guidance! 😊