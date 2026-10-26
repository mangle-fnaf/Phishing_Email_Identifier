# AI Phishing Email Detector

An AI-powered phishing email detection and threat analysis tool built using Python and Machine Learning.

## Overview

This project uses Natural Language Processing (NLP) and Machine Learning to identify phishing emails and assist with basic threat analysis. Emails are processed using TF-IDF vectorization and classified using a Logistic Regression model. Additional cybersecurity-focused features include confidence scoring, indicator extraction, and threat scoring.

The goal of this project is to demonstrate how AI can support security analysts by automating phishing detection and providing actionable threat intelligence.

---

## Features

### Machine Learning Detection

- TF-IDF text vectorization
- Logistic Regression classification
- 98% model accuracy
- Real-time email classification

### Threat Analysis

- Confidence scoring
- URL extraction
- Email address extraction
- IP address extraction
- Threat scoring system

### Investigation Support

- Automated phishing analysis
- Identification of Indicators of Compromise (IOCs)
- Investigation report generation

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- Regular Expressions (Regex)
- Jupyter Notebook

---

## Project Structure

```text
Phishing_Email_Identifier
│
├── notebook/
│   └── EDA.ipynb
│
├── src/
│   ├── data/
│   │
│   ├── model/
│   │   ├── phishing_model.pkl
│   │   └── vectoriser.pkl
│   │
│   ├── modules/
│   │   ├── ioc_extractor.py
│   │   ├── threat_scoring.py
│   │   └── report_generator.py
│   │
│   ├── predict.py
│   └── train_model.py
│
├── README.md
└── .gitignore
```

---

## Machine Learning Pipeline

1. Load phishing email dataset
2. Preprocess and clean email content
3. Split data into training and testing datasets
4. Convert text into TF-IDF features
5. Train Logistic Regression model
6. Evaluate model performance
7. Save trained model and vectoriser
8. Perform phishing detection on user supplied emails

---

## Example Output

```text
Prediction: Phishing

Confidence: 98.47%

URLs Found:
['http://fake-bank.com']

Email Addresses Found:
['security@fake-bank.com']

IP Addresses Found:
['192.168.1.50']

Threat Score: 84/100
```

---

## Future Improvements

- Email header analysis
- SPF/DKIM/DMARC analysis
- URL reputation checking
- Threat intelligence integration
- Dashboard visualisation
- PDF investigation reports

---

## Key Achievements

- Built a phishing email classifier using Machine Learning
- Achieved 98% classification accuracy
- Implemented TF-IDF feature extraction
- Developed a prediction engine using saved machine learning models
- Implemented IOC extraction for URLs, email addresses and IP addresses
- Created a threat scoring system to prioritize suspicious emails
- Generated automated investigation reports for phishing analysis

## Author

**Maliyka**

Cybersecurity Student | Security Operations & Threat Detection Enthusiast