from pathlib import Path

import joblib

from modules.ioc_extractor import extract_iocs
from modules.report_generator import generate_report
from modules.text_cleaning import clean_text
from modules.threat_scoring import calculate_score

# Build paths from this file's location so the script works
# no matter which folder it is run from
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "model"
REPORT_FILE = BASE_DIR / "analysis_report.txt"

# load saved files
model = joblib.load(MODEL_DIR / "phishing_model.pkl")
vectoriser = joblib.load(MODEL_DIR / "vectoriser.pkl")


def read_email():
    # Read a multi-line email. Finish by entering a line containing only END.
    print("Paste the email text, then type END on a new line and press Enter:\n")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)


def main():
    email = read_email()

    if not email.strip():
        print("No email text entered.")
        return

    # IOCs are extracted from the original text (cleaning removes links)
    iocs = extract_iocs(email)

    # Clean the text the same way it was cleaned for training
    email_vector = vectoriser.transform([clean_text(email)])

    # make prediction (1 = phishing, 0 = legitimate)
    prediction = int(model.predict(email_vector)[0])
    confidence = model.predict_proba(email_vector).max() * 100

    label = "Phishing" if prediction == 1 else "Legitimate"

    score = calculate_score(
        prediction,
        confidence,
        iocs["urls"],
        iocs["ips"],
        iocs["emails"]
    )

    report = generate_report(label, confidence, score, iocs)

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"\nPrediction: {label}")
    print(f"Confidence: {confidence:.2f}%")

    print("\nURLs Found:")
    print(iocs["urls"])

    print("\nEmail Addresses Found:")
    print(iocs["emails"])

    print("\nIP Addresses Found:")
    print(iocs["ips"])

    print(f"\nThreat Score: {score}/100")
    print(f"\nReport saved to: {REPORT_FILE}")


if __name__ == "__main__":
    main()
