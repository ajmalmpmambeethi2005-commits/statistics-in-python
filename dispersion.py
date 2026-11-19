import numpy as np
from scipy import stats

data = [2, 4, 6, 8, 10]

# Range
data_range = max(data) - min(data)

# Variance
population_variance = np.var(data)
sample_variance = np.var(data, ddof=1)

# Standard Deviation
population_std = np.std(data)
sample_std = np.std(data, ddof=1)

# Coefficient of Variation
cv = (population_std / np.mean(data)) * 100

# Z-Scores
z_scores = stats.zscore(data)

print("Range:", data_range)
print("Population Variance:", population_variance)
print("Sample Variance:", sample_variance)
print("Population SD:", population_std)
print("Sample SD:", sample_std)
print("Coefficient of Variation:", cv)
print("Z-Scores:", z_scores)
