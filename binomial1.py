
from scipy.stats import binom

# Given values
n = 5
p = 0.7
k = 3

# Probability of exactly 3 successes
probability = binom.pmf(k, n, p)

# Expected value
mean = n * p

# Variance
variance = n * p * (1 - p)

print("Probability:", probability)
print("Percentage:", probability * 100)
print("Mean:", mean)
print("Variance:", variance)
