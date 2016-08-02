#In the previous chapter, you did all the slicing and dicing yourself to find subsets that have a higher chance of surviving. 
#A decision tree automates this process for you and outputs a classification model or classifier.

#Conceptually, the decision tree algorithm starts with all the data at the root node and scans all the variables for the best 
#one to split on. Once a variable is chosen, you do the split and go down one level (or one node) and repeat. 
#The final nodes at the bottom of the decision tree are known as terminal nodes, and the majority vote of the observations 
#in that node determine how to predict for new observations that end up in that terminal node.

#First, let's import the necessary libraries:

# 1) Import the numpy library as np
# 2) From sklearn import the tree

# Import the Numpy library
import numpy as np
# Import 'tree' from scikit-learn library
from sklearn import tree