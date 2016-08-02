#To send a submission to Kaggle you need to predict the survival rates for the observations in the test set. 
#In the last exercise of the previous chapter, we created simple predictions based on a single subset. 
#Luckily, with our decision tree, we can make use of some simple functions to "generate" our answer without 
#having to manually perform subsetting.

#First, you make use of the .predict() method. You provide it the model (my_tree_one), the values of features 
#from the dataset for which predictions need to be made (test). To extract the features we will need to 
#create a numpy array in the same way as we did when training the model. However, we need to take care of 
#a small but important problem first. There is a missing value in the Fare feature that needs to be imputed.

#Next, you need to make sure your output is in line with the submission requirements of Kaggle: a csv file with 
#exactly 418 entries and two columns: PassengerId and Survived. Then use the code provided to make a new data 
#frame using DataFrame(), and create a csv file using to_csv() method from Pandas.

# Instructions and execution

# 1) Impute the missing value for Fare in row 153 with the median of the column.
# 2) Make a prediction on the test set using the .predict() method and my_tree_one. Assign the result to my_prediction.
# 3) Create a data frame my_solution containing the solution and the passenger ids from the test set. Make sure the 
#    solution is in line with the standards set forth by Kaggle by naming the column appropriately.

# Impute the missing value with the median
test.Fare[152] = test.Fare.median()

# Extract the features from the test set: Pclass, Sex, Age, and Fare.
test_features = test[["Pclass", "Sex", "Age", "Fare"]].values

# Make your prediction using the test set and print them.
my_prediction = my_tree_one.predict(test_features)
print(my_prediction)

# Create a data frame with two columns: PassengerId & Survived. Survived contains your predictions
PassengerId =np.array(test["PassengerId"]).astype(int)
my_solution = pd.DataFrame(my_prediction, PassengerId, columns = ["Survived"])
print(my_solution)

# Check that your data frame has 418 entries
print(my_solution.shape)

# Write your solution to a csv file with the name my_solution.csv
my_solution.to_csv("my_solution_one.csv", index_label = ["PassengerId"])