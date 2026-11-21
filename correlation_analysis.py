import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "Flight_Distance": [300, 500, 700, 900, 1100],
    "Departure_Delay": [10, 20, 15, 40, 50],
    "Arrival_Delay": [15, 25, 20, 45, 55],
    "Ticket_Price": [1000, 1500, 2000, 2500, 3000]
}

df = pd.DataFrame(data)

print(df)

print(df.cov())
print(df.corr(method="pearson"))

sns.scatterplot(
    data=df,
    x="Departure_Delay",
    y="Arrival_Delay"
)

plt.title("Departure Delay vs Arrival Delay")
plt.show()

sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

plt.title("Correlation Matrix")
plt.show()