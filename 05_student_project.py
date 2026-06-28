import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 1. LOAD DATA FROM CSV
# We use pandas to read our file just like a real project
df = pd.read_csv("student_data.csv")

print("--- 📄 DATASET LOADED ---")
print(df.head(), "\n") # Shows the first few rows

# 2. SEPARATE FEATURES AND LABELS
# We use TWO features now: Study_Hours and Attendance_Percentage
X = df[['Study_Hours', 'Attendance_Percentage']] 
y = df['Final_Marks']

# 3. THE SPLIT (70% Train, 30% Test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

# 4. TRAIN THE MODEL
model = LinearRegression()
model.fit(X_train, y_train)

# 5. EVALUATE
train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)

print("--- ⚖️ PERFORMANCE RESULTS ---")
print(f"Training Accuracy: {train_acc * 100:.2f}%")
print(f"Testing Accuracy:  {test_acc * 100:.2f}%\n")

# 6. MAKE A CUSTOM PREDICTION
# Let's predict marks for a student who studies 6.5 hours and has 90% attendance
new_student = [[6.5, 90]] 
predicted_mark = model.predict(new_student)

print("--- 🔮 REAL PREDICTION ---")
print(f"A student studying 6.5 hours with 90% attendance is predicted to score: {predicted_mark[0]:.1f} marks!")