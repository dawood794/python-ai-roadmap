from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. Dataset
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [15, 25, 35, 42, 50, 62, 71, 80, 92, 98]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# 2. Check BOTH scores
# Score on the data it SAW (Practice Test)
train_accuracy = model.score(X_train, y_train) 

# Score on the data it DID NOT SEE (Real Exam)
test_accuracy = model.score(X_test, y_test)   

print("--- ⚖️ FIT CHECK RESULTS ---")
print(f"Training Accuracy (Practice Test): {train_accuracy * 100:.2f}%")
print(f"Testing Accuracy (Real Exam):     {test_accuracy * 100:.2f}%")

# 3. Simple logic to tell us how we did
difference = abs(train_accuracy - test_accuracy) * 100

if train_accuracy > 0.95 and test_accuracy < 0.70:
    print("\nResult: 🚨 OVERFITTING! It memorized the training data but failed the exam.")
elif train_accuracy < 0.60:
    print("\nResult: 🚧 UNDERFITTING! The model is too weak and didn't learn anything.")
else:
    print("\nResult: ✅ GOOD FIT! The model generalized well to unseen data.")