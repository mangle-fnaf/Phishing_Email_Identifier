import joblib
from modules.ioc_extractor import extract_iocs
from modules.threat_scoring import calculate_score

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

print(f"\nPrediction: {label}")
print(f"Confidence: {confidence:.2f}%")

print("\nURLs Found:")
print(iocs["urls"])

print("\nEmail Addresses Found:")
print(iocs["emails"])

print("\nIP Addresses Found:")
print(iocs["ips"])

print(f"\nThreat Score: {score}/100")