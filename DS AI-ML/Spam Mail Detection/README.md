# Email Spam Detection

The "Email Spam Detection" project focuses on classifying emails as spam or ham (non-spam) using a logistic regression model with TF-IDF feature extraction. The dataset "mail_data.csv" contains email messages along with their corresponding labels (spam or ham).

## Project Overview

1. **Data Loading**: The project loads the email data from the "mail_data.csv" file into a pandas DataFrame.

2. **Data Preprocessing**: Null values in the dataset are replaced with empty strings.

3. **Label Encoding**: Spam emails are labeled as 0, and ham emails are labeled as 1.

4. **Data Splitting**: The data is split into training and test sets using the `train_test_split` function from scikit-learn.

5. **Feature Extraction**: Text data is converted into feature vectors using the Term Frequency-Inverse Document Frequency (TF-IDF) vectorizer.

6. **Model Training**: A logistic regression model is trained with the training data.

7. **Model Evaluation**: The accuracy scores of the model are computed on both the training and test data.

8. **Spam Detection**: An example email is provided to demonstrate how the model predicts whether it is spam or ham.

## Dependencies

This project requires the following Python libraries:

- numpy
- pandas
- sklearn.model_selection.train_test_split
- sklearn.feature_extraction.text.TfidfVectorizer
- sklearn.linear_model.LogisticRegression
- sklearn.metrics.accuracy_score



## Conclusion

The "Email Spam Detection" project showcases the application of logistic regression with TF-IDF feature extraction for classifying emails as spam or ham. By analyzing email messages' contents, the model can predict whether an email is likely to be spam or not. The project's results can be useful in identifying and filtering out potential spam emails.
