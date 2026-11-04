import re


def _unique(items):
    # Remove duplicates but keep the original order
    return list(dict.fromkeys(items))


def extract_iocs(text):
    urls = re.findall(r'https?://[^\s<>"\']+', text)

    # Remove punctuation that often ends up stuck to the end of a link
    urls = [url.rstrip(".,;:!?)]}") for url in urls]

    emails = re.findall(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        text
    )

    ips = re.findall(
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        text
    )

    # Only keep real IPs (each number must be 0-255)
    ips = [ip for ip in ips if all(0 <= int(part) <= 255 for part in ip.split("."))]

    return {
        "urls": _unique(urls),
        "emails": _unique(emails),
        "ips": _unique(ips)
    }
