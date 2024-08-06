# Titanic Data Analysis and Prediction

This repository contains a Jupyter Notebook that performs data analysis and prediction on the Titanic dataset. The main goal is to predict the survival of passengers based on various features.

## Overview

The notebook is divided into several sections:
1. **Importing Libraries**: Import necessary libraries such as `numpy`, `pandas`, `matplotlib`, `seaborn`, and `sklearn`.
2. **Loading Data**: Load the training and testing data from CSV files.
3. **Exploratory Data Analysis (EDA)**: Analyze the data to understand the distribution of features and their relationships with the target variable.
4. **Data Preprocessing**: Handle missing values, encode categorical variables, and normalize numerical features.
5. **Model Training**: Train a Random Forest classifier to predict the survival of passengers.
6. **Prediction**: Use the trained model to make predictions on the test data.
7. **Submission**: Save the predictions to a CSV file for submission.

## Instructions

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Required libraries: `numpy`, `pandas`, `matplotlib`, `seaborn`, `sklearn`

### Steps to Run

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/titanic-analysis.git
    ```
2. **Navigate to the repository**:
    ```sh
    cd titanic-analysis
    ```
3. **Install the required libraries**:
    ```sh
    pip install -r requirements.txt
    ```
4. **Run the Jupyter Notebook**:
    ```sh
    jupyter notebook titanicdatos.ipynb
    ```

### Data Description

- `train.csv`: The training dataset containing features and the target variable (`Survived`).
- `test.csv`: The test dataset containing features for which we need to predict the target variable.

### Notebook Sections

1. **Importing Libraries**:
    - Import necessary libraries for data manipulation, visualization, and machine learning.

```bash
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder
```

2. **Loading Data**:
    - Load the training and testing datasets using `pandas`.
```bash
df_train = pd.read_csv('/kaggle/input/titanic/train.csv')
df_test = pd.read_csv('/kaggle/input/titanic/test.csv')
```


3. **Exploratory Data Analysis (EDA)**:
    - Visualize the distribution of the `Survived` variable.
    - Analyze categorical and numerical features.
    - Check for missing values and their impact on the dataset.

```bash
df_train.sample(5)
```

```bash
df_train.shape
```
```bash
df_train.info()
```
### valores duplicados
```bash
df_train.duplicated().sum()
```
```bash
df_train.isnull().sum().sort_values(ascending=False)
```

### Determinar valores nulos del dataframe
```bash
df_train.nunique()
```


### Determinar valores de dataset
```bash
columnas_categoricas = df_train.select_dtypes(include=['object']).columns

for column in columnas_categoricas:
    if df_train[column].nunique()<=10:
        print(f"{column}: {df_train[column].unique()}")
```


### Determinar valores de dataset
```bash
columnas_categoricas = df_train.select_dtypes(include=['int64','float64']).columns

for column in columnas_categoricas:
    if df_train[column].nunique()<=10:
        print(f"{column}: {df_train[column].unique()}")
```
### EDA
```bash
sns.countplot(x='Survived',data=df_train)
plt.show
```

```bash
sns.barplot(x='Sex',y='Survived',data = df_train)
plt.show
```

#### Analisis
- Passengerld, Cabin, Fare, ticket, no a la prediccion del modelo, debido a los valores nulos 

```bash
df_train=df_train.drop(columns=['Cabin','Fare','Ticket','Name'])
df_test=df_test.drop(columns=['Cabin','Fare','Ticket','Name'])

df_train.head()
```

4. **Data Preprocessing**:
    - Impute missing values using `SimpleImputer`.
    - Encode categorical variables using `OrdinalEncoder`.
    - Normalize numerical features.
```bash
X = df_train.drop(['Survived'],axis=1)
Y = df_train['Survived']
```
```bash
s = (X.dtypes=='object')
object_cols=list(s[s].index)

ordinal_encoder=OrdinalEncoder()
X[object_cols]=ordinal_encoder.fit_transform(X[object_cols])
```

```bash
X.head()
```

### LLenar valores nulos

```bash
imputer = SimpleImputer()
x_transformed = pd.DataFrame(imputer.fit_transform(X))
x_transformed.columns=X.columns
```


```bash
x_transformed.isnull().sum()
```
5. **Model Training**:
    - Train a `RandomForestClassifier` using the preprocessed training data.
```bash
model = RandomForestClassifier()
model.fit(x_transformed,Y)
```
6. **Prediction**:
    - Transform the test data and make predictions using the trained model.
```bash
df_test[object_cols]=ordinal_encoder.fit_transform(df_test[object_cols])

df_test_transformed = pd.DataFrame(imputer.transform(df_test))
df_test_transformed.columns=df_test.columns

predictions = model.predict(df_test_transformed)
```
7. **Submission**:
    - Create a DataFrame with `PassengerId` and `Survived` predictions.
    - Save the predictions to `submission.csv`.
```bash
output = pd.DataFrame({'PassengerId':df_test.PassengerId,'survived':predictions})
output.to_csv('submission.csv', index=False)
```
### Conclusion

This notebook provides a comprehensive approach to analyze and predict Titanic survivors using machine learning techniques. Feel free to explore and modify the notebook to improve the model's performance.

## Author

- [Your Name](https://github.com/xXThanatosXx)


