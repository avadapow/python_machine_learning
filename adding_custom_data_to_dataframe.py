#Another variable that could influence survival is age; since it's probable that children were saved first. 
#You can test this by creating a new column with a categorical variable Child. Child will take the value 1 in cases 
#where age is less than 18, and a value of 0 in cases where age is greater than or equal to 18.

#To add this new variable you need to do two things 
# (i) create a new column, and 
# (ii) provide the values for each observation (i.e., row) based on the age of the passenger.

#Adding a new column with Pandas in Python is easy and can be done via the following syntax:

## your_data["new_var"] = 0
#This code would create a new column in the train DataFrame titled new_var with 0 for each observation.

#To set the values based on the age of the passenger, you make use of a boolean test inside the square bracket operator. 
#With the []-operator you create a subset of rows and assign a value to a certain variable of that subset of observations. 
#For example,

## train["new_var"][train["Fare"] > 10] = 1
#would give a value of 1 to the variable new_var for the subset of passengers whose fares greater than 10. 
#Remember that new_var has a value of 0 for all other values (including missing values).

#A new column called Child in the train data frame has been created for you that takes the value NaN for all observations.

# Instructions and execution

# 1) Set the values of Child to 1 is the passenger's age is less than 18 years.
# 2) Then assign the value 0 to observations where the passenger is greater than or equal to 18 years in the new Child column.
# 3) Compare the normalized survival rates for those who are <18 and those who are older. Use code similar to what you had in 
#the previous exercise.