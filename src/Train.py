from Data import clean_data, load_data, DATA_SET_PATH
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

def split_data(df):
    #unpacking text column and label number column
    X = df["text"]
    y = df["label_num"]
    
    #splitting data into 20% testing and 80% training with a randomising seed of 42 and strafifying based on target value
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    return X_train, X_test, y_train, y_test


if __name__ == ("__main__"):
    df = load_data(DATA_SET_PATH)
    cleaned_df = clean_data(df)
    X_train, X_test, y_train, y_test = split_data(cleaned_df)
    #ensuring 80/20 split worked
    print(f"Text column training length: {len(X_train)}.")
    print(f"Text column testing length: {len(X_test)}.")
    print(f"label column training length: {len(y_train)}.")
    print(f"label column testing length: {len(y_test)}.")

    #ensuring stratification worked
    print(f"{y_train.mean():.1%}")
    print(f"{y_test.mean():.1%}")