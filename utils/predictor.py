import os
import pickle
import re
import contractions
import sys
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize




class LemmaTokenizer:
    def __init__(self):
        self.wordnetlemma = WordNetLemmatizer()

    def __call__(self, text):
        return [self.wordnetlemma.lemmatize(word) for word in word_tokenize(text)]


sys.modules['__main__'].LemmaTokenizer = LemmaTokenizer

# -----------------------
# Load Models (Safe Path)
# -----------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "model_5.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "tfidfvect.pkl")
label_path = os.path.join(BASE_DIR, "models", "label_encoder.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(vectorizer_path, "rb") as f:
    vectorizer = pickle.load(f)

with open(label_path, "rb") as f:
    le = pickle.load(f)

# -----------------------
# Preprocessing (optional)
# -----------------------
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = contractions.fix(text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = text.lower()

    words = text.split()
    words = [w for w in words if w not in stop_words]

    return " ".join(words)

# -----------------------
# Prediction
# -----------------------

def predict_emotion(text):
    if not text or not text.strip():
        return {"emotion": "No input", "keywords": []}

    # Transform text
    vect = vectorizer.transform([text])

    # Prediction
    pred = model.predict(vect)[0]
    emotion = le.inverse_transform([pred])[0]

    # Get important words
    feature_names = vectorizer.get_feature_names_out()
    nonzero_indices = vect.nonzero()[1]

    words = [feature_names[i] for i in nonzero_indices]

    return {
        "emotion": emotion,
        "keywords": words
    }