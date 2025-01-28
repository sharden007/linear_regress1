# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import json
import matplotlib.pyplot as plt

# Step 1: Load the data from an external JSON file
def load_data(file_path):
    """
    Load sales data from a JSON file into a Pandas DataFrame.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return pd.DataFrame(data)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# Step 2: Prepare the data for Linear Regression
def prepare_data(df):
    """
    Prepare features and target variable for training and testing.
    """
    # Select features and target variable
    features = ['Age', 'Frequency (for visits)', 'Coffee', 'Cold drinks', 'Jaws chip', 
                'Pastries', 'Juices', 'Sandwiches', 'cake']
    target = 'Average Purchase ($)'

    X = df[features]
    y = df[target]

    # Split the data into training and testing sets
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the Linear Regression model
def train_model(X_train, y_train):
    """
    Train a linear regression model using the training data.
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

# Step 4: Evaluate the model
def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model using Mean Squared Error and R-squared metrics.
    """
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    print("Model Evaluation:")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"R-squared Score: {r2:.2f}")
    
    return predictions

# Step 5: Save predictions to a CSV file
def save_predictions(y_test, predictions, output_file):
    """
    Save the actual and predicted values to a CSV file.
    """
    results = pd.DataFrame({
        'Actual': y_test.values,
        'Predicted': predictions
    })
    results.to_csv(output_file, index=False)
    print(f"Predictions saved to {output_file}")

# Step 6: Visualize the results
def visualize_results(y_test, predictions):
    """
    Plot actual vs predicted values.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, predictions, alpha=0.7, color='blue')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')
    plt.title('Actual vs Predicted Average Purchase ($)')
    plt.xlabel('Actual Average Purchase ($)')
    plt.ylabel('Predicted Average Purchase ($)')
    plt.grid(True)
    plt.show()

# Main function to execute the workflow
def main():
    # Load data from external JSON file
    file_path = 'starbucks.json'  # Ensure this file exists in the same directory
    df = load_data(file_path)

    if df is None:
        print("Failed to load data. Exiting.")
        return

    # Prepare data for training and testing
    X_train, X_test, y_train, y_test = prepare_data(df)

    # Train the linear regression model
    model = train_model(X_train, y_train)

    # Evaluate the trained model
    predictions = evaluate_model(model, X_test, y_test)

    # Save predictions to a CSV file
    save_predictions(y_test, predictions, 'predictions.csv')

    # Visualize the results
    visualize_results(y_test, predictions)

if __name__ == "__main__":
    main()
