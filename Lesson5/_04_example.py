# pip install numpy
# pip install pandas
# pip install matplotlib
# pip install sklearn

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.metrics import r2_score # coefficiente di determinazione (1=best, <<0 worse)
from sklearn.linear_model import Lasso
# dataframe
train_data = pd.read_excel('Lesson5/_04_example.xlsx', sheet_name='train')
test_data = pd.read_excel('Lesson5/_04_example.xlsx', sheet_name='test')

X_train = train_data.drop(['DATE', 'Target'], axis=1)
Y_train = train_data[['Target']] # implements def __getitem__(self, i):
X_test = test_data.drop(['DATE', 'Target'], axis=1)
Y_test = test_data[['Target']]

# plt.scatter(X_train['F1'].values, Y_train.values)
# plt.show(block=True)

model = Lasso(alpha=0.9)
model.fit(X_train, Y_train)
Y_train_pred = model.predict(X_train)
Y_test_pred = model.predict(X_test)

for pos, coefficient in enumerate(model.coef_, start=1):
    print(f"f{pos} = {coefficient:.6f}")

plt.figure()
plt.title("TRAIN")
plt.suptitle(f"r^2 on train data : { r2_score(Y_train_pred, Y_train.values) }")
plt.plot(Y_train_pred, 'r')
plt.plot(Y_train.values)
plt.show(block=True)



plt.title("TEST")
plt.suptitle(f"r^2 on test data : { r2_score(Y_test_pred, Y_test.values) }")
plt.plot(Y_test_pred, 'r')
plt.plot(Y_test.values)
plt.show(block=True)