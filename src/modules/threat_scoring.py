def calculate_score(confidence, urls, ips, emails):

    score = confidence * 0.5

    score += len(urls) * 15
    score += len(ips) * 10
    score += len(emails) * 5

    return min(round(score), 100)