import numpy as np
from scipy import stats

# Student marks
marks = [45, 60, 75, 80, 90, 55, 65, 70, 95, 85]

# Basic statistics
mean = np.mean(marks)
median = np.median(marks)
minimum = np.min(marks)
maximum = np.max(marks)

# Dispersion
data_range = np.ptp(marks)
variance = np.var(marks)
std_deviation = np.std(marks)

# Coefficient of Variation
cv = (std_deviation / mean) * 100

# Z-scores
z_scores = stats.zscore(marks)

# Results
print("STUDENT PERFORMANCE ANALYSIS")
print("-----------------------------")
print("Average Marks:", mean)
print("Median Marks:", median)
print("Minimum Marks:", minimum)
print("Maximum Marks:", maximum)
print("Range:", data_range)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)
print("Coefficient of Variation:", cv)
print("Z-Scores:", z_scores)