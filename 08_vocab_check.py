from sklearn.feature_extraction.text import CountVectorizer

# 1. A tiny sample of text messages
sample_messages = [
    "Free Robux click here",
    "Hey friend call me"
]

# 2. Initialize the vectorizer
vectorizer = CountVectorizer()

# 3. Let it read the text and build its word index
X_counts = vectorizer.fit_transform(sample_messages)

print("--- 📖 THE AI'S VOCABULARY DICTIONARY ---")
# This shows the exact index number given to each unique word
print(vectorizer.vocabulary_)
print("-" * 40)

print("--- 🔢 THE TEXT TRANSFORMED INTO NUMBERS ---")
# This turns the sentences into raw numeric counts
print(X_counts.toarray())