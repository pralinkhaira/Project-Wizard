# Bengaluru House Price Prediction

## Project Description

The project involves several steps:

1. **Data Loading**: The data is loaded from a CSV file using pandas.

2. **Data Cleaning**: The data is cleaned by removing unnecessary columns, handling missing values, and converting certain features into a more usable format.

3. **Exploratory Data Analysis (EDA)**: The data is explored using various techniques, such as calculating descriptive statistics, creating box plots, and generating a correlation heatmap.

4. **Feature Engineering**: New features are created from existing ones to improve the model's performance. For example, the 'size' feature is split into 'bedrooms' and 'bathrooms'.

5. **Model Building**: A Ridge regression model is built using a pipeline that includes one-hot encoding for categorical variables.

6. **Model Evaluation**: The model's performance is evaluated using the Mean Absolute Error (MAE) and Mean Absolute Percentage Error (MAPE).

7. **Prediction**: A function is created to make predictions using the trained model. This function takes as input the total square footage, number of bathrooms, number of bedrooms, and location, and returns the predicted price.

## Dependencies

This project requires the following Python libraries:

- pandas
- seaborn
- matplotlib
- ipywidgets
- sklearn
- category_encoders

## Usage

To use this project, you need to run the provided Python script. You can also interact with the model using the provided widgets, which allow you to specify the total square footage, number of bathrooms, number of bedrooms, and location.

## Conclusion

This project demonstrates how to build a machine learning model for predicting house prices. It involves various steps, including data cleaning, exploratory data analysis, feature engineering, model building, and model evaluation. The final model can be used to make predictions about house prices in Bengaluru based on the total square footage, number of bathrooms, number of bedrooms, and location.

## Acknowledgement

The dataset used in this project is provided by [www.Kaggl.com](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)
