import pandas as pd
import pickle

url = "https://ucsd-enron-final-project.s3-us-west-1.amazonaws.com/final_project_dataset.pkl"

df = pd.read_pickle(url)
# df = pd.read_csv(url)

df.head()