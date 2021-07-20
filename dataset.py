from sklearn import datasets
import pandas as pd
iris = datasets.load_iris()
print(iris)
print(iris.keys())
print(iris["data"])
print()
print(iris["target"])
print()
print(iris["target_names"])
print()
print(iris["feature_names"])
print()
print(len(iris["data"]))
species = [iris.target_names[x] for x in iris.target]
print(species)
print("將iris.data轉換為DataFrame")
iris2 = pd.DataFrame(iris.data, columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
iris2["species"] = species
iris2["level"] = iris.target
print(iris2)