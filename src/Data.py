import pandas as pd
#storing the kaggle dataset as a panda dataframe
DATA_SET_PATH = "./resources/spam_ham_dataset.csv"


def load_data(data_set):
    return pd.read_csv(data_set)

def clean_data(df):
    #checking for duplicates
    print(f"Number of duplicates before dropping: {df.duplicated(subset="text").sum()}")

    #Removing duplicates based on text column and checking that duplicates. 
    df = df.drop_duplicates(subset="text", ignore_index=True)
    print(f"Number of duplicates after dropping: {df.duplicated(subset="text").sum()}")

    #removes the email ID provided by the dataset and the label column (spam/ham)
    df = df.drop(columns=["Unnamed: 0","label"])

    #confirming there aren't any empty cells in the text column and that there aren't any cells without text 
    print(f"Number of empty cells: {df["text"].isna().sum()}") #0
    print(f"Number of text cells that are blank or only whitespace: {(df["text"].str.strip() == "").sum()}") #0

    print(df)
    
    return df


# Ensures code doesn't run automatically when imported by another file but will run if current file runs directly
if __name__ == "__main__":
    df = load_data(DATA_SET_PATH)
    cleaned_df = clean_data(df)
