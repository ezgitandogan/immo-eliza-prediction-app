import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pickle
from sklearn.ensemble import RandomForestRegressor


df=pd.read_csv('final.csv')

# Separating features and target variable
X=df.drop('price',axis=1) 
y=df['price'] 

# Splitting the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Creating the randomforest regressor model
rf = RandomForestRegressor(n_estimators=100, random_state=42)

# Fitting the model to the training data
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)





# Evaluating the model's performance
print("R^2:", r2_score(y_test, y_pred))
print("randomforest:", mean_squared_error(y_test, y_pred))
print("randomforest MAE:", mean_absolute_error(y_test, y_pred))
print("Score:", rf.score(X_test, y_test))




# Save the model as a pickle file
pickle.dump(rf, open("randomforest_model.pkl", "wb"))




# Load the model from the pickle file
with open('randomforest_model.pkl', 'rb') as file:
    model = pickle.load(file)
