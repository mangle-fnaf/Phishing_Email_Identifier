# Trains the phishing detection model and saves it to src/model/.
# This is the same process as notebook/EDA.ipynb, as a script that can be
# re-run without opening Jupyter.
#
# Usage (from the project folder):
#     python src/train_model.py

from pathlib import Path

import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from modules.text_cleaning import clean_text

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "raw" / "phishing_email.csv"
MODEL_DIR = BASE_DIR / "model"


def main():
    if not DATA_FILE.exists():
        print(f"Dataset not found: {DATA_FILE}")
        print("Download phishing_email.csv (see README) and place it in src/data/raw/")
        return

    # Load the dataset (label 1 = phishing, 0 = legitimate)
    df = pd.read_csv(DATA_FILE, encoding="latin1")
    df = df.dropna(subset=["text_combined", "label"])
    print(f"Loaded {len(df):,} emails")

    # Clean the text the same way predict.py does
    df["clean_text"] = df["text_combined"].apply(clean_text)

    # Convert text into TF-IDF features
    vectoriser = TfidfVectorizer(stop_words="english", max_features=5000)
    X = vectoriser.fit_transform(df["clean_text"])
    y = df["label"]

    # 80% training, 20% testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Evaluate on the unseen test data
    preds = model.predict(X_test)
    print(classification_report(y_test, preds, target_names=["Legitimate", "Phishing"]))

    # Save the model and vectoriser for predict.py
    MODEL_DIR.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_DIR / "phishing_model.pkl")
    joblib.dump(vectoriser, MODEL_DIR / "vectoriser.pkl")
    print(f"Model saved to {MODEL_DIR}")


if __name__ == "__main__":
    main()
