# -*- coding: utf-8 -*-
"""Final LinearRegression Justina Asanmoa

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tTMDGROlnejCUJreHiFh01ap5o8Q0tu7
"""

# Importing Everything Here to make it easy
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import sklearn.metrics

#importing datasets

# Student preformance
df = pd.read_csv('/content/drive/My Drive/Colab Notebooks/student_performance.csv')
print(df.columns)

df2 = pd.read_csv('/content/drive/My Drive/Colab Notebooks/Student_performance_data.csv')
print(df2.columns)

model = LinearRegression()
X = df[['StudyHoursPerWeek']]
y = df['FinalGrade']
model.fit(X,y)

plt.title('Final Grade vs Attendance Rate')
plt.scatter(X,y)
plt.xlabel('Final Grade')
plt.ylabel('Attendance Rate')
plt.plot(X,model.predict(X),color='red')
plt.show()

mse = sklearn.metrics.mean_squared_error(y,model.predict(X))
print(mse)

model2 = LinearRegression()
x = df2[['StudyTimeWeekly']] # Changed this line to create a DataFrame
y = df2['GPA']
model2.fit(x,y)

plt.title('Study Time vs Grade Class')
plt.scatter(x,y)
plt.xlabel('Study Time Weekly')
plt.ylabel('Grade Class')

plt.plot(x,model2.predict(x),color='red')
plt.show()

mse = sklearn.metrics.mean_squared_error(y,model2.predict(x))
print(mse)