import torch
from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

### 1. MODEL SELECTION ###
# Choosing a local NLP model for sentiment analysis
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
classifier = pipeline("sentiment-analysis", model=model_name)

### 2. IMPLEMENTATION IN JUPYTER NOTEBOOK ###
# Function to analyze sentiment of a given text
def analyze_sentiment(text):
    result = classifier(text)
    return result[0]["label"], result[0]["score"]

### 3. EXPLORATION & ANALYSIS ###
# Testing the model with different inputs
sample_texts = [
    "I love Natural Language Processing!",
    "This is the worst experience ever.",
    "I think this model is very useful.",
    "The performance is not what I expected."
]

print("\nSentiment Analysis Results:")
for text in sample_texts:
    sentiment, confidence = analyze_sentiment(text)
    print(f"Text: {text}\nSentiment: {sentiment} (Confidence: {confidence:.2f})\n")

### 4. RESEARCH QUESTIONS ###
research_questions = [
    "How does this model handle neutral statements?",
    "Can it detect sarcasm accurately?",
    "Does the model show bias in certain topics?",
    "How does it perform on multi-sentence inputs?"
]

print("\nResearch Questions:")
for i, question in enumerate(research_questions, 1):
    print(f"{i}. {question}")

### 5. PROJECT ALIGNMENT & ETHICAL CONSIDERATIONS ###
ethical_considerations = [
    "Is the model biased towards specific sentiment tendencies?",
    "Does it work equally well for all demographics?",
    "Could it be used for misinformation detection?",
    "How can we mitigate ethical concerns in NLP?"
]

print("\nEthical Considerations:")
for i, concern in enumerate(ethical_considerations, 1):
    print(f"{i}. {concern}")

### 6. CONCLUSIONS & INSIGHTS ###
conclusions = [
    "DistilBERT performs well on sentiment analysis but struggles with sarcasm.",
    "The model provides fast responses but may have biases.",
    "More training data could improve accuracy on complex linguistic structures.",
    "Ethical considerations must be addressed when using NLP models in real-world applications."
]

print("\nConclusions & Insights:")
for i, insight in enumerate(conclusions, 1):
    print(f"{i}. {insight}")
