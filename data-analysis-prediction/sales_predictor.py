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
