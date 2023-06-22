import pandas as pd

# Load the dataset into a pandas dataframe
df = pd.read_csv('data.csv')

# Print the first five rows of the dataframe
print(df.head())

# Calculate summary statistics for the numerical columns
print(df.describe())

import pandas as pd

# Load the dataset into a pandas dataframe
df = pd.read_csv('data.csv')

# Replace missing values with the mean
df.fillna(df.mean(), inplace=True)

# Convert categorical variables to numerical
df = pd.get_dummies(df, columns=['Category'])

# Scale the numerical variables
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df[['Variable1', 'Variable2']] = scaler.fit_transform(df[['Variable1', 'Variable2']])

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the dataset into a pandas dataframe
df = pd.read_csv('data.csv')

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[['Variable1', 'Variable2']], df['Target'], test_size=0.2)

# Fit a linear regression model to the training data
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Evaluate the performance of the model
from sklearn.metrics import r2_score
print('R-squared:', r2_score(y_test, y_pred))
