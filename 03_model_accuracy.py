from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. THE DATASET (10 Students)
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]] # Study Hours (Features)
y = [15, 25, 35, 42, 50, 62, 71, 80, 92, 98]          # Marks Scored (Labels)

# 2. AUTOMATIC TRAIN/TEST SPLIT
# We set test_size=0.20 (20%), which means 2 out of 10 rows go to the final exam!
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# 3. INITIALIZE AND TRAIN THE AI
model = LinearRegression()
model.fit(X_train, y_train)  # The AI builds its formula ONLY using training data

print("--- 🎯 AI MODEL EVALUATION ---")

# 4. EXAM TIME: PREDICT ON UNSEEN TEST DATA
predictions = model.predict(X_test)

# Show what questions were on the exam vs what the AI guessed
print(f"Exam Questions (Hours Studied): {X_test}")
print(f"Real Answers   (Actual Marks):  {y_test}")
print(f"AI's Guesses   (Predicted):     [{predictions[0]:.1f}, {predictions[1]:.1f}]")
print("-" * 50)

# 5. GET THE ACCURACY SCORE
# .score() evaluates how close the AI's guesses were to the real exam answers
accuracy = model.score(X_test, y_test)
print(f"Final Model Accuracy Score: {accuracy * 100:.2f}%")