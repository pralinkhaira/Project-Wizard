# Employee Attrition Prediction

The "Employee Attrition Prediction" project aims to predict employee attrition using machine learning models. The dataset, "HR-Employee-Attrition.csv," contains various employee-related features, including job-level, monthly income, total working years, years at the company, years with the current manager, number of companies worked, percent salary hike, and attrition status.

## Project Overview

1. **Data Loading**: The project loads the employee attrition data from the "HR-Employee-Attrition.csv" file into a pandas DataFrame.

2. **Data Preprocessing**: The dataset is inspected to check for any missing values. The "Attrition" column is converted into binary format (0 for 'No' and 1 for 'Yes').

3. **Data Exploration**: Descriptive statistics and correlation analysis are performed to understand the data and identify potential patterns.

4. **Model Building**: A logistic regression model is built using the one-hot encoder to handle categorical variables.

5. **Model Evaluation**: The accuracy score of the logistic regression model is computed on the training data.

6. **Feature Importance**: The odds ratios of the features are calculated to identify the most important predictors of employee attrition.

7. **Confusion Matrix**: A confusion matrix is generated to visualize the performance of the model using the default threshold (0.5) and an adjusted threshold (0.7).

## Dependencies

This project requires the following Python libraries:

- pandas
- numpy
- seaborn
- matplotlib.pyplot
- sklearn.linear_model.LogisticRegression
- sklearn.metrics.accuracy_score
- sklearn.pipeline.make_pipeline
- sklearn.model_selection.train_test_split
- sklearn.metrics.ConfusionMatrixDisplay
- sklearn.metrics.confusion_matrix
- category_encoders.OneHotEncoder

## Usage

1. Clone this repository to your local machine.
2. Place the "HR-Employee-Attrition.csv" file in the same directory as the code files.
3. Run the provided Python script to execute the employee attrition prediction model.
4. The script will display the accuracy score of the logistic regression model and generate confusion matrices with default and adjusted thresholds.

## Conclusion

The "Employee Attrition Prediction" project showcases the application of logistic regression for predicting employee attrition. By analyzing various employee-related features, the model can provide valuable insights into potential attrition risks. The project's results and feature importance analysis aid in understanding the factors influencing employee attrition.
