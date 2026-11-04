import re


def clean_text(text):
    # Clean email text exactly the same way it was cleaned for training.
    # The model only understands text in this format, so predict.py and
    # train_model.py must both use this function.
    text = str(text).lower()

    # Remove links - they are extracted separately as IOCs
    text = re.sub(r"http\S+", "", text)

    # Keep only letters and spaces
    text = re.sub(r"[^a-z\s]", "", text)

    # Collapse extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text
