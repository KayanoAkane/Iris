# Outline
Use database "iris" in sklearn then analyze the data.

* * *

# Introduction
1. *database :* Gathering and preparing data then show all of them which includes

    * *data :* 4 features (sepal_length, sepal_width, petal_length, petal_width) in number of 150 irises
    * *target :* 3 varieties of iris (setosa, versicolor, virginica), here it uses number 0, 1, 2 to represent
    * *target_names :* 3 varieties of iris (setosa, versicolor, virginica)
    * *feature_names :* 4 features (sepal_length, sepal_width, petal_length, petal_width)

2. *scatter :*  Have a quick glance at data. Use different colors to represent three varieties of iris, and then make 6 scatter plots to show the dot and regression line with 2 in pairs.

3. *training :*  Choose K-Nearest-Neighbor as the algorithm then start training and predicting, after compare test data and predicted data, we will get the **preliminary** accuracy rate of our prediction.

4. *bestParameter :*   After parameter tuning by using GridSearchCV, we will find the best parameter and estimator which is suggested by algorithm. Then, we could use new parameter for **advanced** prediction.