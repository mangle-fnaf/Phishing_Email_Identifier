import joblib
from modules.ioc_extractor import extract_iocs
from modules.threat_scoring import calculate_score
from modules.report_generator import generate_report

# load saved files
model = joblib.load("model/phishing_model.pkl")
vectoriser = joblib.load("model/vectoriser.pkl")

# get email from user
email = input("Paste email text:\n\n")

# convert email into TF-IDF features
email_vector = vectoriser.transform([email])
iocs = extract_iocs(email)

# make prediction
prediction = model.predict(email_vector)[0]

confidence = (
    model.predict_proba(email_vector).max()
    * 100
)

if prediction == 1:
    label = "Phishing"
else:
    label = "Legitimate"

score = calculate_score(
    confidence,
    iocs["urls"],
    iocs["ips"],
    iocs["emails"]
)

report = generate_report(
    label,
    confidence,
    score,
    iocs
)

with open(
    "analysis_report.txt",
    "w"
) as f:
    f.write(report)

print("\nReport saved.")

print(f"\nPrediction: {label}")
print(f"Confidence: {confidence:.2f}%")

print("\nURLs Found:")
print(iocs["urls"])

print("\nEmail Addresses Found:")
print(iocs["emails"])

print("\nIP Addresses Found:")
print(iocs["ips"])

print(f"\nThreat Score: {score}/100")
