#Before you can begin constructing your trees you need to get your hands dirty and clean the data so that you can use all 
#the features available to you. In the first chapter, we saw that the Age variable had some missing value. Missingness is 
#a whole subject with and in itself, but we will use a simple imputation technique where we substitute each missing value 
#with the median of the all present values.

## train["Age"] = train["Age"].fillna(train["Age"].median())

#Another problem is that the Sex and Embarked variables are categorical but in a non-numeric format. Thus, we will need 
#to assign each class a unique integer so that Python can handle the information. Embarked also has some missing values 
#which you should impute witht the most common class of embarkation, which is "S".

# Instructions and execution

# 1) Assign the integer 1 to all females
# 2) Impute missing values in Embarked with class S. Use .fillna() method.
# 3) Replace each class of Embarked with a uniques integer. 0 for S, 1 for C, and 2 for Q.
# 4) Print the Sex and Embarked columns

# Convert the male and female groups to integer form
train["Sex"][train["Sex"] == "male"] = 0
train["Sex"][train["Sex"] == "female"] = 1

# Impute the Embarked variable
train["Embarked"] = train["Embarked"].fillna("S")

# Convert the Embarked classes to integer form
train["Embarked"][train["Embarked"] == "S"] = 0
train["Embarked"][train["Embarked"] == "C"] = 1
train["Embarked"][train["Embarked"] == "Q"] = 2

# Print the Sex and Embarked columns
print(train["Sex"])
print(train["Embarked"])