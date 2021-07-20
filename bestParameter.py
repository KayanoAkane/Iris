import training
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

X_train = training.X_train
y_train = training.y_train
X_test = training.X_test
y_test = training.y_test

list1 = []
for x in range(10):
    params1 = {"n_neighbors": [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]}
    model = GridSearchCV(KNeighborsClassifier(), params1, verbose=3)
    print("開始進行訓練")
    model.fit(X_train, y_train)
    print("最佳參數")
    print(model.best_params_)
    dict1 = model.best_params_
    list1.append(dict1["n_neighbors"])
    print("最佳模型")
    print(model.best_estimator_)

list2 = np.array(list1)
print("10次迴圈中分別產出的最佳參數:", list1)
print("我們也可以利用這10個參數的平均值: ", list2.mean(), "做為新的最佳參數")