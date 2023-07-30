# Diabetes Prediction using Support Vector Machine (SVM)
## Demo

https://github.com/sumantadey-ui/diabetesPrediction/assets/113798132/36c816a0-aaae-42c5-b7f8-c8b7f04c9334

# Diabetes Prediction using Support Vector Machine (SVM)


## Table of Contents
Introduction <br>
Dataset<br>
Dependencies<br>
Installation<br>
Usage<br>
Results<br>
Contributing<br>
License<br>

## Introduction
This repository contains a machine learning project that focuses on predicting the likelihood of an individual having diabetes using the Support Vector Machine (SVM) algorithm. The goal of this project is to develop a predictive model that can assist in early diabetes detection, which may lead to timely intervention and better patient outcomes.

## Dataset
The dataset used in this project contains various health-related features and a binary target variable indicating whether a person has diabetes or not. The dataset can be found in the data/ directory of this repository (data/diabetes.csv). It consists of the following columns:

Pregnancies: Number of times pregnant
Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
BloodPressure: Diastolic blood pressure (mm Hg)
SkinThickness: Triceps skinfold thickness (mm)
Insulin: 2-Hour serum insulin (mu U/ml)
BMI: Body mass index (weight in kg/(height in m)^2)
DiabetesPedigreeFunction: Diabetes pedigree function (a function that scores the likelihood of diabetes based on family history)
Age: Age in years
Outcome: Target variable (0 - Non-diabetic, 1 - Diabetic)

## Dependencies
To run the project successfully, you need the following dependencies:

Python 3.x<br>
NumPy<br>
Pandas<br>
Scikit-learn<br>
## Installation<br>
Clone this repository to your local machine or download it as a ZIP file.<br>
Ensure you have Python 3.x installed on your system.<br>
Install the required libraries by running the following command:<br>
Copy code<br>
pip install numpy pandas scikit-learn<br>
## Usage
Before running the code, make sure you have the dataset file diabetes.csv in the data/ directory.<br>
Open a terminal or command prompt in the project's root directory.<br>
Run the diabetes_prediction.py script to train the SVM model and make predictions:<br>
Copy code<br>
python diabetes_prediction.py<br>
The script will train the SVM model on the dataset and display the evaluation metrics such as accuracy, precision, recall, and F1-score.<br>
It will also save the trained model as svm_diabetes_model.pkl, which can be used for future predictions.<br>
Results
After running the script, you will get the evaluation metrics for the SVM model's performance on the test data. These metrics will give you insights into how well the model is predicting diabetes cases.

Additionally, you can use the trained SVM model (svm_diabetes_model.pkl) to predict diabetes for new data points.

## Contributing
If you wish to contribute to this project, you can do so by opening issues for bugs or new features, submitting pull requests, or providing feedback and suggestions.

## License
This project is licensed under the MIT License. Feel free to use and modify the code as per the terms of the license.
