#You will use the scikit-learn and numpy libraries to build your first decision tree. scikit-learn can be 
#used to create tree objects from the DecisionTreeClassifier class. The methods that we will use take numpy 
#arrays as inputs and therefore we will need to create those from the DataFrame that we already have. 
#We will need the following to build a decision tree

# @@ target: A one-dimensional numpy array containing the target/response from the train data. (Survival in your case)
# @@ features: A multidimensional numpy array containing the features/predictors from the train data. (ex. Sex, Age)

#Take a look at the sample code below to see what this would look like:

## target = train["Survived"].values

## features = train[["Sex", "Age"]].values

## my_tree = tree.DecisionTreeClassifier()

## my_tree = my_tree.fit(features, target)

#One way to quickly see the result of your decision tree is to see the importance of the features that are included. 
#This is done by requesting the .feature_importances_ attribute of your tree object. Another quick metric is the mean 
#accuracy that you can compute using the .score() function with features_one and target as arguments.

#Ok, time for you to build your first decision tree in Python! The train and testing data from chapter 1 are available 
#in your workspace.


# Print the train data to see the available features
print(train)

# Create the target and features numpy arrays: target, features_one
target = train["Survived"].values
features_one = train[["Pclass", "Sex", "Age", "Fare"]].values

# Fit your first decision tree: my_tree_one
my_tree_one = tree.DecisionTreeClassifier()
my_tree_one = my_tree_one.fit(features_one, target)

# Look at the importance and score of the included features
print(my_tree_one.feature_importances_)
print(my_tree_one.score(features_one, target))
