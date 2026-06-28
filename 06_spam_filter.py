import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. LOAD THE TEXT DATA
df = pd.read_csv("spam_data.csv")

X = df['Message']  # The text messages (Features)
y = df['Label']    # 'spam' or 'ham' (Labels)

# 2. SPLIT THE DATA
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 3. TEXT TO NUMBERS (VECTORIZATION)
# CountVectorizer counts how many times each word appears in the text
vectorizer = CountVectorizer()
X_train_counts = vectorizer.fit_transform(X_train)
X_test_counts = vectorizer.transform(X_test)

# 4. INITIALIZE AND TRAIN THE AI (Naive Bayes Classifier)
model = MultinomialNB()
model.fit(X_train_counts, y_train)

# 5. TEST ACCURACY
accuracy = model.score(X_test_counts, y_test)
print("--- 🛡️ AI SPAM FILTER ACTIVE ---")
print(f"Model Accuracy on Test Messages: {accuracy * 100:.2f}%\n")

# 6. TEST IT WITH YOUR OWN CUSTOM SENTENCES!
# Let's give the AI two brand new messages it has never seen before
custom_messages = [
    "Hey dude, let's play Roblox later tonight after doing our coding projects.",
    "WIN FREE MONEY NOW!!! CLICK THIS LINK TO GET 100000 ROBUX FREE CASH"
]

# Convert our custom messages into numbers using the exact same vectorizer
custom_counts = vectorizer.transform(custom_messages)
predictions = model.predict(custom_counts)

print("--- 🔮 LIVE SYSTEM PREDICTIONS ---")
for msg, pred in zip(custom_messages, predictions):
    print(f"Message: \"{msg}\"")
    print(f"AI Classification: 🔴 [{pred.upper()}]\n")