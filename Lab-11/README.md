# 🟡 ML Lab 11 – Natural Language Processing (NLP)

This directory contains the implementation of fundamental Natural Language Processing techniques using `NLTK` and `Scikit-Learn`.

## 📝 Objective
Apply and evaluate core text preprocessing methods (lowercasing, tokenization, stopwords/punctuation removal, stemming, lemmatization) and generate text representations using Bag of Words and TF-IDF.

## 📂 Structure
- `notebook.ipynb` - Chronological steps transforming raw text into vectorized matrices.
- `ML LAB -11.docx` - Formal lab report with code snippets, array outputs, and visual plots.
- `outputs/` - Visual results:
    - `tfidf_scores.png`: Bar chart displaying TF-IDF scores for the sample text.

## 📊 Key Output Metrics
- Identifies features from cleaned text (e.g., 'machine', 'language', 'understand').
- **Bag of Words Matrix**: Word frequencies across documents.
- **TF-IDF Matrix**: Word weights reflecting their term-uniqueness inverted across documents.

## 🏆 Key Observations
- Punctuation and stopword removal significantly reduce the vocabulary size (background noise).
- Lemmatization yields better context-aware root words compared to simplistic algorithmic Stemming.
- TF-IDF effectively down-weighs common terms (like 'natural', 'processing') across multiple combined sets to surface the most contextually relevant topics.
