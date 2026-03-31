# EmoSense – Emotion Sentiment Analysis System



## 1. About the Dataset

### 1.1 Overview

This project utilizes a synthetic dataset consisting of 13,970 text samples, each labeled with one of seven emotion categories: Anger, Happiness, Sadness, Surprise, Hate, Love, and Fun.

The dataset was generated using the Mistral-7B language model, ensuring diverse and context-rich emotional expressions. The text samples vary in length and complexity, ranging from short statements to descriptive sentences.

---

### 1.2 Sample Data

**Text:**

"John clenched his fists, his face turning red as he paced back and forth in the room. His eyes flashed with frustration as he muttered under his breath about the latest setback at work."

**Label (Emotion):**  
Anger

---

### 1.3 Key Statistics

- Total Records: 13,970  
- Features:
  - text: Input textual data  
  - emotion: Target label  
- Number of Classes: 7 (balanced distribution)  
- Data Type: Synthetic (generated using Mistral-7B)  
- Privacy: No personally identifiable information (PII)  
- Format: CSV  

---

## 2. Objective

The objective of this project is to design and implement an NLP-based system that can identify and classify emotions from textual input.

The system aims to:

- Analyze user-provided text  
- Classify emotions into predefined categories  
- Demonstrate an end-to-end machine learning pipeline  
- Provide a deployable real-time prediction system  

---

## 3. Mapping to Data Science Problem

### 3.1 Problem Definition

This is a multi-class text classification problem where input text is mapped to one of seven emotion labels.

---

### 3.2 Input and Output

- Input: Raw user text  
- Output: Predicted emotion  

---

### 3.3 Approach

1. Text preprocessing (tokenization, lemmatization, stopword removal)  
2. Feature extraction using TF-IDF (unigrams and bigrams)  
3. Model training using machine learning algorithms  
4. Evaluation using performance metrics  
5. Deployment using Flask  

---

## 4. Expected Outcome

- Accurate emotion classification  
- Real-time prediction via web interface  
- Ability to handle varied sentence structures  
- A reusable and extendable NLP pipeline  

---

## 5. Challenges Observed

### 5.1 Emotion Overlap

Certain emotions are difficult to distinguish:

- Fear vs Sadness  
- Joy vs Happiness  

---

### 5.2 Mixed Emotions

Some sentences contain multiple emotions:

"I feel like working, but I am not interested."

---

### 5.3 Short Text Limitation

The model performs poorly on very short inputs:

- "Okay"  
- "Fine"  

---

### 5.4 Ambiguous Context

Some sentences lack clear emotional meaning:

"I am off these days."

---

### 5.5 Sarcasm and Irony

Sarcastic expressions are difficult to interpret:

"Great, another assignment."

---

### 5.6 Vocabulary Dependency

TF-IDF relies on known words.  
Unseen words reduce prediction accuracy.

---

## 6. Applications

This system can be applied in multiple real-world scenarios:

- **Customer Feedback Analysis**  
  Automatically detect emotions in user reviews, complaints, and feedback to improve services.

- **Mental Health Monitoring**  
  Analyze user text (journals, chats) to detect emotional states and identify early signs of distress.

- **Social Media Analysis**  
  Track public sentiment and emotional trends on platforms like Twitter, Instagram, etc.

- **Chatbots and Virtual Assistants**  
  Enable emotion-aware responses to improve user interaction and personalization.

- **Content Recommendation Systems**  
  Suggest content (music, videos, articles) based on user emotions.

- **Human Resource Analytics**  
  Analyze employee feedback to understand workplace satisfaction and issues.

- **E-learning Platforms**  
  Detect student emotions to improve engagement and adaptive learning systems.

---

## 7. Conclusion

This project demonstrates the use of NLP and machine learning for emotion classification. It highlights both the strengths and limitations of traditional approaches like TF-IDF.

The system works well for structured inputs but faces challenges with ambiguity, short text, and overlapping emotions.

---

## 8. Future Improvements

- Use deep learning models (LSTM, BERT)  
- Handle multi-label classification  
- Improve short text understanding  
- Add prediction confidence scores  
- Enhance UI and deploy on cloud  

---

## 9. Deployment

The model is deployed using a Flask-based web application, enabling real-time emotion prediction from user input.

---

## 10. How to Run the Project

1. Install required libraries:
   pip install -r requirements.txt

2. Download NLTK resources:
   pip install nltk
Then run:
 import nltk
nltk.download('punkt')
nltk.download('wordnet')
exit()

3. Start the Flask application:
  python app.py
4. Open your browser and go to:
   http://127.0.0.1:5000/
5. Enter text in the input box and click predict to see the detected emotion.
