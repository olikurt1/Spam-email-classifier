# Spam-email-classifier
The purpose of this repository will be to showcase

## Data
I will be using a public dataset to train the model. I will then use my own emails as testing data. The main decision for this is my personal dataset would not be large enough to train model. I will be using the enron-spam kaggle dataset to train the model initially. The dataset is split between 71% ham and 29% spam. When splitting the data between training and testing data I will stratify this so that the percentage of ham to spam is the same in both testing and training data. From the dataset, I have dropped the label and email ID label columns. The label column is dropped because there is already a label_num column which sets the row as 1 or 0 depending on if its spam or ham. Ham is 0, spam is 1. This is enough for the dataset as the model can use this value as the target to determine spam or ham. Removing the ID simply cleans up the dataset as it isn't required for context by the model. 

## Libraries
This project will include usage of the Pandas library. This will set the CSV into a dataframe and allow cleaning and manipulation of data. Scikit-Learn is also being utilised for splitting the data into training and testing splits along with importing the algorithm (Naive Bayes)


## Training
The data is being split into an 80/20 split of training and testing. Stratification ensures that both splits have 71% ham and 29% spam. To be exact the split is 70.7% and 29.3%. The model has to easily beat 70.7% otherwise it will have only detected ham when there is a definitive amount of spam. 