import dataset
import matplotlib.pyplot as plt
import seaborn as sns

iris2 = dataset.iris2


def plot_iris(iris, col1, col2):
    sns.lmplot(x=col1, y=col2, data=iris, hue="species", fit_reg=True)
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()


plot_iris(iris2, "sepal_length", "sepal_width")
plot_iris(iris2, "petal_length", "petal_width")
plot_iris(iris2, "sepal_length", "petal_length")
plot_iris(iris2, "sepal_length", "petal_width")
plot_iris(iris2, "sepal_width", "petal_length")
plot_iris(iris2, "sepal_width", "petal_width")