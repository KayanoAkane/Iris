from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()
print(iris)
print("-"*70)
print("keys:\n", iris.keys())
print("-"*70)
print("data:\n", iris["data"])
print("-"*70)
print("target:\n", iris["target"])
print("-"*70)
print("target_names:\n", iris["target_names"])
print("-"*70)
print("feature_names:\n", iris["feature_names"])
print("-"*70)
print("length of data: ", len(iris["data"]))
print("-"*70)
species = [iris.target_names[x] for x in iris.target]
print("species\n", species)
print("-"*70)

iris2 = pd.DataFrame(iris.data, columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
iris2["species"] = species
iris2["level"] = iris.target
print("iris2:\n", iris2)
print("-"*70)