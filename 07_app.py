import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. TRAIN THE AI ENGINE (Just like before)
df = pd.read_csv("spam_data.csv")
X = df['Message']
y = df['Label']

vectorizer = CountVectorizer()
X_counts = vectorizer.fit_transform(X)

model = MultinomialNB()
model.fit(X_counts, y)

# 2. BUILD THE WEB INTERFACE
st.title("🛡️ AI Cyber-Spam Detector")
st.write("Type or paste any suspicious message below, and our trained Naive Bayes AI will analyze it instantly.")

# Create a text input box for the user
user_input = st.text_input("Enter your message here:", placeholder="e.g., You won a free phone! Click here...")

# Create a trigger button
if st.button("Analyze Message"):
    if user_input.strip() != "":
        # Process the input and predict
        input_counts = vectorizer.transform([user_input])
        prediction = model.predict(input_counts)[0]
        
        # Display the result with clean web styling
        if prediction == "spam":
            st.error("🚨 WARNING: This message looks like SPAM / SCAM!")
        else:
            st.success("✅ SAFE: This looks like a legitimate message (HAM).")
    else:
        st.warning("Please type a message first!")