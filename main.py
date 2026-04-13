# Sentiment Analysis - Into the Wild

import pandas as pd
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

from sklearn.metrics import classification_report

# Load dataset
df = pd.read_excel("into_the_wild_reddit_dataset.xlsx")

# Preprocessing function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text

df["Cleaned"] = df["Review"].apply(clean_text)

# Split data
X = df["Cleaned"]
y = df["Sentiment"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text to numeric
vectorizer = TfidfVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Models
nb = MultinomialNB()
lr = LogisticRegression(max_iter=200)
svm = SVC()

# Train models
nb.fit(X_train_vec, y_train)
lr.fit(X_train_vec, y_train)
svm.fit(X_train_vec, y_train)

# Predictions
nb_pred = nb.predict(X_test_vec)
lr_pred = lr.predict(X_test_vec)
svm_pred = svm.predict(X_test_vec)

# Results
print("Naive Bayes:\n", classification_report(y_test, nb_pred))
print("Logistic Regression:\n", classification_report(y_test, lr_pred))
print("SVM:\n", classification_report(y_test, svm_pred))
