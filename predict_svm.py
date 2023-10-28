import pandas as pd
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from prev_year_data import current_data
regressor = SVR(kernel = 'rbf')

day = int(input())
month = int(input())
year = int(input())
state = input()
gas = input()

state = state.lower()

state_codes = {
    "connecticut": 9,
    "maine": 23,
    "massachusetts": 25,
    "new hampshire": 33,
    "new jersey": 34,
    "new york": 36,
    "pennsylvania": 42,
    "rhode island": 44,
    "vermont": 50
}

excel_file = "final_data.xlsx" 
df = pd.read_excel(excel_file)

df['Date Local'] = pd.to_datetime(df['Date Local'])

mean_data = df.groupby(['Date Local', 'State Code', 'Parameter Name'])['Arithmetic Mean'].mean().reset_index()

mean_data['Year'] = mean_data['Date Local'].dt.year
mean_data['Month'] = mean_data['Date Local'].dt.month
mean_data['Day'] = mean_data['Date Local'].dt.day 

target_gas = gas
target_state = state_codes[state]

target_data = mean_data[(mean_data['Parameter Name'] == target_gas) & (mean_data['State Code'] == target_state)]

train_data, test_data = train_test_split(target_data, test_size=0.2, shuffle=False)

X_train = train_data[['Year', 'Month', 'Day']]
y_train = train_data['Arithmetic Mean']
X_test = test_data[['Year', 'Month', 'Day']]
y_test = test_data['Arithmetic Mean']

regressor.fit(X_train, y_train)

train_predictions = regressor.predict(X_train)
test_predictions = regressor.predict(X_test)

future_date_features = [[year, month, day]]

future_prediction_linear = regressor.predict(future_date_features)
prev_data = current_data(day, month, year, target_state, target_gas)
print("Predicted mean value for future date with SVM:", round(future_prediction_linear[0], 6))
print("The Value for the day", day, month, (year-1), "for gas", target_gas, "for state", state, "was: ", round(prev_data, 6))
print("The accuracy is: ", round(future_prediction_linear[0]/prev_data*100, 2))