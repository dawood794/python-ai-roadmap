import random

# 1. OUR RAW DATA
X = [[1], [2], [3], [4], [5]]  # Hours studied
y = [15, 25, 35, 45, 55]       # Marks scored

print("--- 1. BEFORE SHUFFLING ---")
print(f"X: {X}")
print(f"y: {y}\n")

# 2. COMBINE (ZIP) THE DATA
# If we shuffle X and y separately, they will get mismatched!
# zip() pairs them up: ([1], 15), ([2], 25), etc.
combined = list(zip(X, y))

# 3. SHUFFLE THE PACKED DATA
# This randomizes the order completely
random.seed(42)  # This keeps the shuffle exactly the same every time we run it
random.shuffle(combined)

print("--- 2. AFTER SHUFFLING (PAIRED TOGETHER) ---")
print(f"{combined}\n")

# 4. DEFINE SPLIT SIZE
# We want 20% for testing. 20% of 5 items is 1 item.
test_size = 0.20
num_test_items = int(len(combined) * test_size)  # This equals 1

# 5. SLICE THE LISTS
# Test data gets the first 'num_test_items' elements
test_pairs = combined[:num_test_items]
# Train data gets the rest of the elements
train_pairs = combined[num_test_items:]

# 6. UNPACK THEM BACK INTO X AND y BUCKETS
X_train = [pair[0] for pair in train_pairs]
y_train = [pair[1] for pair in train_pairs]

X_test = [pair[0] for pair in test_pairs]
y_test = [pair[1] for pair in test_pairs]

# 7. PRINT THE MANUAL RESULTS
print("--- 3. FINAL MANUAL BUCKETS ---")
print(f"X_train (Hours): {X_train}")
print(f"y_train (Marks): {y_train}")
print("-" * 30)
print(f"X_test (Hours):  {X_test}")
print(f"y_test (Marks):  {y_test}")