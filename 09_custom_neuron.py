import numpy as np
import time

print("--- 🧠 PURE NUMPY NEURAL NETWORK ENGINE ---")

# 1. THE DATA (Pattern: y = 2X - 1)
X = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0])
y = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0])

# 2. INITIALIZE ARBITRARY BRAIN VALUES (Starting guesses)
weight = 0.5   
bias = 0.0     
learning_rate = 0.05  # How fast the AI adjusts its parameters

print(f"Starting guesses before training -> Weight: {weight}, Bias: {bias}")
print("🏋️ Training neuron over 500 epochs...")

# 3. TRAINING LOOP (The Optimization Process)
for epoch in range(500):
    for i in range(len(X)):
        # Calculate prediction: y = (X * w) + b
        prediction = (X[i] * weight) + bias
        
        # Calculate error (How far off was the guess?)
        error = prediction - y[i]
        
        # Adjust weight and bias using Gradient Descent math
        weight = weight - (learning_rate * error * X[i])
        bias = bias - (learning_rate * error)

print("Training Complete!")
print("-" * 40)
print(f"Calculated Final Weight: {weight:.4f} (Target: 2.0)")
print(f"Calculated Final Bias:   {bias:.4f} (Target: -1.0)")
print("-" * 40)

# 4. LIVE PREDICTION TEST
test_val = 10.0
final_prediction = (test_val * weight) + bias
print(f"🔮 PREDICTION: When input is 10.0, the custom neuron predicts: {final_prediction:.4f}")