

## Sentiment Analysis of Movie Reviews – Into the Wild

---

## (1) Problem Statement

The problem is to analyze textual data from online reviews and classify them into positive, negative, or neutral sentiments. Due to unstructured text, identifying sentiment accurately is challenging and requires machine learning techniques.

---

## (2) Objective

The objective of this project is to:

- Collect 100 reviews related to the movie  
- Manually label them as positive, negative, or neutral  
- Apply machine learning models to classify sentiments  
- Evaluate model performance using precision and recall  

---

## (3) Dataset

**Source:**  
Reddit  

**Features:**  
- Review (text data)  
- Sentiment (Positive / Negative / Neutral)  

**Size:**  
- Total: 100 reviews  
- Training: 80  
- Testing: 20  

---

## (4) Methodology

### Data Preprocessing
- Convert text to lowercase  
- Remove special characters and URLs  
- Remove stopwords  
- Clean and normalize text  

### EDA (Exploratory Data Analysis)
- Distribution of sentiment classes  
- Frequency of words  
- Basic text analysis  

### Model Building
- Naïve Bayes  
- Logistic Regression  
- Support Vector Machine (SVM)  

### Evaluation
- Precision  
- Recall  
- F1-score  

---

## (5) Results

- Naïve Bayes → Moderate performance  
- Logistic Regression → Better accuracy  
- SVM → Best performance  

👉 Insight:  
SVM performed best due to its ability to handle high-dimensional text data effectively.

---

## (6) How to Run

```bash
pip install pandas scikit-learn openpyxl
