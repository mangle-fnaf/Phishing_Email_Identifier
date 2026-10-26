from datetime import datetime

def generate_report(
    prediction,
    confidence,
    score,
    iocs
):

    report = f"""
PHISHING ANALYSIS REPORT
========================

Generated:
{datetime.now()}

Prediction:
{prediction}

Confidence:
{confidence:.2f}%

Threat Score:
{score}/100

Indicators of Compromise
------------------------

URLs:
{iocs['urls']}

Email Addresses:
{iocs['emails']}

IP Addresses:
{iocs['ips']}

Assessment
-----------

This email has been classified as:
{prediction}

Overall Threat Score:
{score}/100
"""

    return report