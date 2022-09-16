import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.metrics import r2_score, mean_squared_error
from mlxtend.evaluate import bias_variance_decomp
from mlxtend.evaluate import *
from sklearn import metrics
import random

#Importamos los datos de entrada
data = pd.read_csv('Fish.csv')

# Actualizamos las variables de interes para nuestro modelo
data['L123']= (data['Length1'] * data['Length2'] * data['Length3'])**(1/3)
data['WidthXL123'] = data['L123']*data['Width']
data.pop('Species')
data.pop('Length1')
data.pop('Length2')
data.pop('Length3')
data.sample(10)

#Matriz de correlacion del modelo actualizado
cor_d = data.corr()
cor_d.style.background_gradient (cmap = 'coolwarm')


# Separamos las caracteristicas y nuestra varible a predecir
x = data[['Height','Width','L123','WidthXL123']]
y = data[['Weight']]

#rands = [1, 4, 21, 105, 837]
rands = [] #Se van a crear 5 muestras aleatorias para entrenar y probar el modelo
for i in range(5):
    r = random.randint(0,1000)
    rands.append(r) #"""

for i in range(len(rands)):
  # Se corren para 5 muestras para cada modelo
  print("\t"*4+"MUESTRA",i+1)
  # Separamos un conjunto de datos para entrenar y otro para probar
  X_train, X_test, y_train, y_test = train_test_split(x,y, random_state=rands[i])
  X_train=X_train.values
  X_test = X_test.values
  y_train_bs = (y_train["Weight"]).values
  y_test_bs = (y_test["Weight"]).values
  # Llamamos a nuestra función para el modelo
  mlr = LinearRegression()
  # Ajuste de nuestro modelo
  mlr.fit(X_train, y_train)
  #Predicciónes del modelo
  y_hat_train = mlr.predict(X_train)
  y_hat_test = mlr.predict(X_test)
  # Validación para modelo lineal
  sc_train = r2_score(y_train, y_hat_train)
  sc_test = r2_score(y_test, y_hat_test)
  mse = mean_squared_error(y_test, y_hat_test)
  # Estimation of bias and variance using bias_variance_decomp
  mse_x, bias, var = bias_variance_decomp(mlr, X_train, y_train_bs, X_test, y_test_bs, loss='mse', num_rounds=200, random_seed=123)
  y_pred=mlr.predict(X_test)
  # Resumen de la prueba
  print('Avg Bias: %.3f' % bias)
  print('Avg Variance: %.3f' % var)
  print("\nRegresión Lineal Múltiple")
  print("R2_Train = "+ "{:.10}".format(sc_train*100)+ "%\tR2_Test = "+"{:.10}".format(sc_test*100)+"%\tECM = "+ "{:.10}".format(mse))
  # Hiperparametros para las técnicas de regularización
  a = 0.01
  its = 500
  t = 1e-8
  # Regresión L1 (Lasso)
  lasso_reg = linear_model.Lasso(alpha=a, max_iter=its, tol=t)
  lasso_reg.fit(X_train,y_train)
  #Predicciónes del modelo
  y_hat_test_lasso = lasso_reg.predict(X_test)
  # Validación con regulación L1
  sc_train = lasso_reg.score(X_train, y_train)
  sc_test = lasso_reg.score(X_test, y_test)
  mse = mean_squared_error(y_test, y_hat_test_lasso)
  print("Regresión L1 (Lasso)")
  print("R2_Train = "+ "{:.10}".format(sc_train*100)+ "%\tR2_Test = "+"{:.10}".format(sc_test*100)+"%\tECM = "+ "{:.10}".format(mse))
  # Regresión L2 (Ridge)
  ridge_reg = linear_model.Ridge(alpha=a, max_iter=its, tol=t)
  ridge_reg.fit(X_train,y_train)
  #Predicciónes del modelo
  y_hat_test_ridge = ridge_reg.predict(X_test)
  # Validación con regulación L1
  sc_train = ridge_reg.score(X_train, y_train)
  sc_test = ridge_reg.score(X_test, y_test)
  mse = mean_squared_error(y_test, y_hat_test_ridge)
  print("Regresión L2 (Ridge)")
  print("R2_Train = "+ "{:.10}".format(sc_train*100)+ "%\tR2_Test = "+"{:.10}".format(sc_test*100)+"%\tECM = "+ "{:.10}".format(mse))
