
# Bayes' Theorem - Medical Test Example

# Given probabilities
p_disease = 0.01
p_no_disease = 0.99

p_positive_given_disease = 0.99
p_positive_given_no_disease = 0.05

# Calculate total probability of a positive result
p_positive = (
    p_positive_given_disease * p_disease
    + p_positive_given_no_disease * p_no_disease
)

# Apply Bayes' Theorem
p_disease_given_positive = (
    p_positive_given_disease * p_disease
) / p_positive

# Display results
print("Probability of a positive test:", p_positive)
print(
    "Probability of disease given positive test:",
    p_disease_given_positive
)

print(
    "Percentage:",
    round(p_disease_given_positive * 100, 2), "%"
)
