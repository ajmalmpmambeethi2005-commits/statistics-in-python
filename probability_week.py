
import numpy as np

# Step 1: Define the possible dice outcomes
dice = [1, 2, 3, 4, 5, 6]

# Step 2: Simulate 1000 dice rolls
results = np.random.choice(dice, size=1000)

# Step 3: Count how many times each number appears
values, counts = np.unique(results, return_counts=True)

# Step 4: Calculate the experimental probability
total_rolls = len(results)

print("Dice Probability Analysis")
print("-------------------------")

for value, count in zip(values, counts):
    probability = count / total_rolls

    print(f"Number: {value}")
    print(f"Count: {count}")
    print(f"Probability: {probability:.3f}")
    print()
