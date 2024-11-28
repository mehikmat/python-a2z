from sales_analyzer import load_data, analyze_data, visualize_data
from sales_predictor import prepare_data, predict_future_sales, train_model, evaluate_model


def main():
    # Load and analyze data
    file_path = "sales_data.csv"
    data = load_data(file_path)

    if data is None:
        print("Failed to load data. Exiting.")
        return

    print(f"Raw data:\n {data}")

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
