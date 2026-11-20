import numpy as np

data = [10, 20, 30, 40, 50, 60, 70, 80]

q1 = np.percentile(data, 25)
q3 = np.percentile(data, 75)

iqr = q3 - q1

print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)