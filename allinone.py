
from scipy.stats import bernoulli, binom, geom, poisson

# 1. BERNOULLI
p = 0.7

print("\nBERNOULLI")
print("Success:", bernoulli.pmf(1, p))
print("Failure:", bernoulli.pmf(0, p))
print("Mean:", p)
print("Variance:", p * (1 - p))


# 2. BINOMIAL
n = 5
p = 0.7
k = 3

print("\nBINOMIAL")
print("Exactly 3:", binom.pmf(k, n, p))
print("At most 3:", binom.cdf(k, n, p))
print("Mean:", n * p)
print("Variance:", n * p * (1 - p))


# 3. GEOMETRIC
p = 0.2
k = 3

print("\nGEOMETRIC")
print("First success on trial 3:", geom.pmf(k, p))
print("Mean:", 1 / p)
print("Variance:", (1 - p) / p**2)


# 4. POISSON
lam = 6
k = 4

print("\nPOISSON")
print("Exactly 4 events:", poisson.pmf(k, lam))
print("At most 4 events:", poisson.cdf(k, lam))
print("Mean:", lam)
print("Variance:", lam)
