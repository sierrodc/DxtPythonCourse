# pip install numpy
# pip install pandas
# pip install matplotlib
# pip install sklearn

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.metrics import r2_score
from sklearn.linear_model import Lasso
train_data = pd.read_excel('Lesson5/_10_extra.xlsx', sheet_name='train')
test_data = pd.read_excel('Lesson5/_10_extra.xlsx', sheet_name='test')

X_train = train_data.drop(['DATE', 'Target'], axis=1)
Y_train = train_data[['Target']]
X_test = test_data.drop(['DATE', 'Target'], axis=1)
Y_test = test_data[['Target']]

# plt.scatter(X_train['F1'].values, Y_train.values)
# plt.show(block=True)

model = Lasso(alpha=0.9)
model.fit(X_train, Y_train)
Y_train_pred = model.predict(X_train)
Y_test_pred = model.predict(X_test)

plt.figure()
plt.subplot(1, 2, 1)
plt.title("TRAIN")
plt.plot(Y_train_pred, 'r')
plt.plot(Y_train.values)
plt.subplot(1, 2, 2)
plt.title("TEST")
plt.plot(Y_test_pred, 'r')
plt.plot(Y_test.values)
plt.show(block=True)

print(f"r^2 on train data : { r2_score(Y_train_pred, Y_train.values) }")
print(f"r^2 on test data : { r2_score(Y_test_pred, Y_test.values) }")

print(model.coef_)