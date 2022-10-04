from cgi import test
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2


df = pd.read_csv('./data/n_movies.csv', thousands=',')

cols_to_drop = ["year", "certificate",
                "duration", "genre", "stars", "description"]
# first five rows of dataframe after removing columns
df = df.drop(columns=cols_to_drop, axis=1)
df = df.dropna()
df["votes"] = df["votes"].astype(int)
df["rating"] = df["rating"].astype(float)
df["title"] = df["title"].astype(str)
df.head()

df.info()
