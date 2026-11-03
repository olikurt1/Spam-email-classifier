# Spam-email-classifier

This repository includes a spam email classifier using TF-IDF to turn emails into numerical features that a model can read and a Multinomial Naive Bayes model as the classification model. It is trained on the Enron-Spam dataset (4993 emails after removing duplicates) from Kaggle and built with scikit-learn. The Naive bayes model was given a testing set of 999 emails and reached an accuracy score of 88.3% against a baseline score of 70.7%. There is a 100% precision score meaning no real emails were flagged as spam and a 60% recall score meaning most spam was caught but not all. This shows that the model is cautious as it never blocks real mail (precision score) but lets some spam through (recall score).

## Results 

| Metric      | Score |
|-------------|-------|
| Accuracy    | 88.3% |
| Baseline    | 70.7% |
| Precision   | 100%  |
| Recall      | 60.4% |

### Confusion Matrix 999 test emails:

|             Predicted ham | Predicted spam |
|---------------------------|----------------|
| Actual ham  |         706 |              0 |
| Actual spam |         116 |            177 |

The results and confusion matrix shows that every email the model flagged as spam was really spam, so legitimate emails weren't lost. However, 116 of the 293 spam emails were let through. For a spam filter this is better than blocking a real email but recall needs to be improved. An accuracy of 88.3% is misleading in this case because 70.7% of the emails are already ham. This is why I included precision, recall and the confusion matrix alongside it. 

## Data

Dataset: [Kaggle Spam Mail Dataset](https://www.kaggle.com/datasets/venky73/spam-mails-dataset), a subset of the Enron-Spam set, with columns for email text and spam/ham labelling. 

Cleaning: In Data.py, I cleaned the dataset by removing 178 duplicate emails to avoid score inflation. I also checked for missing or blank email text cells. None were found. Finally I dropped the dataset's ID column and the text label column and only kept the text and label_num columns. label_num is used as the target. After cleaning, the balance between spam and ham was 29.3% and 70.7%

## Approach

1. Train/test split: 80/20 split using train_test_split from scikit-learn. The split was stratified on label_num so both sets could keep the ratio of 70.7/29.3. The split includes a fixed random state which means that results won't vary. 
2. TF-IDF vectorisation: This converts each email into numbers based on how often each word appears. This gives less weight to words that are common to almost all emails such as "the" and "subject". 
3. Multinomial Naive Bayes: This model learns how likely each word is to appear in spam vs ham. These probabilites are then combined to classify new emails. I chose this because it is fast and suits word frequency data well. 
4. Pipeline: Since the TF-IDF and model are combined using scikit-learn Pipeline, the model only ever learns from training data. This prevents testing data being used in training. 

## Project Structure

```
Spam-email-classifier/
├── src/
│   ├── Data.py         # loads and cleans the dataset
│   └── Train.py        # splits data, trains the pipeline, evaluates it
├── resources/          # dataset goes here (not included in repo)
├── requirements.txt
└── README.md
```

## How to run

Requires Python 3.12 or newer.

1. Clone repository:
```
git clone https://github.com/olikurt1/Spam-email-classifier.git
cd Spam-email-classifier
```
2. Create and activate a virtual environment, then install dependencies:
```
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
3. Download the dataset from Kaggle and save it within a 'resources' folder which should be sibling to 'src'. The project expects the file to be named spam_ham_dataset.csv
4. From the project root run: python src/Train.py

## Limitations and next steps

- Low recall (60%): this is the main weakness and I plan to try Logistic Regression against the Naive Bayes baseline. 
- Evaluate the model on my own inbox to measure false positive on modern emails. Performance on this will most likely be lower since the Enron emails are from the early 2000s.