def calculate_score(prediction, confidence, urls, ips, emails):
    # prediction: 1 = phishing, 0 = legitimate
    # confidence: how sure the model is about its prediction (0-100)

    # Probability that the email is phishing (0-100)
    if prediction == 1:
        phishing_probability = confidence
    else:
        phishing_probability = 100 - confidence

    # The model's verdict makes up most of the score
    score = phishing_probability * 0.7

    # Indicators add extra risk, but only when the email looks suspicious.
    # A legitimate newsletter full of links shouldn't score as a threat.
    if phishing_probability >= 50:
        score += min(len(urls) * 10, 20)
        score += min(len(ips) * 10, 10)
        score += min(len(emails) * 5, 10)

    return min(round(score), 100)
