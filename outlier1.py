import numpy as np

data = [10, 12, 13, 14, 15, 16, 18, 100]

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

iqr = q3 - q1

lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

outliers = [
    x for x in data
    if x < lower or x > upper
]

print("IQR:", iqr)
print("Lower Fence:", lower)
print("Upper Fence:", upper)
print("Outliers:", outliers)