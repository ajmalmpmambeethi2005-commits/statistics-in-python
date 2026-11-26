
from scipy.stats import poisson

# Average number of calls per hour
lam = 6

# Required number of calls
k = 4

# Exact probability
probability = poisson.pmf(k, lam)

# Mean and variance
mean = lam
variance = lam

print("Probability:", probability)
print("Percentage:", probability * 100)
print("Mean:", mean)
print("Variance:", variance)
