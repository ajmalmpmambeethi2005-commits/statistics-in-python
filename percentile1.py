import numpy as np

marks = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

p25 = np.percentile(marks, 25)
p50 = np.percentile(marks, 50)
p75 = np.percentile(marks, 75)

print("25th Percentile:", p25)
print("50th Percentile:", p50)
print("75th Percentile:", p75)