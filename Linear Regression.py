#Supervised Learning
'''
Linear regression is a fundamental statistical method widely used in data science to explore relationships between variables. 
In this, we will study through a hands-on project applying linear regression to a real-world dataset. 
Our aim is to simplify the process and demonstrate how this technique can extract valuable insights from data in practical scenarios.
'''
'''
NumPy: Essential for numerical operations.
Pandas: Perfect for data manipulation and analysis.
Statsmodels: Provides classes and functions for the estimation of statistical models.
Matplotlib and Seaborn: Our go-to libraries for data visualization.
Scikit-learn: A comprehensive library for machine learning, including linear regression models.
'''

import numpy as np
import pandas as pd
import statsmodels.api as sm #Statsmodels: Provides classes and functions for the estimation of statistical models.
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns 
sns.set()
''' #APPROACH 1
raw_data = pd.read_csv('1.04. Real-life example.csv')

# Let's explore the top 5 rows of the df
raw_data.head()
# Let's see the description of each columns in dataset
raw_data.describe(include='all')
'''
'''#APPROACH 2 KAGGLE'''

#raw_data = pd.read_csv("/kaggle/input/104reallife-examplecsv")
# Replace with the actual file path printed from the previous code
file_path = '/kaggle/input/104reallife-examplecsv/1.04. Real-life example.csv'

# Read the CSV file into a DataFrame
raw_data = pd.read_csv(file_path)


# Let's explore the top 5 rows of the df
raw_data.head()
# Let's see the description of each columns in dataset
raw_data.describe(include='all')
