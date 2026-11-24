
# Bernoulli Distribution

p = 0.7

# Probability of success
success = p

# Probability of failure
failure = 1 - p

# Mean
mean = p

# Variance
variance = p * (1 - p)

# Standard deviation
import math
standard_deviation = math.sqrt(variance)

print("Probability of Success:", success)
print("Probability of Failure:", failure)
print("Mean:", mean)
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)
