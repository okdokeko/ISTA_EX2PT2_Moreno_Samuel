# I guess I will also add my algorithm and validation here as per the steps. # My code for linear reg from hw 3: (I had to add the r_squared feature to work with the code from medium)
class MyLinearReg():
    # Here I am creating a constructor for my class
    def __init__(self, learning_rate, it):
        self.learning_rate = learning_rate # This if for gradient descent
        self.it = it # This is for gradient decent
        
    # This trains the model
    def fit(self, X, Y):
        # Initializing X and Y
        X = np.array(X)
        Y = np.array(Y)
        
        # n is the number of features (2)
        self.m, self.n = X.shape 
        
        # Initializing my weight
        self.B = np.zeros(self.n) # Modified this to allow for more B
        self.b_0 = 0
        self.X = X
        self.Y = Y
        
        # This is the gradient decent
        for i in range(self.it):
            self.update_weights()
        return self
    
    # This is the implementation of gradient decent formula
    def update_weights(self):
        Y_pred = self.predict(self.X)
        dB = -(2 * (self.X.T).dot(self.Y - Y_pred)) / self.m
        db_0 = -2 * np.sum(self.Y - Y_pred) / self.m
        
        # Here the weight is adjusted according to the learning rate.
        self.B = self.B - self.learning_rate * dB
        self.b_0 = self.b_0 - self.learning_rate * db_0
        
        return self
    
    def predict(self, X):
        return X.dot(self.B) + self.b_0 
    
    def describe(self):
        print("The values of B is:", self.B)
        print("The value of B_0 is: ", self.b_0)
        
    # I had to add this for the forward stepwise, i just used the r^2 formula we have covered in book/class
    # also used this for formula: https://en.wikipedia.org/wiki/Coefficient_of_determination
    def r_squared(self):
        y_pred = self.predict(self.X)
        ss_res = np.sum((self.Y - y_pred) ** 2)
        ss_tot = np.sum((self.Y - np.mean(self.Y)) ** 2)
        r2 = 1 - (ss_res / ss_tot)
        return r2

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

hospital = pd.read_csv("FY_2025_Hospital_Readmissions_Reduction_Program_Hospital.csv")

print(f'Total Columns: {len(hospital)}')
print (hospital["Footnote"].isnull().sum() + hospital["Excess Readmission Ratio"].isnull().sum())
# So Footnote and excess Readmission Ratio, Predicted Readmission Rate, Expected Readmission Rate, and Number of Readmissions are mutually exclusive.    
    
# First I wanna clean up my dataset (drop footnote first)
hospital.drop(['Footnote'], axis=1, inplace=True)  # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html
hospital.dropna(subset = ['Number of Readmissions'], inplace=True) # https://www.statology.org/pandas-dropna-specific-column/
# I think I have enough data to drop na num of discharges:
hospital.dropna(subset = ['Number of Discharges'], inplace=True) # https://www.statology.org/pandas-dropna-specific-column/
print(hospital.isnull().sum())     

hospital.dtypes
hospital["Number of Readmissions"] = hospital["Number of Readmissions"].replace("Too Few to Report", 0) # https://stackoverflow.com/questions/27060098/replacing-few-values-in-a-pandas-dataframe-column-with-another-value
hospital["Number of Readmissions"] = pd.to_numeric(hospital["Number of Readmissions"], errors='coerce') #https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_numeric.html

# I basically turned the readmissions that are too few into 0 so I can include them
sns.pairplot(hospital)
plt.show()
    
# Fitting model with everything but Expected Readmission Rate:
X = hospital[['Number of Discharges', 'Predicted Readmission Rate', 'Excess Readmission Ratio']]
Y = hospital['Number of Readmissions']

model = MyLinearReg(learning_rate=0.000001, it=10000)

model.fit(X, Y)

model.describe()
model.r_squared()

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

model_sklearn = LinearRegression()
model_sklearn.fit(X, Y)

# Calculate coefficients and r squared
print("sklearn coefficient (B):", model_sklearn.coef_)
print("sklearn intercept (B_0):", model_sklearn.intercept_)

Y_pred_sklearn = model_sklearn.predict(X)

r2_sklearn = r2_score(Y, Y_pred_sklearn)

print(f"sklearn R-squared: {r2_sklearn}")