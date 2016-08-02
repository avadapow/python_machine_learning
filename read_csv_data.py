# Import the Pandas library
import pandas as pd #You have to import pandas as pd

# Load the train and test datasets to create two DataFrames
train_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/train.csv"
train = pd.read_csv(train_url)

test_url = "http://s3.amazonaws.com/assets.datacamp.com/course/Kaggle/test.csv"
test = pd.read_csv(test_url)

#Print the `head` of the train and test dataframes
print(train.head())
print(test.head())



# Course details and execution

# 1) First, import the Pandas library as pd.

# 2) Load the test data similarly to how the train data is loaded.

# 3) Inspect the first couple rows of the loaded dataframes using the .head() method with the code provided. 

#When the Titanic sank, 1502 of the 2224 passengers and crew were killed. One of the main reasons for this high 
#level of casualties was the lack of lifeboats on this self-proclaimed "unsinkable" ship.

#Those that have seen the movie know that some individuals were more likely to survive the sinking (lucky Rose) 
#than others (poor Jack). In this course, you will learn how to apply machine learning techniques to predict a 
#passenger's chance of surviving using Python.

#Let's start with loading in the training and testing set into your Python environment. You will use the training 
#set to build your model, and the test set to validate it. The data is stored on the web as csv files; their URLs 
#are already available as character strings in the sample code. You can load this data with the read_csv() method 
#from the Pandas library.