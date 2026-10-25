import re

def extract_iocs(text):
    urls = re.findall(r'https?://[^\s]+', text)

    emails = re.findall(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )

    ips = re.findall(
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        text
    )

    return {
        "urls": urls,
        "emails": emails,
        "ips": ips
    }