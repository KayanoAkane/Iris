from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import dataset

iris2 = dataset.iris2

iris_split = train_test_split(iris2, test_size=45)
X_train = iris_split[0].iloc[:, :4]
y_train = np.ravel(iris_split[0].iloc[:, 5])
X_test = iris_split[1].iloc[:, :4]
y_test = np.ravel(iris_split[1].iloc[:, 5])

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)
predict1 = model.predict(X_test)
print("實際的資料")
print(y_test)
print("預測的資料")
print(predict1)
print("模型訓練的成果(準確率)")
print(accuracy_score(y_test, predict1))
print("-"*70)