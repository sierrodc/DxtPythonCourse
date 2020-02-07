##############################################
## 01: REGRESSIONE LINEARE SEMPLICE
##  y = f(x) = b + wx
## Residual Sum of Squares (RSS) = sum_i[(y_i - (b+wx_i))^2]             OTTIMO = 1
## Mean Squared error (MSE) = sum_i[(y_i - (b+wx_i))^2] / max(i)         MEDIA DEL QUADRATO DEGLI ERRORI, OTTIMO=0
##############################################

import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sb

# dati case a boston
# MEDV = valore medio
house = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data",
        sep="\s+", names=["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PRATIO", "B", "LSTAT", "MEDV"])

print(house.head(5))

sb.heatmap(house.corr(), xticklabels=house.columns, yticklabels=house.columns, annot=True, annot_kws={'size': 12})
plt.show(block=True)

cols = ["RM", "LSTAT", "PRATIO", "TAX", "INDUS", "MEDV"]
sb.heatmap(house[cols].corr(), xticklabels = cols, yticklabels = cols, annot=True, annot_kws={'size': 12})
#sb.pairplot(boston[cols]) # 
plt.show(block=True)


X = house[["RM", "LSTAT"]].values
Y = house["MEDV"].values

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)

lr = LinearRegression()
lr.fit(X_train, Y_train)
Y_pred = lr.predict(X_test)

print(list(zip(cols, lr.coef_)))

from sklearn.preprocessing import PolynomialFeatures
# transorm [ [a] , [b], [c]...] to [ [1,a,a^2...], [1,b,b^2...], [1,c,c^2...] ...]

for i in range(1, 11): #from 1 to 10
    pf = PolynomialFeatures(degree=i)
    X_train_poly = pf.fit_transform(X_train)
    X_test_poly = pf.transform(X_test)
    lr = LinearRegression()
    lr.fit(X_train_poly, Y_train)
    Y_pred = lr.predict(X_test_poly)
    print(f"1-var {i} degree MSE: {mean_squared_error(Y_test, Y_pred)} R2 SCORE: {r2_score(Y_test, Y_pred)}")