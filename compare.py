#How many people in your training set survived the disaster with the Titanic? To see this, you can use the value_counts() 
#method in combination with standard bracket notation to select a single column of a DataFrame:

# absolute numbers
## train["Survived"].value_counts()

# percentages
## train["Survived"].value_counts(normalize = True)

#If you run these commands in the console, you'll see that 549 individuals died (62%) and 342 survived (38%). 
#A simple way to predict heuristically could be: "majority wins". This would mean that you will predict every 
#unseen observation to not survive.

#To dive in a little deeper we can perform similar counts and percentage calculations on subsets of the Survived column. 
#For example, maybe gender could play a role as well? You can explore this using the .value_counts() method for a two-way 
#comparison on the number of males and females that survived, with this syntax:

## train["Survived"][train["Sex"] == 'male'].value_counts()
## train["Survived"][train["Sex"] == 'female'].value_counts()
#To get proportions, you can again pass in the argument normalize = True to the .value_counts() method.

# Instructions and execution

# 1) Calculate and print the survival rates in absolute numbers using values_counts() method.
# 2) Calculate and print the survival rates as proportions by setting the normalize argument to True.
# 3) Repeat the same calculations but on subsets of survivals based on Sex.

# Passengers that survived vs passengers that passed away
print(train["Survived"].value_counts())

# As proportions
print(train["Survived"].value_counts(normalize = True))

# Males that survived vs males that passed away
print(train["Survived"][train["Sex"] == 'male'].value_counts())

# Females that survived vs Females that passed away
print(train["Survived"][train["Sex"] == 'female'].value_counts())

# Normalized male survival
print(train["Survived"][train["Sex"] == 'male'].value_counts(normalize = True))

# Normalized female survival
print(train["Survived"][train["Sex"] == 'female'].value_counts(normalize = True))
