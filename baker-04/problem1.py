import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets
from numpy import genfromtxt
from sklearn.model_selection import KFold
import time

def genDataSet(N):
    x = np.random.normal(0, 1, N)
    ytrue = (np.cos(x) + 2) / (np.cos(x ∗ 1.4) + 2)
    noise = np.random.normal(0, 0.2, N)
    y = ytrue + noise
    return x, y, ytrue

X, y, ytrue = genDataSet(1000)
X = X.reshape((len(X),1))
bestk=[]
kc=0
for n_neighbors in range(1,900,2):
  kf = KFold(n_splits=10)
  kscore=[]
  k=0
  for train, test in kf.split(X):
    X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
  
    reg = neighbors.KNeighborsRegressor(n_neighbors, weights='distance')
    reg.fit(X_train, y_train)
  
    kscore.append(abs(reg.score(X_test,y_test)))
    #print kscore[k]
    k=k+1
  
  print (n_neighbors)
  bestk.append(sum(kscore)/len(kscore))
  print (bestk[kc])
  kc+=1

print (bestk) 
#from here we need to find the three best k's and their n_nearestneighbors
best = -1
bestn = -1
second = -1
secondn = -1
third = -1
thirdn= -1
for index in range(len(bestk)):
    if(bestk[index]>best):
        thirdn = secondn
        secondn = bestn
        bestn = index
        third = second
        second =best
        best = bestk[index]
    elif(bestk[index]>second):
        thirdn = secondn
        secondn = index
        third = second
        second =bestk[index]
    elif(bestk[index]>third):
        thirdn = index
        third =bestk[index]

print(best, second, third)
print(bestn*2+1,secondn*2+1,thirdn*2+1)

plt.plot(X,y,'.')
plt.plot(X,ytrue,'rx')
plt.show()
       