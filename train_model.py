import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

data = pd.read_csv("data/kc_house_data.csv")

features = ['bedrooms', 'bathrooms', 'sqft_living', 'floors', 'zipcode']
target = ["price"]
X = data[features]
y = data[target]

#So we’ll split the data into 2 parts:
#1.Training set — for teaching the model
#2.Test set — for checking how good it is
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# LinearRegression model as our training model
# create model
model = LinearRegression()
# train the model using training data
model.fit(X_train, y_train)

# checks how good is the prediction from reality

# makes predictions on the test set
y_pred = model.predict(X_test)
# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error on test data: {mse:.2f}")

# save the model
joblib.dump(model, "app/house_model.joblib")