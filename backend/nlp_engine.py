# NLP Engine for Healthcare Assistant AI

## Overview
This module is responsible for processing natural language input, extracting symptoms, analyzing queries, and detecting user intent.

## Dependencies
- NLTK
- spaCy
- Scikit-learn

## NLP Text Processing

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word.lower() for word in tokens]
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return tokens
```

## Symptom Extraction

```python
import re

def extract_symptoms(text):
    symptoms_pattern = re.compile(r'(?i)(fever|cough|nausea|headache|fatigue)')
    return symptoms_pattern.findall(text)
```

## Query Analysis

```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def analyze_query(user_query, knowledge_base):
    vectorizer = CountVectorizer().fit_transform([user_query] + knowledge_base)
    vectors = vectorizer.toarray()
    cosine_matrix = cosine_similarity(vectors)
    return cosine_matrix[0][1:]
```

## Intent Detection

```python
def detect_intent(user_input):
    intents = {
        'symptom_check': ['fever', 'cough', 'nausea'],
        'general_query': ['help', 'information', 'advice']
    }
    for intent, keywords in intents.items():
        if any(keyword in user_input.lower() for keyword in keywords):
            return intent
    return 'unknown'
```

# Usage Example
if __name__ == '__main__':
    user_input = "I have a cough and fever."
    preprocessed = preprocess_text(user_input)
    symptoms = extract_symptoms(user_input)
    intent = detect_intent(user_input)
    print(f'Symptoms: {symptoms}, Intent: {intent}')