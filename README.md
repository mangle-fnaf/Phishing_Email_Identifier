# AI Phishing Email Detector

An AI-powered phishing email detection and threat analysis tool built using Python and Machine Learning.

## Overview

This project uses Natural Language Processing (NLP) and Machine Learning to identify phishing emails and assist with basic threat analysis. Emails are processed using TF-IDF vectorisation and classified using a Logistic Regression model. Additional cybersecurity-focused features include confidence scoring, indicator extraction, threat scoring and report generation.

The goal of this project is to demonstrate how AI can support security analysts by automating phishing detection and providing actionable threat intelligence.

---

## Features

### Machine Learning Detection

- TF-IDF text vectorisation
- Logistic Regression classification
- 98% accuracy on a held-out test set of 16,498 emails
- Real-time email classification

### Threat Analysis

- Confidence scoring
- URL extraction
- Email address extraction
- IP address extraction (validated, 0–255)
- Threat scoring system

### Investigation Support

- Automated phishing analysis
- Identification of Indicators of Compromise (IOCs)
- Investigation report generation (`src/analysis_report.txt`)

---

## Technologies Used

- Python
- Pandas
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
│   └── EDA.ipynb                 # Data exploration and model training walkthrough
│
├── src/
│   ├── data/raw/                 # Dataset goes here (not uploaded - see below)
│   │
│   ├── model/
│   │   ├── phishing_model.pkl    # Trained model
│   │   └── vectoriser.pkl        # Trained TF-IDF vectoriser
│   │
│   ├── modules/
│   │   ├── ioc_extractor.py      # Extracts URLs, emails and IPs
│   │   ├── text_cleaning.py      # Shared text cleaning for training and prediction
│   │   ├── threat_scoring.py     # Calculates the threat score
│   │   └── report_generator.py   # Builds the analysis report
│   │
│   ├── predict.py                # Analyse an email
│   └── train_model.py            # Retrain the model
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How to Run

1. Clone the repository and install the requirements
   ```
   git clone https://github.com/mangle-fnaf/Phishing_Email_Identifier.git
   cd Phishing_Email_Identifier
   pip install -r requirements.txt
   ```
2. Analyse an email (the trained model is included, so no dataset is needed)
   ```
   python src/predict.py
   ```
3. Paste the email text, then type `END` on a new line and press Enter

---

## Dataset

The model was trained on the [Phishing Email Dataset](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset) from Kaggle (`phishing_email.csv`, 82,486 emails: 42,891 phishing and 39,595 legitimate). Label `1` = phishing, `0` = legitimate.

The dataset is not included in this repository because of its size. To retrain the model:

1. Download `phishing_email.csv` from the link above
2. Place it in `src/data/raw/`
3. Run
   ```
   python src/train_model.py
   ```

---

## Machine Learning Pipeline

1. Load phishing email dataset
2. Clean email content (lowercase, remove links, numbers and punctuation)
3. Split data into training (80%) and testing (20%) datasets
4. Convert text into TF-IDF features (5,000 features, English stop words removed)
5. Train Logistic Regression model
6. Evaluate model performance
7. Save trained model and vectoriser
8. Clean user-supplied emails in exactly the same way and classify them

---

## Threat Scoring

The threat score (0–100) combines the model's verdict with the indicators found:

- 70% of the score comes from the probability that the email is phishing
- Up to 40 extra points are added for URLs, IP addresses and email addresses, but only when the email already looks suspicious

This means a legitimate email with links (such as a newsletter) is not treated as a threat.

---

## Example Output

```text
Prediction: Phishing
Confidence: 98.68%

URLs Found:
['http://secure-paypa1-login.com/verify']

Email Addresses Found:
['support@paypa1-security.com']

IP Addresses Found:
[]

Threat Score: 84/100
```

---

## Screenshots

### Phishing email detected

![Phishing email detected](screenshots/phishing-detected.png)

### Legitimate email

![Legitimate email](screenshots/legitimate-email.png)

---

## Limitations

- The model only analyses the text of an email, not its headers, sender reputation or attachments.
- The training emails are mostly older public datasets, so modern phishing styles may be less well recognised.
- Accuracy is measured on data from the same dataset; real-world performance is likely to be lower.

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
- Achieved 98% classification accuracy on unseen test data
- Implemented TF-IDF feature extraction
- Developed a prediction engine using saved machine learning models
- Implemented IOC extraction for URLs, email addresses and IP addresses
- Created a threat scoring system to prioritise suspicious emails
- Generated automated investigation reports for phishing analysis

## Credits & Licence

- Dataset: [Phishing Email Dataset](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset) by Naser Abdullah Alam et al., licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- Paper: Al-Subaiey, A. et al. (2024). *Novel Interpretable and Robust Web-based AI Platform for Phishing Email Detection*. [arXiv:2405.11619](https://arxiv.org/abs/2405.11619).
- The email text was cleaned (lowercased, links, numbers and punctuation removed) before training.
- The trained model files in `src/model/` are derived from this dataset and are shared under the same CC BY-SA 4.0 licence.

## Author

**Maliyka**

Cybersecurity Student | Security Operations & Threat Detection Enthusiast