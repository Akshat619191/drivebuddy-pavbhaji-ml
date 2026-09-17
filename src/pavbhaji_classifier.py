import re
import joblib

import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "pavbhaji_text_classifier.pkl")

model = joblib.load(MODEL_PATH)


def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"@\w+", " ", text)
    text = re.sub(r"#", " ", text)
    text = re.sub(r"\\n", " ", text)
    text = re.sub(r"\n", " ", text)
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def remove_pavbhaji(text):
    text = re.sub(r"\bpav\s*bhaji\b", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"\bpavbhaji\b", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def predict_pavbhaji(text):
    cleaned = clean_text(text)
    cleaned = remove_pavbhaji(cleaned)
    prediction = model.predict([cleaned])[0]

    return "Pav Bhaji" if prediction == 1 else "Not Pav Bhaji"


if __name__ == "__main__":
    text = input("Enter Instagram post text: ")
    print("Prediction:", predict_pavbhaji(text))