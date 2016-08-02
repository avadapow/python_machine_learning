#In one of the previous exercises you discovered that in your training set, females had over a 50% 
#chance of surviving and males had less than a 50% chance of surviving. Hence, you could use this 
#information for your first prediction: all females in the test set survive and all males in the test set die.

#You use your test set for validating your predictions. You might have seen that contrary to the training set, 
#the test set has no Survived column. You add such a column using your predicted values. Next, when uploading your results, 
#Kaggle will use this variable (= your predictions) to score your performance.

# 1) Create a variable test_one, identical to dataset test
# 2) Add an additional column, Survived, that you initialize to zero.
# 3) Use vector subsetting like in the previous exercise to set the value of Survived to 1 for observations whose Sex equals "female".
# 4) Print the Survived column of predictions from the test_one dataset.

# Create a copy of test: test_one
test_one = test

# Initialize a Survived column to 0
test_one["Survived"] = 0

# Set Survived to 1 if Sex equals "female" and print the `Survived` column from `test_one`
test_one["Survived"][test_one["Sex"] == "female"] = 1

print(test_one["Survived"])