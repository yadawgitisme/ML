import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

#splitting the data into test set and training set

x_train = pd.read_csv("Linear_X_Train.csv")
y_train = pd.read_csv("Linear_Y_Train.csv")
x_test  = pd.read_csv("Linear_X_Test.csv")

#sometimes using file names works but when it doesn't one can use this method too
#x_test  = pd.read_csv(r"C:\file_path\python\ML\regression\Linear_X_Test.csv")

#training the model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)
y_test = regressor.predict(x_test)

#plotting training set
plt.scatter(x_train, y_train, color = "teal", edgecolors="black")
plt.plot(x_train, regressor.predict(x_train) , color = "red")
plt.title("Time spent on coding vs Marks Scored")
plt.xlabel("Time spent")
plt.ylabel("Marks")
plt.show()

#plt.scatter(x_test, y_test, color = "teal", edgecolors="black")
#plt.plot(x_train, regressor.predict(x_train) , color = "red")
#plt.title("Time spent on coding vs Marks Scored")
#plt.xlabel("Time spent")
#plt.ylabel("Marks")
#plt.show()
