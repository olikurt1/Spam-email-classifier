import pandas as pd
#storing the kaggle dataset as a panda dataframe
df = pd.read_csv("./resources/spam_ham_dataset.csv")

#checking for duplicates
print(df.duplicated(subset="text").sum())
print(df)

#Removing duplicates based on text column and checking that duplicates. 
df = df.drop_duplicates(subset="text")
print(df.duplicated(subset="text").sum())

#removes the email ID provided by the dataset and the label column (spam/ham)
df = df.drop(columns=["Unnamed: 0","label"])

#confirming there aren't any empty cells in the text column and that there aren't any cells without text 
print(df["text"].isna().sum()) #0
print((df["text"].str.strip() == "").sum()) #0

print(df)

def train_test_split(text):
    pass